"""Mission 023 frozen visible-surface experiment with complete diff accounting."""
import hashlib
import json
import os
import pty
import re
import select
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
TARGETS = {
    "isolated": ROOT / "fixture/surfaces/isolated.py",
    "neighborhood": ROOT / "fixture/surfaces/neighborhood.py",
    "module": ROOT / "fixture/surfaces/module.py",
}
MODEL = "ollama_chat/qwen2.5-coder-3b-cpu:latest"
BASELINE = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
PLACEHOLDER = re.compile(r"(?:path/to/|\.\.\./|<[^>]+>)")


def run(cmd, env=None, timeout=300):
    return subprocess.run(cmd, cwd=REPO, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)


def pty_aider(prompt, target, env, timeout=420):
    master, slave = pty.openpty()
    started = time.time()
    process = subprocess.Popen(
        ["aider", "--model", MODEL, "--edit-format", "whole", "--no-auto-commits", "--no-gitignore",
         "--no-show-model-warnings", "--yes-always", "--message-file", str(prompt), str(target.relative_to(REPO))],
        cwd=REPO, env=env, stdin=subprocess.DEVNULL, stdout=slave, stderr=subprocess.PIPE,
        close_fds=True,
    )
    os.close(slave)
    output = bytearray()
    while process.poll() is None:
        ready, _, _ = select.select([master], [], [], 1.0)
        if ready:
            try:
                output.extend(os.read(master, 65536))
            except OSError:
                break
        if time.time() - started > timeout:
            process.kill()
            break
    while True:
        try:
            output.extend(os.read(master, 65536))
        except OSError:
            break
    stderr = process.stderr.read().decode(errors="replace")
    os.close(master)
    return process.returncode if process.returncode is not None else 124, output.decode(errors="replace"), stderr, time.time() - started


def main():
    fixture = ROOT / "fixture"
    env = dict(os.environ, PYTHONPATH=str(fixture), AIDER_CACHE_DIR="/tmp/aider-mission-023-cache")
    for condition, target in TARGETS.items():
        for number in range(1, 4):
            attempt = ROOT / "attempts" / condition / ("valid_%03d" % number)
            raw = attempt / "raw"
            if attempt.exists():
                raise SystemExit("refusing to overwrite %s" % attempt)
            raw.mkdir(parents=True)
            rel = target.relative_to(REPO)
            reset = run(["git", "restore", "--source=" + BASELINE, "--staged", "--worktree", "--", str(rel)])
            (raw / "reset.log").write_text(reset.stdout + reset.stderr)
            baseline = run(["python3", "-m", "pytest", "-q", str(fixture / "test_surfaces.py")], env=env)
            (raw / "baseline_proof.log").write_text(baseline.stdout + baseline.stderr)
            oracle_hash = hashlib.sha256((ROOT / "proof/oracle.py").read_bytes()).hexdigest()
            prompt = ("Goal: Add cents_to_label(cents), returning a dollar string with exactly two decimals.\n"
                      "Allowed scope: %s only.\nDo not change tests, proofs, or unrelated behavior.\n"
                      "Proof: the controller will run the independent oracle and the regression suite.\n" % rel)
            (attempt / "AIDER_PROMPT.md").write_text(prompt)
            (attempt / "PREDICTION.md").write_text("One target source file gains one cents_to_label function; no other paths change; oracle passes.\n")
            (attempt / "RUN_PLAN.md").write_text("Mission 023; condition=%s; repetition=%d; baseline=%s; model=%s; warm before timing; PTY caller.\n" % (condition, number, BASELINE, MODEL))
            warm = run(["ollama", "run", MODEL.split("/", 1)[1], "Reply WARM only."], timeout=300)
            (raw / "warm.log").write_text(warm.stdout + warm.stderr)
            code, stdout, stderr, elapsed = pty_aider(attempt / "AIDER_PROMPT.md", target, env)
            (raw / "aider_stdout.log").write_text(stdout)
            (raw / "aider_stderr.log").write_text(stderr)
            status = run(["git", "status", "--porcelain=v1"])
            (raw / "git_status.log").write_text(status.stdout + status.stderr)
            for label, args in (("unstaged", ["git", "diff", "--", str(rel)]), ("cached", ["git", "diff", "--cached", "--", str(rel)]), ("head", ["git", "diff", "HEAD", "--", str(rel)])):
                diff = run(args)
                (raw / ("git_diff_%s.patch" % label)).write_text(diff.stdout)
            oracle = run(["python3", str(ROOT / "proof/oracle.py"), str(target), condition], env=env)
            (raw / "final_proof.log").write_text(oracle.stdout + oracle.stderr)
            regression = run(["python3", "-m", "pytest", "-q", str(fixture / "test_surfaces.py")], env=env)
            (raw / "regression_proof.log").write_text(regression.stdout + regression.stderr)
            status_text = status.stdout + stdout + stderr
            paths = re.findall(r"(?:^|\n)[MADRCU?! ]{1,3}\s+(.+)", status.stdout)
            forbidden = [p for p in paths if not p.startswith(str(rel)) and not p.startswith("sidecar/experiments/aider_classroom_bite_research_023/")]
            placeholder = bool(PLACEHOLDER.search(status_text))
            head_diff = run(["git", "diff", "HEAD", "--", str(rel)]).stdout
            engineering = baseline.returncode == 0 and oracle.returncode == 0 and regression.returncode == 0 and bool(head_diff)
            aider_success = engineering and not forbidden and not placeholder and code == 0
            (raw / "timing.json").write_text(json.dumps({"elapsed_seconds": elapsed, "exit_code": code, "model": MODEL, "warm_policy": "exact-model request before each attempt", "pty": True}, indent=2) + "\n")
            (attempt / "RECEIPT.md").write_text("condition=%s\nrepetition=%d\nbaseline=%s\ntarget=%s\nmodel=%s\noracle_sha256=%s\naider_exit=%d\nelapsed_seconds=%.3f\nengineering_success=%s\naider_success=%s\nforbidden_paths=%s\nplaceholder_transport=%s\n" % (condition, number, BASELINE, rel, MODEL, oracle_hash, code, elapsed, engineering, aider_success, forbidden, placeholder))
            (attempt / "AFTER_ACTION.md").write_text("ENGINEERING SUCCESS: %s\nAIDER SUCCESS: %s\nCLASSROOM FIT, MACHINE-SIDE PROVISIONAL: assess latency, diff size, prediction mismatch, and proof burden.\nTarget: %s\n" % (engineering, aider_success, rel))
            cleanup = run(["git", "restore", "--source=" + BASELINE, "--staged", "--worktree", "--", str(rel)])
            (raw / "cleanup.log").write_text(cleanup.stdout + cleanup.stderr)


if __name__ == "__main__":
    main()

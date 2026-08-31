"""Mission 024 matched whole-vs-diff Aider transport experiment."""
import hashlib
import json
import os
import pty
import re
import select
import subprocess
import sys
import time
import fcntl
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
TARGET = REPO / "aider_surface_fixture/module.py"
PLACEHOLDER_TARGET = REPO / "path/to/aider_surface_fixture/module.py"
MODEL = "ollama_chat/qwen2.5-coder-3b-cpu:latest"
FORMATS = ("diff",)
BASELINE = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
PLACEHOLDER = re.compile(r"(?:path/to/|\.\.\./|<[^>]+>)")
PROMPT = (
    "Goal: Add cents_to_label(cents). For a non-negative integer number of cents, "
    "return a dollar string with exactly two decimals; for example, 125 -> '$1.25' "
    "and 0 -> '$0.00'. Reject negative cents with ValueError.\n"
    "Allowed scope: aider_surface_fixture/module.py only.\n"
    "Do not change tests, proofs, or unrelated behavior.\n"
    "Proof: the controller will run the independent oracle and the regression suite.\n"
)


def run(cmd, env=None, timeout=300):
    return subprocess.run(cmd, cwd=REPO, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)


def pty_aider(prompt, edit_format, env, label, timeout=420):
    master, slave = pty.openpty()
    started = time.time()
    process = subprocess.Popen(
        ["aider", "--model", MODEL, "--edit-format", edit_format, "--no-auto-commits", "--no-gitignore",
         "--no-show-model-warnings", "--yes-always", "--chat-history-file", "/tmp/aider-mission-024-%s-chat.md" % label,
         "--input-history-file", "/tmp/aider-mission-024-%s-input.history" % label,
         "--llm-history-file", "/tmp/aider-mission-024-%s-llm.history" % label,
         "--message-file", str(prompt), str(TARGET.relative_to(REPO))],
        cwd=REPO, env=env, stdin=subprocess.DEVNULL, stdout=slave, stderr=subprocess.PIPE, close_fds=True,
    )
    os.close(slave)
    flags = fcntl.fcntl(master, fcntl.F_GETFL)
    fcntl.fcntl(master, fcntl.F_SETFL, flags | os.O_NONBLOCK)
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
    drain_deadline = time.time() + 3
    while time.time() < drain_deadline:
        try:
            chunk = os.read(master, 65536)
            if not chunk:
                break
            output.extend(chunk)
            drain_deadline = time.time() + 0.25
        except OSError:
            ready, _, _ = select.select([master], [], [], 0.1)
            if not ready:
                break
    if process.poll() is None:
        process.wait(timeout=30)
    stderr = process.stderr.read().decode(errors="replace")
    os.close(master)
    return process.returncode, output.decode(errors="replace"), stderr, time.time() - started


def text(result):
    return result.stdout + result.stderr


def attempt(format_name, label, scored):
    bucket = "attempts" if scored else "verification"
    suffix = "valid_%03d" % label if scored else "attempt_%03d" % label
    attempt_dir = ROOT / bucket / format_name / suffix
    raw = attempt_dir / "raw"
    if attempt_dir.exists():
        raise SystemExit("refusing to overwrite %s" % attempt_dir)
    raw.mkdir(parents=True)
    rel = str(TARGET.relative_to(REPO))
    reset = run(["git", "restore", "--source=" + BASELINE, "--staged", "--worktree", "--", rel, str(PLACEHOLDER_TARGET.relative_to(REPO))])
    (raw / "reset.log").write_text(text(reset))
    env = dict(os.environ, PYTHONPATH=str(ROOT / "../aider_classroom_bite_research_023/fixture"), AIDER_CACHE_DIR="/tmp/aider-mission-024-cache")
    baseline = run(["python3", "-m", "pytest", "-q", str(ROOT / "../aider_classroom_bite_research_023/fixture/test_surfaces.py")], env=env)
    (raw / "baseline_proof.log").write_text(text(baseline))
    prompt_path = attempt_dir / "AIDER_PROMPT.md"
    prompt_path.write_text(PROMPT)
    (attempt_dir / "PREDICTION.md").write_text("One target source file gains one cents_to_label function; no other paths change; oracle passes. The alternate transport may reduce placeholder-path emissions.\n")
    (attempt_dir / "RUN_PLAN.md").write_text("Mission 024; format=%s; scored=%s; repetition=%s; baseline=%s; model=%s; warm before timing; PTY caller.\n" % (format_name, scored, label, BASELINE, MODEL))
    warm = run(["ollama", "run", MODEL.split("/", 1)[1], "Reply WARM only."], timeout=300)
    (raw / "warm.log").write_text(text(warm))
    code, stdout, stderr, elapsed = pty_aider(prompt_path, format_name, env, "%s-%s-%s" % (format_name, bucket, label))
    (raw / "aider_stdout.log").write_text(stdout)
    (raw / "aider_stderr.log").write_text(stderr)
    status = run(["git", "status", "--porcelain=v1"])
    (raw / "git_status.log").write_text(text(status))
    for name, args in (("unstaged", ["git", "diff", "--", rel]), ("cached", ["git", "diff", "--cached", "--", rel]), ("head", ["git", "diff", "HEAD", "--", rel])):
        (raw / ("git_diff_%s.patch" % name)).write_text(run(args).stdout)
    staged = run(["git", "diff", "--cached", "--name-only"])
    unstaged = run(["git", "diff", "--name-only"])
    (raw / "paths_staged.log").write_text(text(staged))
    (raw / "paths_unstaged.log").write_text(text(unstaged))
    status_text = text(status) + stdout + stderr
    placeholder_hits = PLACEHOLDER.findall(status_text)
    (raw / "placeholder_scan.log").write_text("filesystem_and_raw_placeholder=%s\nhits=%r\n" % (bool(placeholder_hits), placeholder_hits))
    allowed = {rel}
    forbidden = []
    for line in status.stdout.splitlines():
        path = line[3:] if len(line) >= 4 else ""
        if path and path not in allowed and not path.startswith("sidecar/experiments/aider_classroom_bite_research_024/"):
            forbidden.append(path)
    (raw / "forbidden_paths.log").write_text("forbidden=%r\n" % forbidden)
    oracle = run(["python3", str(ROOT / "../aider_classroom_bite_research_023/proof/oracle.py"), str(TARGET), "module"], env=env)
    (raw / "final_proof.log").write_text(text(oracle))
    regression = run(["python3", "-m", "pytest", "-q", str(ROOT / "../aider_classroom_bite_research_023/fixture/test_surfaces.py")], env=env)
    (raw / "regression_proof.log").write_text(text(regression))
    head_diff = run(["git", "diff", "HEAD", "--", rel]).stdout
    engineering = baseline.returncode == 0 and oracle.returncode == 0 and regression.returncode == 0 and bool(head_diff)
    aider_success = engineering and not forbidden and not placeholder_hits and code == 0
    timing = {"elapsed_seconds": elapsed, "exit_code": code, "model": MODEL, "edit_format": format_name, "warm_policy": "exact-model request before each attempt", "pty": True, "scored": scored}
    (raw / "timing.json").write_text(json.dumps(timing, indent=2) + "\n")
    (attempt_dir / "RECEIPT.md").write_text("format=%s\nscored=%s\nrepetition=%s\nbaseline=%s\ntarget=%s\nmodel=%s\naider_exit=%d\nelapsed_seconds=%.3f\nengineering_success=%s\naider_success=%s\nforbidden_paths=%r\nplaceholder_transport=%s\n" % (format_name, scored, label, BASELINE, rel, MODEL, code, elapsed, engineering, aider_success, forbidden, bool(placeholder_hits)))
    (attempt_dir / "AFTER_ACTION.md").write_text("ENGINEERING SUCCESS: %s\nAIDER SUCCESS: %s\nCLASSROOM FIT, MACHINE-SIDE PROVISIONAL: assess latency, diff size, prediction mismatch, and proof burden.\nFormat: %s\nTarget: %s\n" % (engineering, aider_success, format_name, rel))
    cleanup = run(["git", "restore", "--source=" + BASELINE, "--staged", "--worktree", "--", rel, str(PLACEHOLDER_TARGET.relative_to(REPO))])
    (raw / "cleanup.log").write_text(text(cleanup))


def main():
    for format_name in FORMATS:
        numbers = range(3, 6) if format_name == "whole" else range(5, 6)
        for number in numbers:
            attempt(format_name, number, True)


if __name__ == "__main__":
    main()

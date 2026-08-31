"""Mission 028: whole-vs-diff replication on a string-processing MODULE fixture."""
import hashlib
import json
import os
import pty
import re
import select
import signal
import shutil
import subprocess
import time
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
TARGET = REPO / "sidecar/experiments/aider_classroom_bite_research_028/fixture/string_module.py"
PLACEHOLDER = "path/to/sidecar/experiments/aider_classroom_bite_research_028/fixture/string_module.py"
MODEL = "ollama_chat/qwen2.5-coder-3b-cpu:latest"
BASELINE = "REPLACE_WITH_BASELINE_COMMIT"
REL = "sidecar/experiments/aider_classroom_bite_research_028/fixture/string_module.py"
FORBIDDEN = re.compile(r"(?:path/to/|\.\.\./|<path(?:/|\\)|<TARGET(?:/|\\))")
PROMPT = (
    "Goal: add initials(full_name) to the fixed string MODULE fixture at " + REL + ".\n"
    "Behavior: return uppercase initials for each whitespace-separated name part; ignore repeated/leading/trailing whitespace; raise ValueError for blank/whitespace-only input.\n"
    "Allowed scope: the exact target module only.\n"
    "Do not change: tests, oracle, unrelated helpers, unrelated behavior, or any other path.\n"
    "Proof: fixed behavioral oracle plus regression proof.\n"
)


def run(args, env=None, timeout=300):
    return subprocess.run(args, cwd=REPO, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value)


def pty_aider(prompt, fmt, env, raw, timeout=360):
    master, slave = pty.openpty()
    err_path = raw / "aider_stderr.log"
    started = time.time()
    with err_path.open("w") as err:
        proc = subprocess.Popen(
            ["aider", "--model", MODEL, "--edit-format", fmt, "--no-auto-commits", "--no-gitignore",
             "--no-show-model-warnings", "--yes-always", "--chat-history-file", str(raw / "chat_history.md"),
             "--input-history-file", str(raw / "input.history"), "--llm-history-file", str(raw / "llm.history"),
             "--message-file", str(prompt), REL],
            cwd=REPO, env=env, stdin=subprocess.DEVNULL, stdout=slave, stderr=err,
            close_fds=True, start_new_session=True,
        )
        os.close(slave)
        flags = __import__("fcntl").fcntl(master, __import__("fcntl").F_GETFL)
        __import__("fcntl").fcntl(master, __import__("fcntl").F_SETFL, flags | os.O_NONBLOCK)
        output = bytearray()
        timed_out = False
        while proc.poll() is None:
            ready, _, _ = select.select([master], [], [], 1.0)
            if ready:
                try:
                    chunk = os.read(master, 65536)
                    if chunk:
                        output.extend(chunk)
                except OSError:
                    pass
            if time.time() - started > timeout:
                timed_out = True
                os.killpg(proc.pid, signal.SIGTERM)
                try:
                    proc.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    proc.wait(timeout=10)
                break
        for _ in range(20):
            try:
                chunk = os.read(master, 65536)
                if not chunk:
                    break
                output.extend(chunk)
            except OSError:
                break
            time.sleep(0.05)
        if proc.poll() is None:
            proc.wait(timeout=10)
    os.close(master)
    lifecycle = "timeout; process-group terminated and reaped" if timed_out else "child exited and was reaped"
    write(raw / "process_lifecycle.log", "pid=%s\n%s\nexit_code=%s\n" % (proc.pid, lifecycle, proc.returncode))
    return (None if timed_out else proc.returncode), output.decode(errors="replace"), time.time() - started, timed_out


def reset(label):
    result = run(["git", "restore", "--source=" + BASELINE, "--staged", "--worktree", "--", REL])
    run(["git", "reset", "--", "path/to"])
    placeholder_tree = REPO / "path" / "to"
    if placeholder_tree.exists():
        shutil.rmtree(REPO / "path")
    stray = REPO / "aider_classroom_bite_research_022"
    run(["git", "reset", "--", "aider_classroom_bite_research_022"])
    if stray.exists():
        shutil.rmtree(stray)
    placeholder_path = REPO / PLACEHOLDER
    if placeholder_path.exists():
        placeholder_path.unlink()
    cache = REPO / ".aider.tags.cache.v4"
    if cache.exists():
        shutil.rmtree(cache)
    write(label / "raw/reset.log", result.stdout + result.stderr)
    return result.returncode == 0


def attempt(fmt, n, scored):
    bucket = "attempts" if scored else "verification"
    dest = ROOT / bucket / fmt / ("valid_%03d" % n if scored else "attempt_%03d" % n)
    if dest.exists():
        raise SystemExit("refusing to overwrite " + str(dest))
    raw = dest / "raw"
    raw.mkdir(parents=True)
    write(dest / "RUN_PLAN.md", "Mission 028; format=%s; scored=%s; repetition=%s; baseline=%s; model=%s; timeout=360s.\n" % (fmt, scored, n, BASELINE, MODEL))
    write(dest / "AIDER_PROMPT.md", PROMPT)
    write(dest / "PREDICTION.md", "One target source file gains initials; no other paths change; oracle passes.\n")
    status = "VALID_COMPLETE"
    if not reset(dest):
        status = "INVALID_RESET"
    env = dict(os.environ, PYTHONPATH=str(ROOT / "fixture"), AIDER_CACHE_DIR="/tmp/aider-mission-028-cache")
    baseline = run(["python3", "-m", "pytest", "-q", str(ROOT / "fixture" / "test_string_surface.py")], env=env)
    write(raw / "baseline_proof.log", baseline.stdout + baseline.stderr)
    warm = run(["ollama", "run", MODEL.split("/", 1)[1], "Reply WARM only."], timeout=300)
    write(raw / "warm.log", warm.stdout + warm.stderr)
    if status == "VALID_COMPLETE":
        code, stdout, elapsed, timed_out = pty_aider(dest / "AIDER_PROMPT.md", fmt, env, raw)
        write(raw / "aider_stdout.log", stdout)
        if timed_out:
            status = "INVALID_TIMEOUT"
    else:
        code, stdout, elapsed = None, "", 0.0
        write(raw / "aider_stdout.log", "caller skipped after reset failure\n")
        write(raw / "aider_stderr.log", "caller skipped after reset failure\n")
    status_result = run(["git", "status", "--porcelain=v1"])
    write(raw / "git_status.log", status_result.stdout + status_result.stderr)
    for name, args in (("unstaged", ["git", "diff", "--", REL]), ("cached", ["git", "diff", "--cached", "--", REL]), ("head", ["git", "diff", "HEAD", "--", REL])):
        r = run(args)
        write(raw / ("git_diff_%s.patch" % name), r.stdout)
    for name, args in (("unstaged", ["git", "diff", "--name-only"]), ("cached", ["git", "diff", "--cached", "--name-only"]), ("head", ["git", "diff", "HEAD", "--name-only"])):
        r = run(args)
        write(raw / ("git_names_%s.log" % name), r.stdout + r.stderr)
    all_text = status_result.stdout + stdout + (raw / "aider_stderr.log").read_text()
    hits = FORBIDDEN.findall(all_text)
    paths = [line[3:] for line in status_result.stdout.splitlines() if len(line) >= 4]
    forbidden = [p for p in paths if p not in (REL, ".aider.tags.cache.v4/") and not p.startswith("sidecar/experiments/aider_classroom_bite_research_028/")]
    write(raw / "forbidden_path_scan.log", "placeholder_hits=%r\nforbidden_paths=%r\n" % (hits, forbidden))
    oracle = run(["python3", str(ROOT / "proof" / "oracle.py"), str(TARGET)], env=env)
    regression = run(["python3", "-m", "pytest", "-q", str(ROOT / "fixture" / "test_string_surface.py")], env=env)
    write(raw / "final_proof.log", oracle.stdout + oracle.stderr)
    write(raw / "regression_proof.log", regression.stdout + regression.stderr)
    head_diff = run(["git", "diff", "HEAD", "--", REL]).stdout
    engineering = status == "VALID_COMPLETE" and baseline.returncode == 0 and oracle.returncode == 0 and regression.returncode == 0 and bool(head_diff)
    aider_success = engineering and code == 0 and not forbidden and not hits
    write(raw / "timing.json", json.dumps({"elapsed_seconds": elapsed, "exit_code": code, "model": MODEL, "edit_format": fmt, "aider_version": "0.86.2", "warm_policy": "exact model before every attempt", "timeout_seconds": 360, "scored": scored}, indent=2) + "\n")
    receipt = "format=%s\nscored=%s\nrepetition=%s\nstatus=%s\nengineering_success=%s\naider_success=%s\nplaceholder_hits=%r\nforbidden_paths=%r\nelapsed_seconds=%.3f\n" % (fmt, scored, n, status, engineering, aider_success, hits, forbidden, elapsed)
    write(dest / "RECEIPT.md", receipt)
    write(dest / "AFTER_ACTION.md", receipt + "target=%s\nreset_before=recorded\nreset_after=recorded\n" % REL)
    cleanup = run(["git", "restore", "--source=" + BASELINE, "--staged", "--worktree", "--", REL])
    run(["git", "reset", "--", "path/to"])
    placeholder_tree = REPO / "path" / "to"
    if placeholder_tree.exists():
        shutil.rmtree(REPO / "path")
    stray = REPO / "aider_classroom_bite_research_022"
    run(["git", "reset", "--", "aider_classroom_bite_research_022"])
    if stray.exists():
        shutil.rmtree(stray)
    placeholder_path = REPO / PLACEHOLDER
    if placeholder_path.exists():
        placeholder_path.unlink()
    cache = REPO / ".aider.tags.cache.v4"
    if cache.exists():
        shutil.rmtree(cache)
    write(raw / "cleanup.log", cleanup.stdout + cleanup.stderr)
    final = run(["git", "status", "--porcelain=v1"])
    write(raw / "post_cleanup_status.log", final.stdout + final.stderr)


def main():
    if len(sys.argv) > 1 and sys.argv[1].startswith("verification"):
        verification_number = int(sys.argv[1].replace("verification", "") or "1")
        for fmt in ("whole", "diff"):
            attempt(fmt, verification_number, False)
        return
    if len(sys.argv) > 1 and sys.argv[1] == "scored":
        for fmt in ("whole", "diff"):
            for n in (1, 2, 3):
                attempt(fmt, n, True)
        return
    if len(sys.argv) > 1 and sys.argv[1].startswith("diff"):
        attempt("diff", int(sys.argv[1].replace("diff", "")), True)
        return
    for fmt in ("whole", "diff"):
        attempt(fmt, 1, False)
    for fmt in ("whole", "diff"):
        for n in (1, 2, 3):
            attempt(fmt, n, True)


if __name__ == "__main__":
    main()

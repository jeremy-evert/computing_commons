"""Run the repaired Shot 1 ladder with immutable per-attempt evidence."""
import hashlib
import json
import os
import shutil
import subprocess
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[2]
SOURCE = ROOT / "fixture" / "budget.py"
FIXTURE = ROOT / "fixture"
PROOF = ROOT / "proof"
BASELINE = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()
MODEL = "ollama_chat/qwen2.5-coder-3b-cpu:latest"

TASKS = {
    "micro": ("cents_to_label", "micro_oracle.py", "Add only cents_to_label(cents), returning a dollar string with exactly two decimals. Do not edit tests, proofs, or any other function."),
    "small": ("remaining_cents", "small_oracle.py", "Add only remaining_cents(limit_cents, spent_cents), returning the non-negative remainder. Do not edit tests, proofs, or any other function."),
    "medium": ("remaining_cents and by_category", "medium_oracle.py", "Add remaining_cents(limit_cents, spent_cents) and by_category(expenses_by_category), returning non-negative remainder and per-category sums. Do not edit tests, proofs, or any other function."),
    "large": ("budget_report", "large_oracle.py", "Add budget_report(limit_cents, expenses_by_category), returning limit_cents, spent_cents, remaining_cents, by_category, and over_budget. Use small readable helpers if needed. Do not edit tests or proofs."),
}


def run(cmd, cwd=REPO, env=None, timeout=180):
    return subprocess.run(cmd, cwd=cwd, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)


def warm():
    # A tiny exact-model request establishes the warm state; its time is not scored.
    return run(["ollama", "run", "qwen2.5-coder-3b-cpu:latest", "Reply WARM only."], timeout=180)


def main():
    for rung, (behavior, oracle_name, task) in TASKS.items():
        for number in range(1, 4):
            attempt = ROOT / "shot_01" / rung / ("valid_%03d" % number)
            raw = attempt / "raw"
            if attempt.exists():
                raise SystemExit("refusing to overwrite %s" % attempt)
            raw.mkdir(parents=True)
            run(["git", "restore", "--source=%s" % BASELINE, "--", str(SOURCE.relative_to(REPO))])
            regression = run(["python3", "-m", "pytest", "-q", str(FIXTURE / "test_budget.py")])
            (raw / "baseline_regression.log").write_text(regression.stdout + regression.stderr)
            oracle_hash = hashlib.sha256((PROOF / oracle_name).read_bytes()).hexdigest()
            oracle_before = run(["python3", str(PROOF / oracle_name)], env=dict(os.environ, PYTHONPATH=str(FIXTURE)))
            (raw / "baseline_oracle.log").write_text(oracle_before.stdout + oracle_before.stderr)
            prompt = "Implement only the following behavior in fixture/budget.py: %s\n\n%s\n" % (behavior, task)
            (attempt / "AIDER_PROMPT.md").write_text(prompt)
            (attempt / "PREDICTION.md").write_text("Expected one production file, behavior: %s; no test/proof edits; oracle should pass after implementation.\n" % behavior)
            (attempt / "RUN_PLAN.md").write_text("Mission 021 Shot 1; rung=%s; repetition=%d; baseline=%s; model=%s; warm before timing.\n" % (rung, number, BASELINE, MODEL))
            warm()
            start = time.time()
            result = run(["aider", "--model", MODEL, "--edit-format", "whole", "--no-auto-commits", "--no-gitignore", "--yes-always", "--message-file", str(attempt / "AIDER_PROMPT.md"), str(SOURCE.relative_to(REPO))], timeout=240)
            elapsed = time.time() - start
            (raw / "aider_stdout.log").write_text(result.stdout)
            (raw / "aider_stderr.log").write_text(result.stderr)
            (raw / "timing.json").write_text(json.dumps({"start_epoch": start, "elapsed_seconds": elapsed, "exit_code": result.returncode, "warm_policy": "exact-model request before each attempt"}, indent=2) + "\n")
            diff = run(["git", "diff", "--", str(SOURCE.relative_to(REPO))])
            (raw / "git_diff.patch").write_text(diff.stdout)
            oracle_after = run(["python3", str(PROOF / oracle_name)], env=dict(os.environ, PYTHONPATH=str(FIXTURE)))
            (raw / "final_proof.log").write_text(oracle_after.stdout + oracle_after.stderr)
            regression_after = run(["python3", "-m", "pytest", "-q", str(FIXTURE / "test_budget.py")])
            (raw / "regression_proof.log").write_text(regression_after.stdout + regression_after.stderr)
            touched = run(["git", "status", "--short"])
            (raw / "status.log").write_text(touched.stdout + touched.stderr)
            (attempt / "RECEIPT.md").write_text("rung=%s\nrepetition=%d\nbaseline=%s\noracle=%s\noracle_sha256=%s\naider_exit=%d\nelapsed_seconds=%.3f\nfinal_oracle_exit=%d\nregression_exit=%d\n" % (rung, number, BASELINE, oracle_name, oracle_hash, result.returncode, elapsed, oracle_after.returncode, regression_after.returncode))
            (attempt / "AFTER_ACTION.md").write_text("Engineering success: %s\nAider success: %s\nClassroom-fit machine-side provisional: inspect diff, latency, prediction mismatch, and proof burden.\nFiles intended: fixture/budget.py only.\n" % (oracle_after.returncode == 0, result.returncode == 0 and oracle_after.returncode == 0 and regression_after.returncode == 0))
            run(["git", "restore", "--source=%s" % BASELINE, "--", str(SOURCE.relative_to(REPO))])


if __name__ == "__main__":
    main()

# Morgan Student-Surrogate Validation Plan

Status: **READY FOR TESTING**

Morgan is the first controlled machine for testing the public Computing Commons NRP path before we assume it works smoothly for a room full of students.

The purpose is not to turn Morgan into a special instructor snowflake. The purpose is to make Morgan behave as much like a student workstation as practical and discover friction early.

## What Morgan can prove

Morgan can validate the **client experience**:

```text
Computing Commons instructions
  -> WSL/Ubuntu shell
  -> kubectl
  -> kubelogin
  -> kubeconfig placement
  -> browser/CILogon/GitHub authentication
  -> explicit namespace use
  -> first finite Job
  -> logs
  -> cleanup
  -> evidence receipt
```

Morgan using Jeremy's personal NRP identity does **not** prove an ordinary student has identical RBAC permissions because Jeremy is a namespace administrator.

Therefore we need two complementary proofs:

```text
Morgan  -> proves workstation/tooling/instruction path
Student One -> proves ordinary student identity/permission path
```

Do not confuse one for the other.

## Target environment

Preferred Morgan test lane:

```text
Windows host
  -> WSL
      -> Ubuntu
          -> Computing Commons
          -> kubectl
          -> kubelogin
          -> NRP
```

This is useful because it resembles a realistic student Windows setup while still giving us a normal Linux shell for the public helper scripts.

## Gate 0 — Start from the correct workbench

Before running Commons commands:

```bash
cd ~/git/computing_commons
pwd
git rev-parse --show-toplevel
git status --short
git pull --ff-only
```

Expected repository root:

```text
.../computing_commons
```

Do not begin by copying commands from a neighboring repository.

## Gate 1 — Read the student instructions as a student

Open:

```text
national_research_platform/README.md
national_research_platform/getting_started.md
```

Do not skip directly to a known instructor shortcut.

While testing, keep a friction log:

```text
step
what the instruction said
what Morgan actually did
unexpected question/error
what a student would likely misunderstand
```

The curriculum is part of the product under test.

## Gate 2 — Local tools

From WSL/Ubuntu:

```bash
command -v kubectl || true
command -v kubectl-oidc_login || true
kubectl version --client 2>/dev/null || true
```

If a tool is missing, follow the **current official NRP Getting Access documentation** rather than an old copied installer:

<https://nrp.ai/documentation/userdocs/start/getting-started/>

Record which installation step was needed. That becomes curriculum data.

## Gate 3 — Kubeconfig location

NRP currently expects the normal Linux/WSL location:

```text
~/.kube/config
```

Verify existence without printing its contents:

```bash
test -f ~/.kube/config && echo "kubeconfig present" || echo "kubeconfig missing"
```

Do **not** `cat` the kubeconfig into a transcript, chat, or public artifact.

## Gate 4 — Context

Run:

```bash
kubectl config get-contexts
kubectl config current-context
```

The current NRP docs use:

```text
nautilus
```

If required:

```bash
kubectl config use-context nautilus
```

Do not assume the namespace yet.

## Gate 5 — Authenticate using the same public path

Use an ordinary authenticated `kubectl` request and let kubelogin trigger the browser/CILogon flow.

For the current SWOSU path, use GitHub through CILogon.

Important: Morgan should test the **same CILogon/GitHub mechanism students are being told to use**, even though Jeremy's resulting permissions are stronger.

## Gate 6 — Explicit course namespace

Current CS2 target:

```text
swosu-jevert-cs2-f26
```

Set it for convenience:

```bash
kubectl config set-context nautilus --namespace=swosu-jevert-cs2-f26
```

But still use `-n swosu-jevert-cs2-f26` in the actual validation commands so the evidence is unambiguous.

## Gate 7 — Run the Commons read-only preflight

From the Computing Commons repository root:

```bash
bash national_research_platform/scripts/student_preflight.sh \
  swosu-jevert-cs2-f26
```

Expected broad result:

```text
PREFLIGHT PASS
```

Inspect individual checks rather than accepting the final line blindly.

Because Jeremy is an admin, a permission result of `yes` proves the namespace works for Jeremy; it does not prove the student role.

## Gate 8 — Create the first Job exactly from public curriculum

Copy the template:

```bash
cp national_research_platform/templates/first_job.template.yaml \
  /tmp/morgan-first-nrp-job.yaml
```

Edit only the placeholders:

```text
REPLACE_WITH_GITHUB_USERNAME -> a DNS-safe Jeremy/Morgan test identifier
REPLACE_WITH_COURSE_NAMESPACE -> swosu-jevert-cs2-f26
```

Read the final manifest before applying it.

Confirm:

```text
course namespace is explicit
CPU-only
10m request / 50m limit
16Mi request / 32Mi limit
finite active deadline
no secret values
no GPU request
```

Then follow Lesson 2 exactly.

Do not use the private `nrp_k8s_launcher` as the student-facing path for this test. Morgan is validating what a student can learn from the public Commons.

## Gate 9 — Verify result

Collect:

```text
Job name
Job completion
Pod name/status
logs
container hostname
kernel line
```

The key learning proof is not merely "kubectl apply worked."

We want to know whether the public lesson made it obvious how to prove the workload actually ran.

## Gate 10 — Cleanup

Delete only Morgan's exact test Job:

```bash
kubectl delete job MORGAN_TEST_JOB -n swosu-jevert-cs2-f26
```

Verify the Job is gone and no Pod remains with its `job-name` label.

## Gate 11 — Write the student-style receipt

Use:

```text
national_research_platform/templates/evidence_receipt.md
```

Fill it out as though Morgan were a student.

This tests whether the receipt asks for the right evidence and whether any requested field feels pointless or unclear.

## Gate 12 — Test one intentional failure

After the clean successful path works, create **one safe diagnostic failure** without mutating cluster policy.

Recommended option:

```bash
kubectl get pods -n definitely-not-a-real-course-namespace
```

Observe the error and use Lesson 3 to classify it.

Do not intentionally create runaway Jobs, oversized resource requests, invalid secrets, or cluster-wide mutations just to manufacture drama.

## Acceptance criteria

Morgan validation is green when:

1. A fresh reader can find the NRP landing page from Computing Commons.
2. WSL/Ubuntu can install/find `kubectl` and `kubelogin` using current NRP instructions.
3. CILogon/GitHub authentication works.
4. `nautilus` context is visible.
5. `swosu-jevert-cs2-f26` is explicitly readable.
6. The public read-only preflight behaves sensibly.
7. The public first-Job template runs as a finite CPU-only workload.
8. Logs are recovered.
9. Cleanup is independently verified.
10. The evidence receipt can be completed without exposing a secret.
11. Any friction discovered is turned into a curriculum fix rather than tribal instructor knowledge.

## Student-One comparison

After Morgan passes, compare Student One's experience against the same gates.

The most valuable differences will likely be around:

```text
namespace membership
RBAC permissions
first-time CILogon behavior
local OS/tool installation
GitHub identity mismatch
browser/kubelogin behavior
```

If Morgan passes and Student One fails, that difference is high-value evidence because it narrows the problem to student identity/permissions or student-machine variation rather than the overall curriculum path.

## Durable test note

After the first full Morgan pass, preserve a short report under an instructor/reports or sidecar/report location rather than relying on terminal scrollback.

Failures are data. Curriculum improvements are what we decide to do with them.

# Getting Started with the National Research Platform

Welcome to the **National Research Platform (NRP)**.

You do not need to know Kubernetes before beginning. Your first goal is much smaller:

> **Can I prove that I am me, enter the correct course workspace, run one tiny program somewhere other than my own computer, see the result, and clean up after myself?**

If you can do that, you have already crossed an important line from "code that runs on my laptop" toward "software that can become a portable remote workload."

## 1. What is the NRP?

Most beginning programs follow this path:

```text
source code -> compiler/interpreter -> your computer -> result
```

Modern computing often adds more layers:

```text
source code
   -> Git / GitHub
   -> containerized environment
   -> remote cluster
   -> scheduler
   -> available CPU / memory / GPU
   -> result and evidence
```

The NRP gives researchers and students access to the Nautilus Kubernetes cluster and related research-computing services. Your laptop can become the steering wheel while another machine supplies the engine.

This does **not** mean the class is becoming a Kubernetes certification course. Kubernetes is a useful vehicle for learning portability, reproducibility, identity, authorization, containers, resource management, automation, observability, failure, and scale.

## 2. Four words you need today

### Cluster

The large collection of computing resources participating in Nautilus.

### Namespace

An isolated Kubernetes workspace. A course namespace is where your class is authorized to run its work.

Your instructor will tell you the exact namespace to use. For Fall 2026 Computer Science II, it is:

```text
swosu-jevert-cs2-f26
```

### Pod

A Kubernetes unit that runs one or more containers. For the first lesson, it is enough to think:

```text
Pod -> container -> program
```

### Job

A Kubernetes object for **finite work**. A Job should run, finish, leave evidence, and then be cleaned up.

## 3. Log into NRP

Go to <https://nrp.ai/> and choose **Log In**.

You will be sent to CILogon. If SWOSU is not available as an identity provider, use **GitHub** for this course. Use the same GitHub identity associated with the email you gave your instructor.

On your first successful login, complete any required NRP account/AUP steps.

Then open the NRP Namespaces Manager:

<https://nrp.ai/namespaces>

Find the course namespace your instructor gave you.

For CS2:

```text
swosu-jevert-cs2-f26
```

### Checkpoint A

Before installing anything, you should be able to say:

```text
[ ] I authenticated through CILogon using GitHub.
[ ] NRP recognizes my account.
[ ] I can see the course namespace.
```

If the namespace is missing, stop there and tell your instructor. Do not invent a workaround.

## 4. Install the command-line tools

You need two pieces:

```text
kubectl       -> talks to Kubernetes
kubelogin     -> handles your CILogon/OIDC authentication
```

Use the current NRP Getting Access page for the platform-specific installation instructions:

<https://nrp.ai/documentation/userdocs/start/getting-started/>

The NRP documentation currently requires the `kubelogin` plugin for its kubeconfig to work.

## 5. Install your NRP kubeconfig

Follow the current NRP instructions to download the Nautilus Kubernetes config and place it in the standard location.

Typical locations are:

```text
Linux / macOS / WSL: ~/.kube/config
Windows:             %USERPROFILE%\.kube\config
```

Your kubeconfig is part of your authentication setup.

**Do not commit it to GitHub. Do not paste it into Canvas, chat, an AI prompt, or a public screenshot.**

## 6. Verify the Nautilus context

Run:

```bash
kubectl config get-contexts
```

You should see the Nautilus context. The NRP documentation currently uses the context name:

```text
nautilus
```

If necessary:

```bash
kubectl config use-context nautilus
```

Set the course namespace explicitly:

```bash
kubectl config set-context nautilus --namespace=swosu-jevert-cs2-f26
```

Then inspect again:

```bash
kubectl config get-contexts
```

For other courses, replace `swosu-jevert-cs2-f26` with the exact namespace your instructor gives you.

## 7. Prove read access before creating anything

Run:

```bash
kubectl get pods -n swosu-jevert-cs2-f26
```

Your browser may open for CILogon authentication. Use GitHub again if prompted.

If you see a message like:

```text
No resources found
```

that is good news. It means Kubernetes accepted your identity and you can inspect that namespace; there just are not any Pods to list.

Now ask Kubernetes what you are allowed to do:

```bash
kubectl auth can-i get pods -n swosu-jevert-cs2-f26
kubectl auth can-i create jobs -n swosu-jevert-cs2-f26
```

For the normal student path, both should return:

```text
yes
```

If either returns `no`, preserve the command and result and tell your instructor. Permissions are part of the system design, not a puzzle to defeat.

## 8. Optional read-only preflight helper

From this repository you may run:

```bash
bash national_research_platform/scripts/student_preflight.sh swosu-jevert-cs2-f26
```

The script does not create or delete anything. It checks the local tools, current context, namespace visibility, and basic permissions.

Read the script before running it if you are curious. That habit is encouraged.

## 9. Run your first remote Job

Continue to:

[Lesson 2 — Your First Remote Job](curriculum/02_first_remote_job.md)

The first Job is intentionally tiny, CPU-only, and boring. A boring success is ideal when learning a new system.

The pattern is:

```text
CREATE -> RUN -> OBSERVE -> VERIFY -> CLEAN UP -> VERIFY AGAIN
```

That pattern matters more than the hello-world program itself.

## 10. When access was just changed

NRP authentication can be cached. If your instructor has just added you to a namespace and your local credentials do not see the change yet, the current NRP documentation recommends:

```bash
kubectl oidc-login clean
```

Then retry a normal `kubectl` command and authenticate again.

## 11. What not to publish

Do not put these into GitHub, Canvas, chat, screenshots, or assignments:

```text
passwords
API tokens
private keys
full kubeconfigs
secret environment files
grades
student records
protected personal data
```

Good evidence includes commands, namespace names, Job names, status, logs that contain no secrets, timing, resource requests, Git commits, explanations, and cleanup proof.

## 12. If something fails

A useful failure report says:

1. What were you trying to do?
2. What exact command did you run?
3. What did you expect?
4. What actually happened?
5. What error or status did the computer give you?

Do **not** send your token or kubeconfig with the failure report.

Failures are data. The goal is to collect enough evidence to decide what to do with them.

## 13. Why this belongs in your computer science journey

Today you are learning this chain:

```text
identity
  -> authorization
  -> namespace
  -> Job
  -> Pod
  -> container
  -> output
  -> evidence
  -> cleanup
```

Later this can grow into:

```text
source code
  -> Git
  -> container
  -> Kubernetes
  -> CPU / memory / GPU
  -> experiment
  -> evidence
  -> reproducible result
```

The interesting lesson is not merely that NRP has large computers.

The deeper lesson is:

> **Software can leave your laptop and become a workload that another computing environment can understand, schedule, run, observe, and verify.**

That idea connects directly to containers, distributed systems, software engineering, computer architecture, cloud computing, research computing, and eventually AI/ML systems.

## Next

Start the curriculum here:

[NRP Curriculum Map](curriculum/README.md)

Current official references:

- <https://nrp.ai/documentation/userdocs/start/getting-started/>
- <https://nrp.ai/documentation/userdocs/start/using-nautilus/>
- <https://nrp.ai/documentation/userdocs/tutorial/basic/>
- <https://nrp.ai/documentation/userdocs/start/policies/>

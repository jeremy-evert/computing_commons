# Lesson 1 — Identity, Access, and the Course Namespace

## Why this matters

Before a remote system will run your code, it has to answer two different questions:

1. **Who are you?**
2. **What are you allowed to do?**

Those are not the same question.

This lesson gives you a mental model for authentication, authorization, and namespaces before you create any remote workload.

## Learning outcomes

By the end of this lesson, you should be able to:

- authenticate to NRP through CILogon using the identity path assigned by your instructor;
- find your course namespace;
- explain the difference between identity and permission;
- verify that `kubectl` is talking to Nautilus;
- verify read access to the course namespace;
- ask Kubernetes whether you may create Jobs;
- report an access failure without exposing credentials.

## Before you begin

You need:

- a GitHub account using the identity/email your instructor expects;
- membership in the appropriate NRP course namespace;
- `kubectl` installed;
- the NRP-required `kubelogin` plugin installed;
- the NRP kubeconfig in the standard location.

Use the current NRP setup instructions when installing these pieces:

<https://nrp.ai/documentation/userdocs/start/getting-started/>

For Fall 2026 CS2, the course namespace is:

```text
swosu-jevert-cs2-f26
```

If you are taking a different class, replace that example with the namespace your instructor gives you.

## Mental model

Think of the path this way:

```text
GitHub account
    ↓
CILogon authentication
    ↓
NRP account
    ↓
course/project membership
    ↓
Kubernetes authorization
    ↓
course namespace
```

Authentication answers:

> Who are you?

Authorization answers:

> What may that identity do here?

A namespace answers:

> Which isolated workspace are we talking about?

## Step 1 — Prove the NRP account path

Go to:

<https://nrp.ai/>

Choose **Log In**.

If your institution is not available through CILogon, your instructor may direct you to use GitHub. NRP currently documents GitHub as one of the fallback identity providers when the institutional choices do not work.

After login, open:

<https://nrp.ai/namespaces>

Find your course namespace.

For CS2:

```text
swosu-jevert-cs2-f26
```

### Checkpoint

Record only this much in your notes:

```text
NRP login: success / not yet
Course namespace visible: yes / no
```

Do not record passwords or tokens.

## Step 2 — Inspect your local Kubernetes context

Run:

```bash
kubectl config get-contexts
```

NRP's current documentation uses the context name:

```text
nautilus
```

If it exists but is not current:

```bash
kubectl config use-context nautilus
```

Now set the intended namespace:

```bash
kubectl config set-context nautilus --namespace=swosu-jevert-cs2-f26
```

Then inspect again:

```bash
kubectl config get-contexts
```

The point is not merely to save typing. You are making the workspace choice visible and inspectable.

## Step 3 — Verify read access

Run:

```bash
kubectl get pods -n swosu-jevert-cs2-f26
```

You may be sent through browser authentication.

A result such as:

```text
No resources found
```

is a **successful access result**. It means there are no Pods to list, not that the command failed.

## Step 4 — Ask what your identity may do

Run:

```bash
kubectl auth can-i get pods -n swosu-jevert-cs2-f26
kubectl auth can-i create jobs -n swosu-jevert-cs2-f26
```

For the normal student path, you want:

```text
yes
yes
```

If you receive `no`, stop and preserve the result.

Do not try to alter RBAC, create another identity, borrow another person's kubeconfig, or use an instructor credential.

A permission failure is useful evidence.

## Step 5 — Run the Commons read-only preflight

From a checkout of Computing Commons:

```bash
bash national_research_platform/scripts/student_preflight.sh swosu-jevert-cs2-f26
```

Read the output.

The script is intentionally boring. It should tell you whether the expected local tools exist, what context is current, whether the namespace is visible, and whether your identity has the basic permissions needed for the first Job.

## If you were just added to the namespace

NRP access tokens may cache old membership for a short time.

If your instructor just added you and your local commands do not see the new namespace yet, NRP currently recommends:

```bash
kubectl oidc-login clean
```

Then retry a normal `kubectl` command and authenticate again.

## Failure as data

If this lesson fails, capture:

```text
Command:
Expected:
Actual result:
Exact error/status:
Course namespace:
```

Useful commands include:

```bash
kubectl config get-contexts
kubectl auth can-i get pods -n swosu-jevert-cs2-f26
kubectl auth can-i create jobs -n swosu-jevert-cs2-f26
```

Do not paste your kubeconfig, token cache, private key, or password into the report.

## Evidence receipt

Create a short receipt containing:

```text
Lesson: NRP 01 Identity, Access, Namespace
Identity path used: CILogon -> GitHub (or instructor-approved alternative)
Course namespace: ______________________
Nautilus context visible: yes/no
Can get pods: yes/no
Can create jobs: yes/no
One thing I learned about authentication vs authorization:
```

## Reflection

Answer these in your own words:

1. Why can a person successfully authenticate but still be denied permission to create a Job?
2. Why is an explicit course namespace safer than assuming the current/default namespace is correct?

## Next

Continue to:

[Lesson 2 — Your First Remote Job](02_first_remote_job.md)

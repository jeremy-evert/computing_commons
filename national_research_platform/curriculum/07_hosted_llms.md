# Lesson 7 — Hosted LLMs as a Remote Service

## Why this matters

Running a Kubernetes Job and calling a hosted language model are both forms of remote computing, but they are **not the same thing**.

A Kubernetes workload asks the cluster to run your containerized work.

A hosted LLM API asks an already-running remote service to process a request for you.

Learning that boundary helps you reason about credentials, reproducibility, cost/capacity, privacy, and where computation actually happens.

## Learning outcomes

By the end of this lesson, you should be able to:

- explain the difference between Kubernetes identity and hosted-service API identity;
- use a personal NRP LLM token without committing or displaying it;
- discover the currently available model IDs rather than hard-coding assumptions;
- make one small programmatic request to an NRP-hosted model;
- preserve a token-free evidence receipt;
- explain what a hosted-model result does and does not make reproducible.

## Before you begin

Your instructor must tell you that hosted LLM access is enabled for your NRP group/course.

You need your **own personal token** from the NRP LLM access flow.

Do not use:

- another student's token;
- an instructor token;
- a shared class token;
- a Kubernetes ServiceAccount credential as an LLM API key.

Current NRP documentation:

<https://nrp.ai/documentation/userdocs/ai/llm-managed/>

<https://nrp.ai/documentation/userdocs/ai/llm-managed/api-access/>

## Mental model

Kubernetes path:

```text
personal CILogon identity
  -> Kubernetes authorization
  -> namespace
  -> Job/Pod/container
```

Hosted LLM path:

```text
personal NRP LLM token
  -> NRP LLM gateway
  -> already-hosted model
  -> response
```

The token boundary is separate from Kubernetes namespace credentials.

## Step 1 — Store the token outside source code

Use an environment variable or another instructor-approved protected local secret store.

For a temporary shell session:

```bash
export NRP_LLM_TOKEN='YOUR_TOKEN_HERE'
```

Do not put the real token in a Markdown file, Python file, Git commit, screenshot, or assignment.

When showing commands in a report, use a placeholder such as:

```text
$NRP_LLM_TOKEN
```

not the value.

## Step 2 — Discover active model IDs

NRP's hosted catalog changes over time. Do not assume a model that existed last month still exists today.

List the models currently available to your token:

```bash
curl -sS \
  -H "Authorization: Bearer $NRP_LLM_TOKEN" \
  https://ellm.nrp-nautilus.io/v1/models
```

The current NRP API endpoint is OpenAI-compatible:

```text
https://ellm.nrp-nautilus.io/v1
```

Record the model ID you choose. Do not record the token.

## Step 3 — Make one tiny request

Choose an active model from the returned list.

Use a deliberately small prompt such as:

```text
Reply with OK only.
```

If you use the OpenAI Python client, the conceptual pattern is:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["NRP_LLM_TOKEN"],
    base_url="https://ellm.nrp-nautilus.io/v1",
)

response = client.chat.completions.create(
    model="REPLACE_WITH_ACTIVE_MODEL_ID",
    messages=[{"role": "user", "content": "Reply with OK only."}],
    temperature=0,
)

print(response.choices[0].message.content)
```

The goal is not to build an AI application yet. It is to prove the service boundary cleanly.

## Step 4 — Compare this with a Kubernetes Job

Ask yourself:

```text
Who selected the physical machine?
Did I provide the container image?
Did I request CPU/memory directly?
Did I start the model server?
Which credential authorized the request?
What evidence can I preserve without leaking the credential?
```

For a hosted API, much of the infrastructure is hidden behind the service endpoint.

That convenience is useful, but it also means some details are outside your direct control.

## Step 5 — Think about reproducibility

A hosted model request can record:

```text
model ID
prompt
parameters
client/code version
response
request time
```

But even with all of that, you should ask whether the remote service/model deployment could change.

A service response is evidence of what happened during that request. It is not automatically proof that the same response will always occur forever.

## CS2 connection

A hosted model is an example of a software dependency reached through an API.

That connects directly to CS2 ideas:

- interfaces;
- input/output contracts;
- error handling;
- serialization/JSON;
- abstraction;
- dependency boundaries;
- testing;
- nondeterminism;
- responsible use of external services.

The model may be enormous. Your program's responsibility is still to call the interface correctly, validate the response appropriately, and handle failure.

## Failure as data

Useful failure categories include:

- missing/invalid token;
- permission/group does not have LLM access;
- invalid model ID;
- rate/concurrency limit;
- malformed request;
- client library mismatch;
- remote service unavailable;
- response content does not satisfy your program's expectations.

Preserve the HTTP/status/error message. Do not preserve the token.

## Evidence receipt

Record:

```text
Lesson: NRP 07 Hosted LLMs
NRP group/course with LLM access:
Endpoint used: https://ellm.nrp-nautilus.io/v1
Model ID discovered at runtime:
Prompt purpose:
Response summary:
Token exposed in receipt: NO
One way this differs from a Kubernetes Job:
One reproducibility limitation:
```

## Reflection

1. Why should each student use a personal service token instead of a shared class token?
2. What does an API hide from you compared with running your own containerized workload?
3. Why should model IDs be discovered/verified rather than assumed forever?
4. What independent test would you add before trusting a model response inside a real program?

## Next

Continue to:

[Lesson 8 — GPUs and Accelerators](08_gpu_accelerators.md)

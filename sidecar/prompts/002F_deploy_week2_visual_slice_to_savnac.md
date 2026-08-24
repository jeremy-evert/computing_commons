# 002F — Deploy accepted Computing Commons visual slice to Savnac

## Mission

Deploy the **accepted bounded Computing Commons visual slice** to the Savnac Canvas test range on Brandy so Jeremy can inspect the real Canvas rendering from home.

This is test-range deployment, not SWOSU production deployment.

## Preconditions

Before changing Savnac:

1. `computing_commons` source for the visual system, Success Foundations/Kickoff prototype, and Week 2 Local AI slice has passed the source-side visual/adversarial review required by Controller 002.
2. Repository state is committed/pushed and clean.
3. Read current Savnac operational truth in:
   - `jeremy-evert/Savnac/START_HERE.md`
   - `jeremy-evert/Savnac/requirements/REQ-001/readiness.md`
   - `jeremy-evert/Savnac/requirements/REQ-001/runbook.md`
4. Confirm the live `savnac` VM and Canvas instance before making content changes.

## Authorized live mutation

Authorized:

- create or reuse a clearly identifiable **Computing Commons prototype course** inside the Savnac Canvas instance;
- create/update only the pages/modules/0-point prototype assignments needed for the bounded visual slice;
- publish/unpublish prototype objects as necessary for owner inspection;
- use the protected Savnac administrator credential already documented on Brandy without printing, copying, or committing secret values;
- create a small deployment helper under `computing_commons` if a repeatable adapter is needed.

Not authorized:

- any write to `https://swosu.instructure.com/courses/24298` or another SWOSU Canvas course;
- Savnac VM rebuild/snapshot/rollback/destruction;
- network/firewall/sshd/libvirt changes unless a separate owner authorization is obtained;
- changes to unrelated Savnac courses;
- student/grade/identity data;
- broad home-course cleanup;
- Quick Tune execution in this pass.

## Prototype content scope

Load only enough to prove the visual/navigation system and Week 2 student path:

- Commons landing/Start Here as needed for coherent navigation;
- Success Foundations/Kickoff visual prototype as the low-risk design example;
- Week 2 Local AI landing and its required child pages/navigation/evidence entry points;
- Recitation/Get Help link or page needed to test the persistent recovery route;
- compact week/semester strip and consistent Home/Back/Next behavior;
- 0-point prototype assignment(s) only where needed to verify the intended completion posture.

Do not try to populate the entire future Commons in this pass.

## Deployment method

Prefer an existing safe/repeatable Canvas content path if one is present on Brandy/Savnac. If no adequate adapter exists, build the smallest bounded deployment adapter in `computing_commons` that can idempotently create/update this prototype slice.

Requirements for any adapter:

- target Savnac only;
- refuse a non-Savnac base URL unless explicitly overridden by a future owner-authorized mission;
- do not log secrets;
- make object identity stable enough for repeated tuning;
- produce a machine-readable deployment manifest with Canvas course/object IDs, titles, and source hashes;
- support read-back verification.

## Acceptance

Before reporting success:

- read back every created/updated Canvas object;
- confirm expected titles/order/links at the API/content level;
- confirm 0-point values where used;
- confirm no stale ZyBooks dependency was introduced;
- confirm external/internal links are syntactically valid where machine-checkable;
- preserve a deployment manifest in `computing_commons` under `sidecar/evidence/savnac/` or another clearly documented evidence path;
- write `sidecar/reports/luna/002F_savnac_week2_deployment_report.md`.

Do not claim aesthetic acceptance. That belongs to Jeremy's visual inspection.

Required verdict:

`SAVNAC VISUAL SLICE DEPLOYED FOR OWNER INSPECTION`

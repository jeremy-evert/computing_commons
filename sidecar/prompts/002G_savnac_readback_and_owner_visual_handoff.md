# 002G — Savnac read-back and owner visual handoff

## Mission

Verify the just-deployed Computing Commons prototype slice in Savnac and give Jeremy the shortest practical path to inspect it visually from Grace at home.

This pass **stops at the owner visual gate**. Do not start Quick Tune or synthetic-student review yet.

## Required inspection

1. Read back the Savnac prototype course and all in-scope objects created/updated by 002F.
2. Confirm the deployment manifest matches live Savnac object IDs/titles/order.
3. Confirm the intended landing path works structurally from Start Here/Kickoff into Week 2 and back through the common navigation pattern.
4. Confirm the Week 2 slice exposes Recitation/recovery where designed.
5. Re-check that no SWOSU Canvas course was touched.

## Grace/home access handoff

Read current Savnac runbook/live network truth and provide the **current verified or best-evidence access path** for Jeremy to inspect Savnac from Grace.

Do not assume an old Faith tunnel command is still correct without checking current Savnac address and Brandy forwarding policy.

The handoff must contain:

- exact Brandy host/destination currently expected;
- exact tunnel command if a tunnel is required;
- local browser URL Jeremy should open on Grace;
- Savnac prototype course title and direct course/page path when available;
- any login expectation, without displaying credentials;
- three to seven specific visual questions worth judging, focused on clarity, beauty, navigation, week strip, spacing, link affordance, and whether the page feels easy rather than busy.

If Brandy can verify the server side but Grace's client-side route cannot be proven remotely, say so clearly and give the narrowest command for Jeremy to try. A failed first attempt becomes evidence for the next repair, not permission to reconfigure infrastructure broadly.

## Deliverables

Write:

`sidecar/reports/luna/002G_savnac_owner_visual_handoff.md`

Also preserve any non-secret read-back evidence needed to reproduce the deployment state.

## Stop condition

Required final status:

`OWNER VISUAL INSPECTION REQUIRED`

Do not:

- run Savnac Quick Tune;
- launch synthetic students;
- dogfood the Windows Local AI flow on Jeremy's behalf;
- deploy to SWOSU Canvas course 24298;
- continue into broader Commons construction.

Jeremy's visual judgment is the next authority gate.

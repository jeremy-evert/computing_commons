# Owner direction — Savnac visual prototype, Quick Tune, and Grace dogfood

Date: 2026-08-23
Status: **OWNER DIRECTION / ACTIVE BUILD LOOP**

The Computing Commons visual campaign is pivoted from a repository-only/Maise pass to a **Brandy + Savnac prototype loop**.

## Current staffing

- Flo is occupied on April with the S'MOOR project.
- Luna should run this Computing Commons campaign from **Brandy**.

## Week 2 development loop

1. Build the Computing Commons visual/navigation system in Git.
2. Use Kickoff/Success Foundations as a low-risk proving ground if useful.
3. Make **Week 2 Local AI** the first real target.
4. Load the accepted bounded slice into **Savnac Canvas**.
5. Give Jeremy a simple browser path so he can visually inspect the real Canvas rendering from home on Grace.
6. Repair source/design issues in Git and redeploy to Savnac until Week 2 looks right.
7. Then run **Savnac Quick Tune** as a read-only audit lane.
8. Controlled synthetic-student testing may be used if it adds useful evidence.
9. Jeremy then dogfoods the student experience on **Grace**, including the Windows Local AI path where practical.
10. Repair findings and ship the corrected slice to Savnac again.

Only after the Commons is built and accepted does the complete course deploy to SWOSU Canvas course `24298`.

## Important boundaries

- Savnac is authorized as a mutable test range for this bounded prototype.
- `https://swosu.instructure.com/courses/24298` is **not** authorized for this early vertical-slice campaign.
- Do not interfere with Flo/S'MOOR work on April.
- Do not broadly clean the home course repos yet.
- Do not treat Quick Tune as a repair tool; it is audit-only.
- Visual inspection by Jeremy is a real owner gate before Quick Tune.

## Desired outcome of the next Luna mission

Luna should leave:

- accepted repository source for the visual system and Week 2 slice;
- a bounded Savnac Canvas prototype loaded from that source;
- a read-back/deployment manifest with Canvas object identifiers but no secrets;
- a simple Grace/home visual-inspection handoff;
- a clear stop at the owner visual gate.

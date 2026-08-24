# Savnac prototype loop for Computing Commons

## Purpose

Savnac is the rendering and behavior laboratory for Computing Commons before the complete course is deployed to SWOSU Canvas course 24298.

The loop exists because repository Markdown/HTML can look correct while Canvas rendering, links, module sequencing, completion rules, and student navigation still behave badly.

## Operating loop

For each meaningful Commons slice:

**SOURCE -> SAVNAC -> OWNER VISUAL -> REPAIR -> SAVNAC -> QUICK TUNE -> OWNER DOGFOOD -> REPAIR -> SAVNAC -> ACCEPT**

### Source

`jeremy-evert/computing_commons` remains curricular/composition truth. Canonical specialist repositories remain authoritative for their domains.

### Savnac

Deploy only the bounded slice currently under test. Savnac may be mutated as a test range when a mission explicitly authorizes it.

Do not change Savnac host/network/Canvas infrastructure merely to improve course content unless a separately scoped infrastructure defect is proven.

### Owner visual inspection

After a deploy/read-back, stop and give Jeremy a simple path to inspect the real Canvas rendering from Grace at home. The handoff must identify:

- the Savnac Canvas course;
- the exact page/module to open;
- the verified access/tunnel path available at that time;
- what changed since the previous build;
- the specific questions worth visually judging.

Visual taste is a real owner gate. Luna should not pretend to accept Jeremy's aesthetic preference on his behalf.

### Repair

Curricular and design defects go back into `computing_commons` first, then Savnac is reconciled to that source.

### Quick Tune

Once the slice is visually where the owner wants it, use `jeremy-evert/Savnac_quick_tune` as a **read-only audit lane**. Quick Tune does not repair Canvas or source content. It produces evidence/findings for the next bounded repair.

### Synthetic students

`jeremy-evert/synthetic_student_laboratory` may be used when a controlled synthetic-student path adds evidence about clarity, instruction-following, workload, or likely failure points. Synthetic outputs are test evidence only, not student data and not authoritative assessment.

### Owner dogfood

Jeremy then walks the student experience himself. For Week 2 this includes Grace as the Windows machine for the real Local AI path where practical.

Dogfood findings are repaired in Git, redeployed to Savnac, and checked again.

## Week 2 first target

Week 2 is the first full proving ground because it exercises:

- visual design;
- multi-page navigation;
- external/canonical source stitching;
- Local AI setup and evidence;
- Windows-specific instructions;
- 0-point/completion posture;
- recovery instructions;
- a real physical dogfood path on Grace.

Kickoff/Success Foundations may be used as the low-risk visual prototype, but Week 2 is the first slice that must survive the whole loop.

## Savnac operating source

Savnac operational truth lives in `jeremy-evert/Savnac`, especially:

- `START_HERE.md`
- `requirements/REQ-001/readiness.md`
- `requirements/REQ-001/runbook.md`

The current runbook records that Canvas runs inside the `savnac` VM on Brandy, that the admin credential file is protected on Brandy, and that browser access is tunneled through Brandy rather than exposing the guest publicly.

Never commit or print credentials into Commons reports.

## Separation from SWOSU Canvas

Success in Savnac means a slice is ready to keep building from. It does not authorize production/complete deployment to:

`https://swosu.instructure.com/courses/24298`

That course remains behind the complete Commons acceptance gate.

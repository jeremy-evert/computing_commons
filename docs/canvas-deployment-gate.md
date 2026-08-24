# Computing Commons Canvas deployment gate

## Two Canvas boundaries

Computing Commons now uses **two distinct Canvas surfaces for two distinct jobs**.

### 1. Savnac — design/test range

Savnac is the authorized laboratory for bounded prototype deployment **before** the full Commons is complete.

A vertical slice may be pushed to Savnac when its repository source is coherent enough to inspect in a real Canvas rendering. Savnac is where we test:

- visual design and Canvas HTML behavior;
- links and navigation;
- module/page ordering;
- mobile/narrow behavior where observable;
- 0-point/completion behavior;
- synthetic/student-path review;
- Quick Tune audits;
- owner dogfooding before a final SWOSU deployment.

Savnac is not curricular authority. Defects found there are repaired in repository truth first, then redeployed.

### 2. SWOSU Canvas course 24298 — established Commons target

Future complete deployment target:

`https://swosu.instructure.com/courses/24298`

This target remains gated until the **complete Computing Commons repository product** passes acceptance.

## Gate principle

**Build in Git -> prototype in Savnac -> inspect -> repair in Git -> re-prototype -> Quick Tune -> dogfood -> accept -> deploy complete Commons to SWOSU Canvas.**

Canvas must not become the accidental authoring source for material that is newer or clearer in the Commons/canonical repositories.

## Savnac prototype loop

For a bounded vertical slice such as Week 2:

1. build/reconcile the source in `computing_commons`;
2. adversarially review the source;
3. deploy the accepted slice to Savnac;
4. read back the rendered Canvas objects;
5. owner visually inspects from the house/Grace path;
6. repair source defects in Git and redeploy;
7. once the slice looks right, run `Savnac_quick_tune` as a read-only audit lane;
8. optionally use controlled synthetic-student testing where it adds evidence;
9. owner dogfoods the student path, including the real Windows/local-lab experience when applicable;
10. repair and redeploy until the slice is accepted.

A Savnac prototype verdict is **not** authorization to publish the same material to SWOSU Canvas course 24298.

## Required repository acceptance before complete SWOSU deployment

The Commons must have:

- a clear Start Here/front door;
- a Recitation/help model;
- a complete source registry;
- one shared Success Foundations path;
- one accepted Local AI Lab composition path tied to `local_ai_lab_setup` + `windows_classroom`;
- AI Fluency progressive Levels 1–5 tied to `ai_fluency`;
- Professional Minds tied to `professional_minds`;
- a usable Recitation Toolbox covering Containers, LaTeX/documentation, Work First, Linux/profiling, and Git/source management;
- a shared Farkle + Machine Learning finale map;
- Fall 2026 0-point/completion/bonus posture;
- explicit home-course wrapper boundaries;
- recovery paths for students who get stuck;
- an adversarial review verdict of `READY FOR COMPUTING COMMONS CANVAS DEPLOYMENT`.

## Complete SWOSU Canvas deployment expectations

When complete deployment is authorized, deploy the Commons as one coherent course rather than piecemeal experiments that leave contradictory student routes.

The Canvas structure should make these concepts obvious:

1. **Start Here**
2. **Recitation / Get Help**
3. **Success Foundations**
4. **Local AI Lab**
5. **AI Fluency** with cumulative levels
6. **Professional Minds**
7. **Recitation Toolbox**
8. **Farkle + Machine Learning**
9. **Reference / Recovery**

## Fall 2026 grading posture

Initial shared activities may:

- have due dates;
- be worth 0 points;
- record completion/evidence;
- support home-course bonus credit for exceptional work.

Do not assume Canvas can or should synchronize grades between the Commons and home courses until that behavior is deliberately tested.

## Deployment verification

For both Savnac prototypes and the eventual complete SWOSU deployment, perform a read-back from the student-facing Canvas surface and verify the applicable objects:

- module/page ordering;
- links;
- published/unpublished state;
- assignment point values;
- due-date behavior;
- completion requirements;
- cumulative level visibility;
- absence of stale Upswing/legacy front-door language where it conflicts with the Commons identity;
- no dead download or Local AI links;
- no hidden dependence on ZyBooks;
- no accidental enrollment/grade behavior.

## Owner dogfood gate

After Savnac technical verification, the owner may walk the bounded slice as though enrolled. After complete SWOSU deployment, repeat the walk for the complete Commons.

For the complete course, dogfooding should include:

- begin from the front door;
- follow the expected Level 1/shared runway;
- use the Local AI path;
- revisit earlier material;
- use at least one toolbox capability;
- inspect AI Fluency and Professional Minds navigation;
- test recovery from a deliberate wrong turn;
- inspect what a student sees in Grades/Assignments/Modules.

Observed defects should be repaired in repository truth first when they are curricular/content defects, then redeployed/reconciled to Canvas.

## Video gate

Instructional videos should be recorded from an accepted/dogfooded path, not from an unstable prototype. This reduces re-recording and prevents video instructions from freezing an obsolete navigation path.

## Cleanup handoff

Only after the Commons is established should later course cleanup use it as a reference. Flo can then remove/reconcile duplicated shared material from the individual classes while checking later weeks against the now-established Commons.

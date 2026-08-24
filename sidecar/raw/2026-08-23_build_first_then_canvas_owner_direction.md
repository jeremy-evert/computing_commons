# Owner direction — Build Computing Commons first, then deploy

Date: 2026-08-23
Status: **OWNER DIRECTION / BUILD FIRST**

The Computing Commons repository should be completed and accepted before the Commons is deployed wholesale into the SWOSU Canvas test course.

## Deployment target

Future Canvas target:

- `https://swosu.instructure.com/courses/24298`
- Role: Computing Commons test/prototype course first, then established shared Recitation surface after acceptance.

## Required order

1. Build `jeremy-evert/computing_commons` into a coherent, student-ready shared Recitation/clearinghouse.
2. Reconcile and stitch canonical shared sources rather than forking them.
3. Review the complete Commons as a repository product.
4. Only after repository acceptance, deploy the complete intended Commons structure to Canvas course `24298`.
5. Establish the Canvas course and verify navigation, completion behavior, links, due/0-point posture, and student-facing clarity.
6. Owner dogfoods the established Commons as a student/instructor.
7. Fix defects found by dogfooding.
8. Owner records instructional videos from the accepted path.
9. After Commons is stable, Flo may use it as the shared reference while cleaning later weeks and removing duplicated common material from individual course repositories/classes.

## Boundary

Do not use the current Canvas shell as the source from which the Commons is designed. Repository truth comes first. Canvas is the deployment target after acceptance.

Do not begin broad cleanup of CS1, CS2, DSCT, Computer Architecture, Software Engineering, or Machine Learning merely to make the Commons look clean. First establish the destination and its contracts. Cleanup comes later and can be verified against the established Commons.

## Owner validation sequence

The owner wants the ability to:

- dogfood the finished Commons;
- make videos from the accepted student path;
- then let Flo act as cleanup/reconciliation crew across the later course weeks.

The practical sequence is therefore:

**BUILD -> ACCEPT -> DEPLOY -> ESTABLISH -> DOGFOOD -> REPAIR -> RECORD -> CLEAN UP COURSES**

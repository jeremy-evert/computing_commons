# Prompt 003 — Savnac owner teacher access + credential rotation

## Mission

Make the Savnac Computing Commons prototype inspectable by Jeremy from his normal Savnac account by adding that existing user as a **Teacher** in prototype course **18**.

Because the previous deployment run reported that protected Savnac administrator credential material was accidentally exposed in diagnostic/tool output, **rotate the Savnac administrator credential before using the account for ordinary follow-on work**.

This is a bounded Savnac test-range operation. It does not authorize any SWOSU production Canvas mutation.

## Target

- Savnac Canvas prototype course: **18**
- Expected course title: `Computing Commons — Visual Prototype (Week 2)` or the exact current equivalent established by read-back.
- Desired owner result: Jeremy's existing Savnac user can open course 18 as **Teacher** from Grace through the normal Savnac tunnel.

## Required order

### 1. Reconcile current truth

Before mutation:

- read current `jeremy-evert/Savnac` `START_HERE.md` and the REQ-001 Canvas runbook;
- verify course 18 exists and is the intended Computing Commons prototype;
- verify course 17 is the known duplicate shell and **do not delete it**;
- inspect current enrollments on course 18 without exposing protected information.

If course 18 is not the intended prototype, stop with evidence rather than guessing.

### 2. Rotate compromised Savnac admin credential

Treat the previously exposed credential as compromised.

Use the existing protected credential only as needed to authenticate the rotation itself. Prefer a supported Canvas/local application method that changes the Savnac administrator login credential without changing VM/network/libvirt state.

Requirements:

- generate a new high-entropy credential locally;
- never print the old or new credential to terminal transcript, report, Git, or chat;
- atomically update the protected Brandy credential file documented by Savnac;
- preserve owner-only permissions (`0600` or stricter);
- verify the rotated credential works with a bounded non-secret Canvas read;
- record only success/failure and non-secret metadata in the report.

If safe rotation cannot be completed without an infrastructure/destructive step outside this mission, stop with a narrow HUMAN NUDGE before reusing the compromised credential for course administration.

### 3. Resolve Jeremy's existing Savnac user

Do **not** create a duplicate user if Jeremy already exists.

Resolve the correct existing user from current Savnac evidence. Preferred evidence is the user already enrolled as Teacher in one or more established Savnac computing courses (for example course 7 or the current CS1/CS2/DSCT/Architecture shells).

Use stable Canvas identifiers once resolved. Do not place private profile data in durable reports beyond what is necessary to identify the non-production user object.

If multiple plausible existing users cannot be distinguished safely, stop with HUMAN NUDGE rather than creating another account.

### 4. Add Teacher enrollment to course 18

Enroll the resolved existing Jeremy user in course 18 with the Canvas **Teacher** role.

Requirements:

- do not enroll real students;
- do not alter existing home-course enrollments;
- do not change grades, submissions, assignments, modules, pages, due dates, or course content;
- do not delete course 17;
- do not touch SWOSU Canvas `https://swosu.instructure.com/courses/24298`.

If Jeremy is already a Teacher in course 18, treat the operation as idempotently satisfied and do not add a duplicate enrollment.

### 5. Verify owner access

Read back course 18 and its enrollment state and prove:

- course 18 still matches the Computing Commons prototype;
- Jeremy's existing Savnac user has Teacher access;
- no student enrollment was added;
- no course content was modified by this mission;
- rotated administrator credential verification succeeded without secret disclosure.

Write the report:

`sidecar/reports/luna/003_savnac_owner_teacher_access_report.md`

Required verdict:

`SAVNAC OWNER TEACHER ACCESS READY`

or

`HUMAN NUDGE REQUIRED`

## Final handoff

Return only non-secret facts:

- course ID/title;
- resolved owner Canvas user ID or other non-secret stable identifier;
- enrollment role/status;
- credential rotation success/failure (never the credential);
- exact Grace inspection route already supported by Savnac;
- confirmation course 17 remains untouched;
- confirmation SWOSU Canvas 24298 was untouched.

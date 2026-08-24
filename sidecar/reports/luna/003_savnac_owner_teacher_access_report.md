# Prompt 003 — Savnac owner Teacher access

## Verdict

**SAVNAC OWNER TEACHER ACCESS READY**

## Non-secret result

- Course: **18 — Computing Commons — Visual Prototype (Week 2)**; course
  state remained `available`.
- Course 17 was verified as the known duplicate shell and was not deleted or
  modified.
- Existing Jeremy Savnac user resolved as Canvas user ID **3**. Existing
  evidence shows this same user is already an active Teacher in Savnac courses
  1, 7, and 8.
- Course 18 enrollment was already satisfied: user ID 3 had one active
  `TeacherEnrollment`, so no duplicate enrollment was created.
- Course 18 read-back showed one enrollment total and zero
  `StudentEnrollment` records.

## Credential handling

The exposed `agent-admin@savnac.local` administrator login was rotated using
the installed Canvas/Authlogic Pseudonym path. A locally generated 256-bit
hex credential was used; the protected Brandy record was atomically replaced
only after the Canvas mutation succeeded and remains mode `0600`. A bounded
non-secret Canvas read of course 18 authenticated successfully. No old or new
credential value is recorded here, in Git, or in chat.

## Boundaries

No course content, modules, pages, assignments, due dates, grades,
submissions, student enrollments, course 17, VM/network/libvirt state, or
SWOSU Canvas course 24298 was modified by Prompt 003.

## Grace route

Use the existing private tunnel:

```bash
ssh -L 3002:192.168.122.172:3000 jevert@10.2.0.48
```

Then open `http://localhost:3002/courses/18/modules` in the browser after
logging in with the normal Savnac account. The owner should now see the course
through **Courses → Computing Commons** as Teacher.

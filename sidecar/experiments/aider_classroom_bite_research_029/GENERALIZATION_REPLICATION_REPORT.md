# Mission 029 generalization replication report

Mission 028's simultaneous 360-second whole/diff failures are best classified
as local model-service/caller-path availability evidence. Mission 029 restored
the exact versions/model/CPU route and passed a 2.58-second direct model check,
but the exact Aider verification path did not reproducibly complete after one
apparatus repair cycle. Therefore no scored matrix exists.

| format | verification attempts | valid complete | invalid | engineering | Aider |
|---|---:|---:|---:|---:|---:|
| whole | 4 | 0 | 4 | not estimable | not estimable |
| diff | 1 | 0 | 1 | not estimable | not estimable |

The diff row has only the initial reset failure because the frozen runner stops
after the whole-format failure. No result is inferred for either treatment.

Latency distributions, failure taxonomy by treatment, inspectability, and the
Mission 025 diff advantage are not estimable. This run does not justify an
Aider 101 diff rule or any model-capability conclusion. The supported teaching
rule remains `SMALL JOB + SMALL WORKSPACE`.

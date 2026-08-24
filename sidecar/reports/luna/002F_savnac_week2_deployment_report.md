# 002F Savnac Week 2 deployment

Deployment used the established Harbor/Imprint transport through the new
Savnac-only adapter `scripts/deploy_savnac_visual_slice.py`. It created the
clearly labeled course **Computing Commons — Visual Prototype (Week 2)**,
course id **18**, and three modules containing five pages plus one published
0-point prototype assignment. The course and modules were then published for
owner inspection. The machine-readable manifest is
`sidecar/evidence/savnac/002F_deployment_manifest.json`.

The first attempt also created duplicate shell course 17 before the adapter's
all-state lookup was corrected. It contains the same nine objects and was not
deleted because that cleanup is destructive and requires owner approval.

Read-back is recorded separately in `sidecar/evidence/savnac/002G_readback.json`.
No Quick Tune, synthetic students, student records, or SWOSU Canvas were used.

**SAVNAC VISUAL SLICE DEPLOYED FOR OWNER INSPECTION**

# Invalid caller attempts

The first three MICRO and three SMALL attempts were not scored. Aider was passed an absolute path and interpreted it as a literal `path/to/...` path, editing an unintended untracked tree while leaving the intended fixture unchanged. Their raw outputs and timings are preserved under the attempt directories. The caller was corrected to pass the repository-relative source path before any valid scoring resumes.

Reviewer Prompt:
“Review meta/pending_changes.md. Ensure each change aligns to docs/Influences.md and meta/standards.md. Annotate with evidence and trace file paths. Flag conflicts in meta/issues.md. Mark review_complete=true when done.”

Editor Prompt:
“Read meta/state.json. If review_complete=true and apply=true, apply all checked changes from meta/pending_changes.md. Generate unified diffs in .changes/. Commit logs in meta/change_log/. Enforce config/constitution.json and meta/standards.md. Reset state.json.”

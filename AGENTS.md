# Research Paper Watch

Keep public paper metadata in `data/papers.json`, the only editable catalogue.
Generate `README.md` and `dist/index.html` with `python3 scripts/paper_watch.py build`.
Do not copy PDFs, private notes, raw conversations, experiments, or credentials.
Verify paper identity and public links from primary sources; use null for unknown links.
Chinese summaries cover problem, method, value, and limits in 80–160 characters total.
Do not create or change scheduled tasks as part of catalogue maintenance.
Daily task integration uses existing task IDs and preserves their research scope and schedule.
Run Python unit tests, Node reader tests, and generated-file consistency checks before publishing.
Scheduled publishing may stage only data/papers.json, README.md, and dist/index.html.
Never force-push or expand GitHub permissions. Publishing target: RipeMangoBox/research-paper-watch.

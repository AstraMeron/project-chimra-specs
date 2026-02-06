```markdown
# Pull Request Checklist

Please ensure the following before requesting review or merging.

- [ ] I have referenced the relevant `specs/` documents (link to spec).
- [ ] I have added or updated tests and run the TDD baseline locally.
  - Run locally: `$env:PYTHONPATH = '.'; uv run pytest`
- [ ] I have run linters and static analysis.
- [ ] My PR does not bypass Judge or Safety logic; financial flows are gated.
- [ ] Any changes to data models are accompanied by an ADR in `docs/adr/`.
- [ ] Secrets or keys are not checked into source control.
- [ ] At least one code reviewer has been requested and assigned.

Include a short summary of the change and the `specs/` reference in the PR description.

``` 

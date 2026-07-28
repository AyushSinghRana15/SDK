# Module 1: Agent Loop Notebook

`module1_agent_loop.ipynb` demonstrates a basic Claude Agent SDK workflow for auditing a local codebase.
The code is now separated into `notebooks/module1_agent_loop.py`, and this document keeps the markdown walkthrough.

The notebook:

- operates on the committed `data/` codebase containing TODO and FIXME comments;
- loads `ANTHROPIC_API_KEY` from `.env`;
- configures an agent with read-only `Read`, `Glob`, and `Grep` tools;
- asks the agent to find TODO/FIXME comments and summarize them by file and line number; and
- saves the agent response to `todo_fixme_report.md`.

The example shows the agent loop managed by `query()`: Claude can inspect files, receive tool results, and continue until it returns a final answer. The tool allowlist keeps the audit read-only.

To run the live audit, Claude Code and an Anthropic API key with access to the required service are needed. The notebook setup can run successfully even if the API account does not have that entitlement; in that case, the report will contain the API error instead of an audit result.

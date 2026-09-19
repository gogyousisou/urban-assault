# Security Policy for AI-Assisted Work

This repository may be edited with AI-assisted tools. AI recommendations must not be treated as proof that an external repository, package, MCP server, skill, GitHub Action, binary, or script is safe.

- Do not add or run external code without verifying the official source, owner, source code, history, dependencies, requested permissions, and network behavior.
- Do not commit API keys, GitHub Secrets, OAuth data, cookies, tokens, passwords, or other credentials.
- Require explicit human approval before cloning external repositories, downloading Releases, running binaries or scripts, adding MCP servers, skills, plugins, containers, packages, or third-party GitHub Actions, or granting new permissions.
- Do not use commands such as `curl ... | bash`, obfuscated PowerShell, or other direct execution methods when the retrieved content has not been reviewed.
- Set GitHub Actions `permissions` explicitly and keep them to the minimum required. Prefer commit-SHA pinning for third-party Actions after verifying their source.
- Keep jobs that receive secrets separate from jobs that process untrusted external input, and never print secrets to logs or artifacts.

If compromise is suspected, stop execution and revoke or rotate sessions, tokens, OAuth grants, API keys, and credentials. Changing only the password may not invalidate stolen sessions.

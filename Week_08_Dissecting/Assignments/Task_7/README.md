# Task 7: Local MCP tool

This directory contains a minimal Python MCP server with one tool,
`count_words`, which counts whitespace-separated words without accessing the
network or filesystem.

## Setup and verification

From the repository root, create a virtual environment, install the dependency,
and run the MCP client check:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r Week_08_Dissecting/Assignments/Task_7/requirements.txt
.venv/bin/python -m Week_08_Dissecting.Assignments.Task_7.verify_tool
```

The check starts the server over stdio, discovers `count_words`, calls it once,
and prints the result.

The workspace registration is in [`.vscode/mcp.json`](../../../.vscode/mcp.json).
The MCP configuration uses the repository's `.venv` interpreter. For a native
Windows environment, change `command` to
`${workspaceFolder}/.venv/Scripts/python.exe`.

After opening the repository in VS Code, start or restart the
`task7-local-tool` server from the MCP servers UI.

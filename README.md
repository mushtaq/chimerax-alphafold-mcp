# ChimeraX MCP

A Model Context Protocol (MCP) server that enables Claude AI to directly interact with ChimeraX and its AlphaFold integration for structural biology and protein analysis.

## Installation

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager.

```bash
uvx --from git+https://github.com/mushtaq/chimerax-alphafold-mcp chimerax-mcp
```

## Configuration

### 1. Enable ChimeraX REST API

In ChimeraX command line:
```bash
remotecontrol rest start
```

### 2. Configure Claude Code

Add to MCP settings:

```bash
claude code mcp add chimerax-alphafold uvx --from git+https://github.com/mushtaq/chimerax-alphafold-mcp chimerax-mcp
```

### 3. Configure VS Code

Install the MCP extension and add the server:

```bash
code --add-mcp "{\"name\":\"chimerax-alphafold\",\"command\":\"uvx\",\"args\":[\"--from\",\"git+https://github.com/mushtaq/chimerax-alphafold-mcp\",\"chimerax-mcp\"]}"
```
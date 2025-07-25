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
remotecontrol rest start port 63269
```

### 2. Configure Claude Code

```bash
# Add MCP server
claude mcp add chimerax-alphafold -- uvx --from git+https://github.com/mushtaq/chimerax-alphafold-mcp chimerax-mcp

# List configured servers
claude mcp list

# Remove server (if needed)
claude mcp remove chimerax-alphafold
```

### 3. Configure VS Code

```bash
# Add MCP server
code --add-mcp "{\"name\":\"chimerax-alphafold\",\"command\":\"uvx\",\"args\":[\"--from\",\"git+https://github.com/mushtaq/chimerax-alphafold-mcp\",\"chimerax-mcp\"]}"

# List/remove servers: Use VS Code UI (Extensions > MCP SERVERS section)
```

## Usage

Once configured, start a Claude CLI session:

```bash
claude
```

Then ask Claude to perform ChimeraX tasks using natural language:

**Example commands:**
- "Load PDB structure 1UBQ and display it as cartoon"
- "Use AlphaFold to predict the structure of this protein sequence: MKFLVL..."
- "Search for kinase structures in the PDB"
- "Fetch the AlphaFold structure for UniProt ID P04637"
- "Color the protein by secondary structure and save a high-res image"
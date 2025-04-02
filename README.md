# ChimeraX-AlphaFold-MCP: Integrating ChimeraX and AlphaFold with Claude AI

ChimeraX-AlphaFold-MCP connects ChimeraX and its AlphaFold Tool to Claude AI through the Model Context Protocol (MCP), enabling Claude to directly interact with and control PyMOL. This powerful integration allows for conversational structural biology, molecular visualization, and structure prediction and analysis capabilities through natural language.




## Features

- **Two-way communication**: Connect Claude AI to ChimeraX through a REST API.
- **Intelligent command parsing**: Natural language processing for Chimera and AlphaFold commands
- **Molecular visualization control**: Manipulate representations, colors, and views
- **Structural analysis**: Perform measurements, alignments, and other analyses
- **Code execution**: Run arbitrary Python code in ChimeraX from Claude
- **Protein Structure Prediction**: Directly run AlphaFold & ESMFold Commands by typing your workflow.



## Installation Guide

### Prerequisites

- ChimeraX installed on your system (Any Version After March 18th 2024)
- Claude for Desktop
- Python 3.10 or newer
- Git

### Step 1: Install the UV Package Manager

**On macOS:**

```bash
brew install uv
```

**On Windows:**

```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
set Path=C:\Users\[YourUsername]\.local\bin;%Path%
```

For other platforms, visit the [UV installation guide](https://docs.astral.sh/uv/getting-started/installation/).

### Step 2: Clone the Repository

```bash
git clone https://github.com/GDAmitha/chimerax-alphafold-mcp.git
cd pymol-mcp
```

### Step 3: Set Up the Environment

Create and activate a Python virtual environment:

```bash
python -m venv venv
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**On Windows:**

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

With the virtual environment activated:

```bash
pip install mcp
```

### Step 5: Configure Claude Desktop

1. Open Claude Desktop
2. Go to Claude > Settings > Developer > Edit Config
3. This will open the `claude_desktop_config.json` file
4. Add the MCP server configuration:

```json
{
  "mcpServers": {
    "pymol": {
      "command": "[Full path to your venv python]",
      "args": ["[Full path to pymol_mcp_server.py]"]
    }
  }
}
```

For example:

```json
{
  "mcpServers": {
    "pymol": {
      "command": "/Users/username/chimerax-alphafold-mcp/venv/bin/python",
      "args": ["/Users/username/chimerax-alphafold-mcp/mcp_direct_chimerax.py"]
    }
  }
}
```

> **Note:** Use the actual full paths on your system. On Windows, use forward slashes (/) instead of backslashes.

### Step 6: Start listening on ChimeraX

1. Open ChimeraX
2. Type "remotecontrol rest start" into the command line.

## Usage

### Starting the Connection

 In Claude Desktop:
   - You should see a hammer icon in the tools section when chatting
   - Click it to access the ChimeraX & AlphaFold tools

### Example Commands

Here are some examples of what you can ask Claude to do:

- "Load PDB 1UBQ and display it as cartoon"
- "Color the protein by secondary structure"
- "Highlight the active site residues with sticks representation"
- "Align two structures and show their differences"
- "Calculate the distance between these two residues"
- "Save this view as a high-resolution image"

## Troubleshooting

- **Connection issues**: Make sure the REST connection plugin is listening at http://127.0.0.1:63269/cmdline.html
- **Command errors**: Check the ChimeraX output window for any error messages
- **AlphaFold Collab not appearing**: Restart ChimeraaX and check that the connection was established.
- **Claude not connecting**: Verify the paths in your Claude configuration file are correct

## Limitations & Notes

- Some complex operations may need to be broken down into simpler steps
- Always save your work before using experimental features
- Join our Bio-MCP Community to troubleshoot, provide feedback & improve Bio-MCPS! https://join.slack.com/t/bio-mcpslack/shared_invite/zt-31z4pho39-K5tb6sZ1hUvrFyoPmKihAA

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
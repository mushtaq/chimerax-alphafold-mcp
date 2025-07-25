"""
ChimeraX AlphaFold MCP Client

This module provides the main entry point for the ChimeraX AlphaFold MCP server.
It imports and exposes the functionality from the server module.
"""

import sys

try:
    from .server import main as _main
except ImportError as e:
    print(f"Error importing server module: {e}")
    print("Make sure the server module is available in the package.")
    sys.exit(1)


def main():
    """
    Main entry point for the ChimeraX AlphaFold MCP server.

    This function starts the MCP server that provides tools for:
    - Direct ChimeraX command execution
    - AlphaFold structure prediction
    - AlphaFold structure fetching by UniProt ID
    - Protein PDB searching
    """
    try:
        _main()
    except KeyboardInterrupt:
        print("\nShutting down MCP server...")
        sys.exit(0)
    except Exception as e:
        print(f"Error starting MCP server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

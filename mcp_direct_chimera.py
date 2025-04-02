import re
import os
import json
import logging
import requests
import urllib.parse
from contextlib import asynccontextmanager
from typing import Dict, Any, AsyncIterator

from mcp.server.fastmcp import FastMCP, Context

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ChimeraXDirectMCP")

# ChimeraX connection details
CHIMERAX_HOST = "127.0.0.1"
CHIMERAX_PORT = 63269
CHIMERAX_BASE_URL = f"http://{CHIMERAX_HOST}:{CHIMERAX_PORT}"

# MCP server setup
@asynccontextmanager
async def server_lifespan(server: FastMCP) -> AsyncIterator[dict]:
    logger.info("Starting ChimeraX Direct MCP server")
    yield {}
    logger.info("ChimeraX Direct MCP server shut down")

mcp = FastMCP("ChimeraXDirectMCP",
              description="ChimeraX Direct MCP Server",
              lifespan=server_lifespan)

def send_to_chimerax(command: str) -> Dict[str, Any]:
    """
    Send a command directly to ChimeraX using the correct URL format.
    
    Args:
        command: Command to execute in ChimeraX
    
    Returns:
        Dictionary with the response details
    """
    try:
        # Replace spaces with + in the URL (as shown in the working URL)
        encoded_command = command.replace(" ", "+")
        
        # Create the full URL with the command
        url = f"{CHIMERAX_BASE_URL}/run?command={encoded_command}"
        
        logger.info(f"Sending command: {command}")
        logger.info(f"Using URL: {url}")
        
        # Send the GET request
        response = requests.get(url)
        
        if response.status_code == 200:
            logger.info("Command executed successfully")
            return {
                "status": "success",
                "output": response.text,
                "error": None
            }
        else:
            logger.error(f"Command failed with status {response.status_code}")
            return {
                "status": "error",
                "output": None,
                "error": f"HTTP error {response.status_code}: {response.text}"
            }
    except Exception as e:
        logger.error(f"Error sending command: {e}")
        return {
            "status": "error",
            "output": None,
            "error": str(e)
        }

@mcp.tool()
def parse_and_execute(ctx: Context, user_input: str) -> str:
    """
    Execute a ChimeraX command directly.
    
    Args:
        user_input: Command to execute in ChimeraX
        
    Returns:
        Result of the command execution
    """
    if not user_input.strip():
        return "Empty command"
    
    command = user_input.strip()
    result = send_to_chimerax(command)
    
    if result["status"] == "success":
        return result["output"] or "Command executed successfully"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def alphafold_predict(ctx: Context, sequence: str) -> str:
    """
    Predict the structure of a protein sequence using AlphaFold.
    
    Args:
        sequence: Protein sequence to predict
    
    Returns:
        Result of the prediction
    """
    # Simply construct the direct command as seen in the working URL
    command = f"alphafold predict {sequence}"
    result = send_to_chimerax(command)
    
    if result["status"] == "success":
        return result["output"] or "AlphaFold prediction started successfully"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def alphafold_fetch(ctx: Context, uniprot_id: str) -> str:
    """
    Fetch an AlphaFold structure by UniProt ID.
    
    Args:
        uniprot_id: UniProt ID of the protein
    
    Returns:
        Result of the fetch operation
    """
    command = f"alphafold fetch {uniprot_id}"
    result = send_to_chimerax(command)
    
    if result["status"] == "success":
        return result["output"] or f"Fetched AlphaFold structure for {uniprot_id}"
    else:
        return f"Error: {result['error']}"

@mcp.tool()
def search_protein_pdbs(ctx: Context, protein_type: str, num_results: int = 10) -> str:
    """
    Search for protein PDBs based on the specified type.
    
    Args:
        protein_type: Type of protein to search for
        num_results: Maximum number of results to return
    
    Returns:
        Search results
    """
    command = f"open pdb:search:{protein_type} limit {num_results}"
    result = send_to_chimerax(command)
    
    if result["status"] == "success":
        return result["output"] or f"Search completed for '{protein_type}'"
    else:
        return f"Error: {result['error']}"

def main():
    mcp.run()

if __name__ == "__main__":
    main()
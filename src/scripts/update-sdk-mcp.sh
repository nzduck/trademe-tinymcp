#!/bin/bash
# update-sdk-mcp.sh
# 
# This script updates both the Trade Me SDK and MCP server in development mode.
# 
# Prerequisites:
# - The trademe-sdk project must be located in the same parent directory as this project
# - Expected structure:
#   parent-folder/
#   ├── trademe-sdk/          # Trade Me SDK project
#   └── trademe-tinymcp/      # This MCP server project
#
# The script:
# 1. Activates the virtual environment for this project
# 2. Installs the SDK in editable mode from the sibling directory
# 3. Installs this MCP server in editable mode
#

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Navigate to the project root (two levels up from scripts directory)
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

cd "$PROJECT_ROOT"
source .venv/bin/activate

# Install the SDK from sibling directory in editable mode
pip install -e ../trademe-sdk

# Install this MCP server in editable mode
pip install -e .

echo "SDK and MCP server updated. Restart Claude Code to see changes (remember to run from VENV)."
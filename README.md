# Trade Me MCP Server

A simple Model Context Protocol (MCP) server for integrating with Trade Me APIs through an external SDK.

## Overview

This MCP server provides tools for interacting with Trade Me APIs. It's designed to work with Claude Code and other MCP-compatible applications.

## Features

- **Hello World**: Basic connectivity test
- **Server Info**: Get information about the MCP server
- **SDK Connection Test**: Verify connection to Trade Me SDK wrapper
- **Extensible**: Ready for integration with your Trade Me API SDK

## Prerequisites

This MCP server depends on a separate Trade Me SDK project that must be installed alongside it. 

### Required Project Structure

Both projects should be located in the same parent directory:

```
parent-folder/
├── trademe-sdk/          # Trade Me SDK project (required dependency)
└── trademe-tinymcp/      # This MCP server project
```

## Installation

1. **Ensure you have the Trade Me SDK project**: 
   - Clone the `trademe-sdk` project from: https://github.com/nzduck/trademe-sdk
   - Place it in the same parent directory as this project

2. **Navigate to the project directory**:
   ```bash
   cd trademe-tinymcp
   ```

3. **Install dependencies using uv (recommended):**
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -e .
   ```

4. **Install the Trade Me SDK dependency**:
   ```bash
   pip install -e ../trademe-sdk
   ```

5. **Install development dependencies (optional):**
   ```bash
   uv sync --group dev
   ```

### Quick Setup Script

For development, you can use the provided script to install both the SDK and MCP server:

```bash
bash src/scripts/update-sdk-mcp.sh
```

This script will:
- Activate the virtual environment
- Install the Trade Me SDK in editable mode from the sibling directory
- Install this MCP server in editable mode

## Usage

### Running the Server

Run the MCP server using the command-line interface:

```bash
python -m trademe_mcp.server
```

Or using the installed script:

```bash
trademe-mcp
```

### Testing the Server

Test that the server is working correctly:

```bash
# Test basic functionality
python -c "
import asyncio
from trademe_mcp.server import mcp

async def test():
    # This would typically be done by an MCP client
    print('Server initialized successfully')

asyncio.run(test())
"
```

### Integration with Claude Code

To use this MCP server with Claude Code, add it to your Claude Code configuration:

```json
{
  "mcpServers": {
    "trademe": {
      "command": "python",
      "args": ["-m", "trademe_mcp.server"],
      "env": {}
    }
  }
}
```

## Development

### Project Structure

```
trademe-tinymcp/
├── src/trademe_mcp/
│   ├── __init__.py
│   ├── server.py          # Main MCP server implementation
│   └── sdk_wrapper.py     # Trade Me SDK wrapper (placeholder)
├── pyproject.toml         # Project configuration
├── README.md              # This file
└── .gitignore            # Git ignore rules
```

### Available Tools

- `hello_world()`: Returns a simple greeting
- `get_server_info()`: Returns server metadata and available tools
- `test_sdk_connection()`: Tests the connection to the Trade Me SDK wrapper

### Extending the Server

1. **Replace the SDK wrapper**: Update `src/trademe_mcp/sdk_wrapper.py` with your actual Trade Me SDK integration
2. **Add new tools**: Create new `@mcp.tool()` decorated functions in `server.py`
3. **Add resources**: Use `@mcp.resource()` decorators for data endpoints

### Development Tools

Run linting and formatting:

```bash
# Format code
uv run black src/

# Lint code  
uv run ruff src/

# Run tests
uv run pytest
```

## Troubleshooting

### Common Setup Issues

1. **"No module named 'trademe_sdk'" error**:
   - Ensure the `trademe-sdk` project is in the correct location (sibling directory)
   - If missing, clone it from: https://github.com/nzduck/trademe-sdk
   - Install the SDK in editable mode: `pip install -e ../trademe-sdk`
   - Run the update script: `bash src/scripts/update-sdk-mcp.sh`

2. **Script fails with path errors**:
   - Verify the project structure matches the expected layout
   - Ensure both projects are in the same parent directory
   - Check that the virtual environment is activated

3. **Claude Code integration issues**:
   - Remember to start Claude Code from the virtual environment
   - Restart Claude Code after making changes to see updates

## Requirements

- Python 3.10 or higher
- MCP SDK 1.2.0 or higher
- Trade Me SDK project (must be in sibling directory)

## License

This project is a development stub. Add your license information here.
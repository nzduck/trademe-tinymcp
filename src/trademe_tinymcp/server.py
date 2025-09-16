#!/usr/bin/env python3
"""
Trade Me MCP Server

A simple Model Context Protocol server that provides tools for interacting
with Trade Me APIs through an external SDK.
"""

import asyncio
import logging
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP
from trademe_sdk import TMClient, ensure_auth

logger = logging.getLogger(__name__)

mcp = FastMCP("Trade Me MCP Server")

@mcp.tool()
async def hello_world() -> str:
    """A simple hello world tool to verify the MCP server is working."""
    return "Hello from Trade Me MCP Server!"

@mcp.tool()
async def get_server_info() -> Dict[str, Any]:
    """Get information about this MCP server."""
    return {
        "name": "Trade Me MCP Server",
        "version": "0.1.0",
        "description": "A simple MCP server for Trade Me API integration",
        "tools": ["hello_world", "get_server_info", "test_sdk_connection", "get_listing", "get_watchlist"]
    }

@mcp.tool()
async def test_sdk_connection() -> Dict[str, Any]:
    """Test the connection to the Trade Me SDK."""
    try:
        auth = ensure_auth()
        client = TMClient(auth)
        # Test with a simple API call
        result = client.get_watchlist(rows=1)
        return {
            "status": "success",
            "message": "SDK connection test successful",
            "data": {"api_accessible": True, "watchlist_items": len(result.get("List", []))}
        }
    except Exception as e:
        logger.error(f"SDK connection test failed: {e}")
        return {
            "status": "error",
            "message": f"SDK connection test failed: {str(e)}",
            "data": None
        }

@mcp.tool()
async def get_listing(listing_id: int) -> Dict[str, Any]:
    """Get details for a specific Trade Me listing.
    
    Args:
        listing_id: The ID of the listing to retrieve
    """
    try:
        auth = ensure_auth()
        client = TMClient(auth)
        result = client.get_listing(listing_id)
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        logger.error(f"Failed to get listing {listing_id}: {e}")
        return {
            "status": "error",
            "message": f"Failed to get listing: {str(e)}",
            "data": None
        }

@mcp.tool()
async def get_watchlist(filter_type: str = "All", page: int = 1, rows: int = 50, category: Optional[str] = None) -> Dict[str, Any]:
    """Get the user's watchlist from Trade Me.
    
    Args:
        filter_type: Filter type (default: "All")
        page: Page number (default: 1) 
        rows: Number of items per page (default: 50)
        category: Optional category filter
    """
    try:
        auth = ensure_auth()
        client = TMClient(auth)
        kwargs = {"filter": filter_type, "page": page, "rows": rows}
        if category:
            kwargs["category"] = category
        result = client.get_watchlist(**kwargs)
        return {
            "status": "success",
            "data": result
        }
    except Exception as e:
        logger.error(f"Failed to get watchlist: {e}")
        return {
            "status": "error",
            "message": f"Failed to get watchlist: {str(e)}",
            "data": None
        }

def main():
    """Main entry point for the server."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    try:
        logger.info("Starting Trade Me MCP Server...")
        mcp.run()
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise

if __name__ == "__main__":
    main()
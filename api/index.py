import sys
import os

# Add src to path so mcp_mt5 can be imported
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from mcp_mt5.main import mcp

# Expose the ASGI app for Vercel
app = mcp.http_app(path="/")

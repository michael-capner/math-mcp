# math-mcp

This project is a simple MCP (Model Context Protocol) server for basic math operations.

## Prerequisites
- Python 3.12+
- [uv](https://github.com/charliermarsh/uv) (for running the server)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/michael-capner/math-mcp.git
   cd math-mcp
   ```
2. Install dependencies:
   ```bash
   uv pip install -r requirements.txt
   ```
   Or, if using `pyproject.toml`:
   ```bash
   uv pip install -e .
   ```

## Running the MCP Server

You can start the MCP server using the following command:

```bash
uv --directory /workspaces/math-mcp run server.py
```

Or use the configuration in `.vscode/mcp.json` for integration with MCP tools.

## MCP Server Configuration

The MCP server is configured in `.vscode/mcp.json` as follows:

```json
{
  "servers": {
    "math-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/workspaces/math-mcp",
        "run",
        "server.py"
      ]
    }
  },
  "inputs": []
}
```

## Project Structure
- `server.py`: Main MCP server implementation
- `pyproject.toml`: Project metadata and dependencies
- `uv.lock`: Dependency lock file
- `.vscode/mcp.json`: MCP server configuration

## License
MIT

# Keyless MCP Server

A stateless Model Context Protocol server with no authentication required.

## Features
- Zero dependencies (uses zeromcp)
- Stateless per MCP 2026-07-28 spec
- No API keys or auth tokens
- Simple HTTP/SSE transport

## Quick Start

```bash
pip install zeromcp
python server.py
```

Server runs on http://localhost:8000

## Tools
- `echo` - Returns the input message
- `add` - Adds two integers

## Usage
Connect any MCP-compatible client to `http://localhost:8000/mcp` or use the SSE endpoint.

## Deployment

### Docker
```bash
docker build -t keyless-mcp .
docker run -p 8000:8000 keyless-mcp
```
# Lemon Email MCP Server

A Model Context Protocol (MCP) server that provides email sending capabilities through the Lemon Email service. This allows AI agents and applications to send transactional emails programmatically.

## Features

- 🍋 **Lemon Email Integration**: Send emails through the Lemon Email API
- 🤖 **MCP Compatible**: Works with any MCP-compatible AI agent or application
- ⚡ **Easy Setup**: Simple configuration with environment variables
- 🧪 **Built-in Testing**: Includes test client and standalone testing mode
- 🐍 **Pure Python**: No complex dependencies

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/lemon-email-mcp.git
cd lemon-email-mcp

# Install dependencies
pip install -r requirements.txt

# Set your API key
export LEMON_EMAIL_API_KEY="your-api-key-here"

# Test the server
python simple_mcp_server.py test
```

### Usage as MCP Server

Start the MCP server:
```bash
python simple_mcp_server.py
```

The server provides one tool:
- `send_email`: Send transactional emails via Lemon Email API

### Configuration

Set the following environment variable:
- `LEMON_EMAIL_API_KEY`: Your Lemon Email API key (required)
- `LEMON_EMAIL_API_BASE_URL`: API base URL (optional, defaults to Lemon Email API)

### Integration Examples

#### Continue.dev (VS Code)
```yaml
mcpServers:
  - name: lemon-email
    command: python
    args:
      - /path/to/simple_mcp_server.py
    env:
      LEMON_EMAIL_API_KEY: your-api-key
```

#### Claude Desktop
```json
{
  "mcpServers": {
    "lemon-email": {
      "command": "python",
      "args": ["/path/to/simple_mcp_server.py"],
      "env": {
        "LEMON_EMAIL_API_KEY": "your-api-key"
      }
    }
  }
}
```

## API Reference

### send_email Tool

Send an email using the Lemon Email service.

**Parameters:**
- `to` (string, required): Recipient email address
- `subject` (string, required): Email subject line
- `body` (string, required): Email body content
- `fromemail` (string, required): Sender email address
- `fromname` (string, optional): Sender name (default: "Email Assistant")
- `toname` (string, optional): Recipient name
- `tag` (string, optional): Email tag for tracking (default: "mcp-agent")
- `variables` (object, optional): Template variables
- `replyto` (string, optional): Reply-to email address

**Example:**
```json
{
  "name": "send_email",
  "arguments": {
    "to": "recipient@example.com",
    "subject": "Hello from AI Agent",
    "body": "This email was sent by an AI agent!",
    "fromemail": "sender@example.com",
    "fromname": "AI Assistant"
  }
}
```

## Development

### Testing

Run the comprehensive test suite:
```bash
python mcp_client_test.py
```

Run standalone email test:
```bash
python simple_mcp_server.py test
```

### Project Structure

```
lemon-email-mcp/
├── simple_mcp_server.py    # Main MCP server
├── mcp_client_test.py      # Test client
├── requirements.txt        # Dependencies
├── README.md              # This file
└── LICENSE               # MIT License
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/lemon-email-mcp/issues)
- 📧 **Email**: Create an issue for support
- 📖 **MCP Docs**: [Model Context Protocol](https://modelcontextprotocol.io/)

---

Built with ❤️ for the AI agent ecosystem.
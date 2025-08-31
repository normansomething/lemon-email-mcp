# Lemon Email MCP Server

A Model Context Protocol (MCP) server that provides email sending capabilities through the Lemon Email service. This allows AI agents and applications to send transactional emails programmatically.

## 🚀 Live Deployment

**The MCP server is now deployed and ready to use!**

🌐 **Deployed at**: https://lemon-email-mcp-production.up.railway.app/

### Quick Test the Deployed API

```bash
curl -X POST https://lemon-email-mcp-production.up.railway.app/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "to": "your-email@example.com",
    "subject": "Test from Lemon Email MCP",
    "body": "Hello! This email was sent via our deployed MCP server.",
    "fromemail": "mail@normanszobotka.com",
    "api_key": "your-lemon-email-api-key"
  }'
```

### 🔑 Get Your API Key

**Lemon Email is cheaper than Mailchimp and Resend!** 

Get your API key:

- 🐦 **DM us on X (Twitter)**: [@Norman_Szobotka](https://x.com/Norman_Szobotka)
- 📧 **Email us**: [manojk030303@gmail.com](mailto:manojk030303@gmail.com)

## Features

- 🍋 **Lemon Email Integration**: Send emails through the Lemon Email API
- 🌐 **Web API**: RESTful API for easy integration
- 🤖 **MCP Compatible**: Works with any MCP-compatible AI agent or application
- ⚡ **Easy Setup**: Simple configuration with your API key
- 🧪 **Built-in Testing**: Includes test client and standalone testing mode
- 🐍 **Pure Python**: No complex dependencies
- 💰 **Cost-Effective**: Cheaper than Mailchimp and Resend

## Usage Options

### 1. 🌐 Use the Deployed Web API (Recommended)

**No setup required!** Just use our deployed service:

```bash
# Send email via REST API
curl -X POST https://lemon-email-mcp-production.up.railway.app/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "to": "recipient@example.com",
    "subject": "Your Subject",
    "body": "Your email content here",
    "fromemail": "mail@normanszobotka.com",
    "fromname": "Your Name",
    "api_key": "your-lemon-email-api-key"
  }'
```

**Parameters:**
- `to` (required): Recipient email
- `subject` (required): Email subject
- `body` (required): Email content
- `fromemail` (required): Sender email
- `api_key` (required): Your Lemon Email API key
- `fromname` (optional): Sender name
- `toname` (optional): Recipient name
- `tag` (optional): Email tag for tracking
- `variables` (optional): Template variables
- `replyto` (optional): Reply-to email

### 2. 🔧 Local MCP Server Setup

For local development or custom setups:

```bash
# Clone the repository
git clone https://github.com/manojk0303/lemon-email-mcp.git
cd lemon-email-mcp

# Install dependencies
pip install -r requirements.txt

# Set your API key
export LEMON_EMAIL_API_KEY="your-api-key-here"

# Test the server
python simple_mcp_server.py test

# Start MCP server
python simple_mcp_server.py
```

### 3. 🌐 Run Web Server Locally

```bash
# Start local web server
python web_server.py

# Server runs at http://localhost:8001
```

## Integration Examples

### Continue.dev (VS Code)
```yaml
mcpServers:
  - name: lemon-email
    command: python
    args:
      - /path/to/simple_mcp_server.py
    env:
      LEMON_EMAIL_API_KEY: your-api-key
```

### Claude Desktop
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

### JavaScript/Node.js Integration
```javascript
const response = await fetch('https://lemon-email-mcp-production.up.railway.app/send-email', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    to: 'recipient@example.com',
    subject: 'Hello from Node.js',
    body: 'This email was sent from my JavaScript app!',
    fromemail: 'mail@normanszobotka.com',
    api_key: 'your-lemon-email-api-key'
  })
});

const result = await response.json();
console.log(result);
```

### Python Integration
```python
import requests

response = requests.post(
    'https://lemon-email-mcp-production.up.railway.app/send-email',
    json={
        'to': 'recipient@example.com',
        'subject': 'Hello from Python',
        'body': 'This email was sent from my Python app!',
        'fromemail': 'mail@normanszobotka.com',
        'api_key': 'your-lemon-email-api-key'
    }
)

print(response.json())
```

## API Endpoints

### 🌐 Deployed Service Endpoints

- **Base URL**: https://lemon-email-mcp-production.up.railway.app/
- **Health Check**: `GET /health`
- **Send Email**: `POST /send-email`
- **API Documentation**: `GET /docs` (Interactive Swagger UI)
- **Server Info**: `GET /mcp-info`

## MCP Tool Reference

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

## Testing

### Test the Deployed API
```bash
# Health check
curl https://lemon-email-mcp-production.up.railway.app/health

# Send test email
curl -X POST https://lemon-email-mcp-production.up.railway.app/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "to": "test@example.com",
    "subject": "API Test",
    "body": "Testing the deployed API!",
    "fromemail": "sender@example.com",
    "api_key": "your-api-key"
  }'
```

### Local Testing
```bash
# Run comprehensive test suite
python mcp_client_test.py

# Run standalone email test
python simple_mcp_server.py test

# Test local web server
python run_local.py
```

## Why Lemon Email?

🍋 **Better Than the Competition**

- 💰 **Cheaper than Mailchimp** - Save money on your email costs
- 💰 **Cheaper than Resend** - Better pricing for developers
- 🚀 **Fast & Reliable** - Built for developers who need performance
- 🤖 **AI-Ready** - Perfect integration with AI agents and automation
- 🔧 **Simple API** - Easy to integrate, no complex setup
- 📊 **Great Analytics** - Track your email performance

## Project Structure

```
lemon-email-mcp/
├── simple_mcp_server.py    # Main MCP server
├── web_server.py           # Web API server (Railway deployment)
├── mcp_client_test.py      # MCP protocol test client
├── run_local.py           # Local testing script
├── requirements.txt        # Dependencies
├── Procfile               # Railway deployment config
├── README.md              # This file
└── LICENSE               # MIT License
```

## Development

### Local Development Setup
```bash
git clone https://github.com/manojk0303/lemon-email-mcp.git
cd lemon-email-mcp
pip install -r requirements.txt

# Test everything locally
python run_local.py
```

### Deploy Your Own Instance
1. Fork this repository
2. Connect to Railway/Vercel/Heroku
3. No environment variables needed (users provide their own API keys)
4. Deploy!

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support & Contact

- 🐛 **Issues**: [GitHub Issues](https://github.com/manojk0303/lemon-email-mcp/issues)
- 🐦 **Get API Key**: [@Norman_Szobotka](https://x.com/Norman_Szobotka)
- 📧 **Email**: [manojk030303@gmail.com](mailto:manojk030303@gmail.com)
- 📖 **MCP Docs**: [Model Context Protocol](https://modelcontextprotocol.io/)
- 🌐 **Live API**: https://lemon-email-mcp-production.up.railway.app/

## Quick Links

- 🚀 **Try it now**: https://lemon-email-mcp-production.up.railway.app/
- 📚 **API Docs**: https://lemon-email-mcp-production.up.railway.app/docs
- 🔍 **Health Check**: https://lemon-email-mcp-production.up.railway.app/health

---

Built with ❤️ for the AI agent ecosystem. **Cheaper than Mailchimp & Resend!** 🍋
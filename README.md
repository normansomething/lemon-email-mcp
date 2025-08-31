# 🍋 Lemon Email MCP

> **The email API that just works.** Open source. AI-ready. Zero config.

<div align="center">

[![Live Demo](https://img.shields.io/badge/🌐_Try_Now-Live-brightgreen?style=for-the-badge)](https://lemon-email-mcp-production.up.railway.app/)
[![Open Source](https://img.shields.io/badge/📖_Open_Source-MIT-blue?style=for-the-badge)](https://github.com/manojk0303/lemon-email-mcp)
[![Get API Key](https://img.shields.io/badge/🔑_Get_Key-Instant-orange?style=for-the-badge)](https://x.com/Norman_Szobotka)

</div>

---

## ⚡ Send Your First Email in 30 Seconds

```bash
curl -X POST https://lemon-email-mcp-production.up.railway.app/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "to": "user@example.com",
    "subject": "Hello World 👋",
    "body": "This was stupid easy to send.",
    "fromemail": "mail@member-notification.com",
    "api_key": "your-key-here"
  }'
```

**Need an API key?** → DM [@Norman_Szobotka](https://x.com/Norman_Szobotka) or email [manojk030303@gmail.com](mailto:manojk030303@gmail.com)

💡 **Pro tip**: If you don't want to set up DNS records with your domain, you are free to use `mail@member-notification.com` as your sender - it's pre-configured and works with any API key!

---

## 🚀 Why This is a No-Brainer

**🌐 Use Our API** (Recommended)
- Zero setup required
- Works instantly
- Use `mail@normanszobotka.com` as sender (pre-configured)
- Or configure your own domain
- Global infrastructure
- Free to try

**🏠 Run Locally** (Open Source)
- Full source code available
- Host anywhere you want  
- Customize everything
- MIT licensed

**🤖 AI Integration**
- Built for Claude Desktop
- MCP protocol support
- Perfect for AI agents
- Works with any AI tool

---

## 🛠 Quick Integrations

<details>
<summary><b>JavaScript</b> - Copy & paste ready</summary>

```javascript
const response = await fetch('https://lemon-email-mcp-production.up.railway.app/send-email', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    to: 'user@example.com',
    subject: 'Your app just got email superpowers',
    body: 'Welcome to the future!',
    fromemail: 'mail@normanszobotka.com', // Pre-configured sender
    api_key: 'your-key-here'
  })
});

const result = await response.json();
console.log('Email sent!', result);
```

</details>

<details>
<summary><b>Python</b> - Two lines, that's it</summary>

```python
import requests

response = requests.post('https://lemon-email-mcp-production.up.railway.app/send-email', json={
    'to': 'user@example.com',
    'subject': 'Python made this easy',
    'body': 'No complicated setup needed!',
    'fromemail': 'mail@normanszobotka.com',  # Pre-configured sender
    'api_key': 'your-key-here'
})

print('Done!', response.json())
```

</details>

<details>
<summary><b>Claude Desktop</b> - AI email assistant</summary>

Add to your Claude Desktop config:

```json
{
  "mcpServers": {
    "lemon-email": {
      "command": "python",
      "args": ["/path/to/simple_mcp_server.py"],
      "env": {
        "LEMON_EMAIL_API_KEY": "your-key-here"
      }
    }
  }
}
```

Now Claude can send emails for you automatically!

</details>

---

## 🏠 Run It Locally (Open Source)

**1. Clone & Run**
```bash
git clone https://github.com/manojk0303/lemon-email-mcp.git
cd lemon-email-mcp
pip install -r requirements.txt

# Set your API key
export LEMON_EMAIL_API_KEY="your-key-here"

# Start local server
python web_server.py
```

**2. Test It**
```bash
# Your local server runs at http://localhost:8001
curl -X POST http://localhost:8001/send-email -H "Content-Type: application/json" -d '{...}'
```

**3. Deploy Anywhere**
- Railway ✅
- Vercel ✅  
- Heroku ✅
- Your own server ✅

---

## 🔥 Real Use Cases

**🤖 AI Agents**
- Customer support bots
- Automated notifications  
- Workflow automation

**🚀 Web Apps**
- User onboarding emails
- Password resets
- Order confirmations

**⚡ Side Projects**
- Newsletter sending
- Contact form emails
- Event notifications

---

## 📚 What You Get

**☁️ Hosted API**
- `POST /send-email` - Send emails
- `GET /health` - Check status
- `GET /docs` - Interactive docs

**📦 Open Source**
- Full Python source code
- MIT license
- Deploy anywhere
- Customize everything

**🤖 MCP Integration**
- Works with Claude Desktop
- AI agent ready
- Zero config needed

---

## 🌟 Getting Started

**Option 1: Use Our API (5 minutes)**
1. Get API key → DM [@Norman_Szobotka](https://x.com/Norman_Szobotka)
2. Copy code example above
3. Send your first email
4. Ship your app

**Option 2: Self-Host (10 minutes)**  
1. `git clone` the repo
2. `pip install -r requirements.txt`
3. Set your API key
4. `python web_server.py`

---

<div align="center">

## 🚀 Ready to send emails the easy way?

[![Try the API](https://img.shields.io/badge/🌐_Try_API_Now-Free-brightgreen?style=for-the-badge)](https://lemon-email-mcp-production.up.railway.app/)
[![Download Code](https://img.shields.io/badge/📦_Get_Source_Code-Open_Source-blue?style=for-the-badge)](https://github.com/manojk0303/lemon-email-mcp)
[![Get API Key](https://img.shields.io/badge/🔑_Get_API_Key-30_seconds-orange?style=for-the-badge)](https://x.com/Norman_Szobotka)

**Questions?** → [manojk030303@gmail.com](mailto:manojk030303@gmail.com) | **Updates** → [@Norman_Szobotka](https://x.com/Norman_Szobotka)

</div>

---

<div align="center">
<sub>Open source • MIT licensed • Made for developers</sub>
</div>

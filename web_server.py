#!/usr/bin/env python3
"""
Web wrapper for Railway deployment of Lemon Email MCP Server
This creates a simple web interface and health endpoint for Railway
"""

import asyncio
import json
import os
import threading
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uvicorn

# Import your existing email server
from simple_mcp_server import LemonEmailServer

# FastAPI app
app = FastAPI(
    title="Lemon Email MCP Server - Web Interface",
    description="Web wrapper for the Lemon Email MCP Server",
    version="1.0.0"
)

# Initialize email server (for class definition only, users provide their own API key)
try:
    # Create a dummy instance just to validate the class works
    if os.getenv("LEMON_EMAIL_API_KEY"):
        email_server = LemonEmailServer()
    else:
        # Create class without API key for public API mode
        email_server = None
except Exception as e:
    print(f"Note: Running in public API mode - users will provide their own API keys")
    email_server = None

# Pydantic models
class EmailRequest(BaseModel):
    # Email content
    to: str
    subject: str
    body: str
    fromname: str = "Email Assistant"
    fromemail: str
    toname: str = ""
    tag: str = "web-api"
    variables: Optional[Dict[str, Any]] = None
    replyto: Optional[str] = None
    
    # User's API key
    api_key: str

@app.get("/")
async def root():
    """Root endpoint with basic info"""
    return HTMLResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>🍋 Lemon Email MCP Server</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; }
            .header { text-align: center; color: #333; }
            .status { padding: 20px; background: #f0f8ff; border-radius: 8px; margin: 20px 0; }
            .endpoint { background: #f9f9f9; padding: 15px; margin: 10px 0; border-radius: 5px; }
            .code { background: #e8e8e8; padding: 10px; border-radius: 3px; font-family: monospace; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🍋 Lemon Email MCP Server</h1>
            <p>Web Interface & API</p>
        </div>
        
        <div class="status">
            <h3>📊 Status</h3>
            <p><strong>Server:</strong> Running ✅</p>
            <p><strong>Email Service:</strong> Ready ✅</p>
            <p><strong>Mode:</strong> Public API (users provide their own API key)</p>
        </div>
        
        <div class="endpoint">
            <h3>🔍 Available Endpoints</h3>
            <ul>
                <li><strong>GET /</strong> - This page</li>
                <li><strong>GET /health</strong> - Health check</li>
                <li><strong>POST /send-email</strong> - Send email via API</li>
                <li><strong>GET /docs</strong> - API documentation</li>
            </ul>
        </div>
        
        <div class="endpoint">
            <h3>📡 MCP Integration</h3>
            <p>This server is designed for <strong>Model Context Protocol (MCP)</strong> integration.</p>
            <p>For MCP usage, connect to this server using the MCP protocol on the standard input/output.</p>
        </div>
        
        <div class="endpoint">
            <h3>🔧 Quick Test</h3>
            <p>Test the email API (replace with your Lemon Email API key):</p>
            <pre class="code">curl -X POST """ + os.getenv("RAILWAY_PUBLIC_URL", "https://your-app.railway.app") + """/send-email \\
  -H "Content-Type: application/json" \\
  -d '{
    "to": "test@example.com",
    "subject": "Test Email",
    "body": "Hello from Railway!",
    "fromemail": "mail@normanszobotka.com",
    "api_key": "your-lemon-email-api-key-here"
  }'</pre>
        </div>
    </body>
    </html>
    """)

@app.get("/health")
async def health_check():
    """Health check endpoint for Railway"""
    status = {
        "status": "healthy",
        "service": "lemon-email-mcp-server",
        "version": "1.0.0",
        "mode": "public_api",
        "description": "Users provide their own Lemon Email API keys"
    }
    
    return JSONResponse(status)

@app.post("/send-email")
async def send_email_api(email: EmailRequest, background_tasks: BackgroundTasks):
    """Send email via REST API with user's API key"""
    
    try:
        # Create a temporary email server instance with user's API key
        user_email_server = LemonEmailServer()
        user_email_server.api_key = email.api_key  # Use user's API key
        
        result = await user_email_server.send_email(
            to=email.to,
            subject=email.subject,
            body=email.body,
            fromname=email.fromname,
            fromemail=email.fromemail,
            toname=email.toname,
            tag=email.tag,
            variables=email.variables,
            replyto=email.replyto
        )
        
        if result["success"]:
            return {
                "success": True,
                "message": "Email sent successfully",
                "status_code": result["status_code"],
                "response": result["response"]
            }
        else:
            raise HTTPException(
                status_code=400,
                detail=result.get("error", "Unknown error occurred")
            )
            
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to send email: {str(e)}"
        )

@app.get("/mcp-info")
async def mcp_info():
    """Information about MCP integration"""
    return {
        "mcp_server": {
            "name": "lemon-email",
            "version": "1.0.0",
            "description": "Send emails via Lemon Email API",
            "protocol": "Model Context Protocol (MCP)",
            "tools": [
                {
                    "name": "send_email",
                    "description": "Send transactional emails",
                    "required_params": ["to", "subject", "body", "fromemail"],
                    "optional_params": ["fromname", "toname", "tag", "variables", "replyto"]
                }
            ]
        },
        "integration_notes": [
            "This server runs in web mode when deployed on Railway",
            "For MCP protocol usage, run locally with: python simple_mcp_server.py",
            "Environment variable LEMON_EMAIL_API_KEY is required"
        ]
    }

# Background task to run MCP server (if needed)
def run_mcp_in_background():
    """Run MCP server in background (optional)"""
    # This could be used if you want to support both web and MCP simultaneously
    pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    
    print("🍋 Starting Lemon Email MCP Server - Web Mode")
    print(f"🌐 Port: {port}")
    print(f"🔑 API Key configured: {bool(os.getenv('LEMON_EMAIL_API_KEY'))}")
    print("🚀 Starting server...")
    
    uvicorn.run(
        "web_server:app",
        host="0.0.0.0",
        port=port,
        reload=False
    )
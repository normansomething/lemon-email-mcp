# Contributing to Lemon Email MCP

Thank you for your interest in contributing to Lemon Email MCP! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

1. Check the [existing issues](https://github.com/manojk0303/lemon-email-mcp/issues) first
2. Create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, etc.)

### Suggesting Features

1. Check existing issues and discussions
2. Create a feature request issue with:
   - Clear description of the feature
   - Use case and benefits
   - Proposed implementation (if you have ideas)

### Code Contributions

1. Fork the repository
2. Create a feature branch from `main`
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Update documentation as needed
7. Submit a pull request

### Development Setup

```bash
git clone https://github.com/yourusername/lemon-email-mcp.git
cd lemon-email-mcp
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

### Code Style

- Follow PEP 8
- Use Black for formatting: `black .`
- Add type hints where appropriate
- Write clear docstrings for functions and classes

### Testing

```bash
pip install pytest pytest-asyncio
pytest
```

## Code of Conduct

Please be respectful and constructive in all interactions. We're all here to build something great together!

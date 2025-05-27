# 🕷️ Decodo Website Scraper

A Model Context Protocol (MCP) server that provides website scraping capabilities using the Decodo scraping API. This tool allows you to extract text content from specific HTML elements on web pages.

## ✨ Features

- **🌐 Website Scraping**: Scrapes any publicly accessible website using the Decodo API
- **🎯 Targeted Content Extraction**: Extracts text from specific HTML div elements by ID
- **🔌 MCP Integration**: Built as an MCP server for seamless integration with AI assistants

## 📦 Installation

1. Download Claude Desktop from this website and log in.

```bash
https://claude.ai/download
```

2. Create a Decodo account and get your API key:  
   Claim your free trial on Decodo: https://visit.decodo.com/aOL4yR

3. Clone this repository:

```bash
git clone https://github.com/abdullahtarek/mcp_webscrapper
cd decodo-webscrapper
```

4. Replace the API key at the top main.py with your Decodo API key.

5. Install uv:

```bash
pip install uv
```

6. Run MCP server and connect it to Claude Desktop:

```bash
uv run mcp install -e. main.py
```

## 🚀 Usage

Once installed and connected to Claude Desktop, you can use the scraper by asking Claude to scrape websites. The tool will extract content from specified HTML elements using the Decodo API.

## ⚙️ Requirements

- Python 3.8+
- uv package manager
- Decodo API key
- Claude Desktop

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

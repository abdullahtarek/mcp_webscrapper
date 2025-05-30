from mcp.server.fastmcp import FastMCP
from typing import List
import requests
from bs4 import BeautifulSoup
import json

# Decodo API Token (Get your API token from https://visit.decodo.com/aOL4yR)
decodo_token = "VTAwMDAyNjc0Mzk6T3lkc19haU4yTTVucjIwd2pG"

# Create MCP server
mcp = FastMCP("DecodoWebsiteScrapper")

# Tool: Get Article Text
@mcp.tool()
def get_article_text(website_url:str, div_id: str) -> str:
    """Scrapes a website HTML and extracts the text from the given div Id"""

    # Scrape Website
    url = "https://scraper-api.decodo.com/v2/scrape"
  
    payload = {
        "url": website_url
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Basic " + decodo_token
    }
    crawled_article = requests.post(url, json=payload, headers=headers)
    crawled_article_json = json.loads(crawled_article.text)

    # If article is not crawled correctly retutn None
    status_code = crawled_article_json['results'][0]['status_code']
    if status_code!=200:
        return "Website Can't be Crawled"
    
    # Create BeautifulSoup object from HTML
    html_string = crawled_article_json['results'][0]['content']
    soup = BeautifulSoup(html_string,'html.parser')

    # Get Article Text
    story_div = soup.find('div',id=div_id)
    if story_div is None:
        return "Div does not exist"
    
    text = story_div.get_text(strip=True,separator='\n')

    return text

if __name__ == "__main__":
    mcp.run()



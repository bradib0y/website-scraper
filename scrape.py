import os
import asyncio
from crawl4ai import AsyncWebCrawler
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import aiohttp
import sys

async def fetch_links(session, url):
    async with session.get(url) as resp:
        raw = await resp.read()  # get bytes, not text
        # Try UTF-8, then ISO-8859-1/ISO-8859-2, then replace errors
        for encoding in ("utf-8", "iso-8859-1", "iso-8859-2"):
            try:
                html = raw.decode(encoding)
                break
            except UnicodeDecodeError:
                continue
        else:
            html = raw.decode("utf-8", errors="replace")  # fallback

        soup = BeautifulSoup(html, "html.parser")
        links = set()
        for a in soup.find_all("a", href=True):
            link = urljoin(url, a['href'])
            if urlparse(link).netloc == urlparse(url).netloc:
                links.add(link)
        return html, links



async def main():
    #start_url = "https://kenese.accenthotels.com/hu"
    start_url = sys.argv[1]
    visited = set()
    to_visit = {start_url}

    async with aiohttp.ClientSession() as session:
        while to_visit:
            url = to_visit.pop()
            if url in visited:
                continue
            visited.add(url)

            html, links = await fetch_links(session, url)
            soup = BeautifulSoup(html, "html.parser")
            title = soup.title.string.strip() if soup.title else "No title"
            text = soup.get_text(separator="\n", strip=True)

            print("URL:", url)
            print("Title:", title)
            print("Text:", text[:2000])  # printing first 2000 chars to avoid huge output
            print("="*80)

            # Add new links to visit
            to_visit.update(links - visited)

if __name__ == "__main__":
    if os.environ.get("BUILD_IMAGE_FOR_DEV") == "true":
        import debugpy
        debugpy.listen(("0.0.0.0", 5678))
        print("Waiting for debugger to attach...")
        debugpy.wait_for_client()
    asyncio.run(main())

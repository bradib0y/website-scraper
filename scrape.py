import os
import asyncio
from crawl4ai import AsyncWebCrawler


async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://kenese.accenthotels.com/hu")
        print(result.markdown)

if __name__ == "__main__":
    if os.environ.get("BUILD_IMAGE_FOR_DEV") == "true":
        import debugpy
        debugpy.listen(("0.0.0.0", 5678))
        print("Waiting for debugger to attach...")
        debugpy.wait_for_client()
    asyncio.run(main())

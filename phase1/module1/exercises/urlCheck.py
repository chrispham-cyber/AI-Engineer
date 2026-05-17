import asyncio

import aiohttp


async def check_url(session, url):
    try:
        async with session.get(url, timeout=10) as resp:
            return url, resp.status
    except Exception as e:
        return url, str(e)


async def run(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [check_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results


if __name__ == "__main__":
    urls = [
        "https://google.com",
        "https://g0ogle.com",
        "https://gooogle.com",
        "https://fb.com",
        "https://facebook.com",
        "https://yt.com",
        "https://youtube.com",
        "https://github.com",
        "https://invalid.url",
    ]

    results = asyncio.run(run(urls))

    for url, status in results:
        print(url, status)

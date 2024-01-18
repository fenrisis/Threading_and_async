import aiohttp
import asyncio
import time


async def fetch(session, url):
    try:
        start_time = time.time()
        async with session.get(url) as response:
            if response.status != 200:
                # Exceptions
                raise aiohttp.ClientResponseError(
                    request_info=response.request_info,
                    history=response.history,
                    status=response.status,
                    message=f"Non-200 status code: {response.status}",
                    headers=response.headers
                )
            resp_time = time.time() - start_time
            print(f"URL: {url} - Time: {resp_time:.3f} seconds.")
            return await response.text()
    except aiohttp.ClientResponseError as e:
        print(f"URL: {url} returned a non-200 status code. Details: {e}")
    except aiohttp.ClientError as e:
        print(f"URL: {url} could not be reached. ClientError: {e}")
    except Exception as e:
        print(f"URL: {url} could not be reached. General Error: {e}")


async def main():
    urls = [
        "http://python.org",
        "https://google.com",
        "http://example.com",
        "https://github.com",
        "https://slcms-b65449f506fa.herokuapp.com/"  # 503
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())

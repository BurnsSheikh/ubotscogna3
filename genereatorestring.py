import asyncio
from pyrogram import Client

API_ID   = 17222139 #api id che prendi da my.telegram.org
API_HASH = 'ffd330fed81cf05cc639f6b8ff71389b' #api hash che prendi da my.telegram.org


async def gensess(api_id, api_hash):
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        print('------\n')
        print(await app.export_session_string())
        print('------\n')

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gensess(API_ID, API_HASH))
import plustik

bot = plustik.Client("69661788:lAhqXlSddLf-ZO3n0TfthdyAWf4QkXzpd04")

async def main():
    me = await bot.get_me()
    print(me.first_name)

import asyncio
asyncio.run(main())
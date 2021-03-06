# (c) @dasqinnagiyev

import asyncio
from configs import Config
from multiprocessing import Process
from pyrogram import Client, filters
from dasqin.livestatus import GetLiveStatus
from pyrogram.types import Message

Bot0 = Client(
    session_name="Looped-Session",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)
Bot1 = Client(
    session_name="LiveStatus-Session",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)


def thread0():
    with Bot0 as bot:
        try:
            print("Canlı nəticələr başlayır...")
            asyncio.get_event_loop().run_until_complete(GetLiveStatus(bot, Config.STATUS_UPDATE_CHANNEL_ID))
        except KeyboardInterrupt:
            print("Canlı nəticələr dayanır...")


def thread1():
    @Bot1.on_message(filters.command("start"))
    async def start_command(_, event: Message):
        await event.reply_text("Salam, bot @daqobots'a məxsusdur.")

    Bot1.run()


if __name__ == '__main__':
    try:
        p1 = Process(target=thread0)
        p1.start()
        p2 = Process(target=thread1)
        p2.start()
        p1.join()
        p2.join()
    except KeyboardInterrupt:
        print("Döngələnmiş Sessiyadan çıxılır...")

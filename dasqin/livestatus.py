# (c) @dasqinnagiyev

import aiohttp
import asyncio
import datetime
from pyrogram import Client
from pyrogram.types import Message
from dasqin.send_msg import SendMessage, EditMessage

MessagesDB = {}


async def GetData(date: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://www.fotmob.com/matches?date={date}") as resp:
            data = await resp.json()
            return data


async def GetLiveStatus(bot: Client, updates_channel_id: int):
    running = False
    status = ""
    reason = ""
    while True:
        print("Məlumatlar əldə edilir...")
        data = await GetData(str(datetime.datetime.now().date()).replace('-', ''))
        for i in range(len(data["leagues"])):
            print("Məlumatlar yüklənir...")
            for x in range(len(data["leagues"][i]["matches"])):
                leagueName = data["leagues"][i]["name"]
                firstMatchTime = data["leagues"][i]["matches"][x]["time"]
                finished = data["leagues"][i]["matches"][x]["status"].get("finished", True)
                started = data["leagues"][i]["matches"][x]["status"].get("started", False)
                cancelled = data["leagues"][i]["matches"][x]["status"].get("cancelled", False)
                ongoing = data["leagues"][i]["matches"][x]["status"].get("ongoing", False)
                score = data["leagues"][i]["matches"][x]["status"].get("scoreStr", "")
                if score == "":
                    score = f"{data['leagues'][i]['matches'][x]['home']['score']} - {data['leagues'][i]['matches'][x]['away']['score']}"
                if (finished is False) and (started is True) and (cancelled is False) and (ongoing is True):
                    running, status = True, "Başladı"
                elif finished is True:
                    running, status = False, "Bitdi"
                elif cancelled is True:
                    running, status, reason = False, "Cancelled", data["leagues"][i]["matches"][x]["status"].get("reason", {}).get("long", "")
                if (running is True) and (finished is False) and (ongoing is True):
                    liveTime = data["leagues"][i]["matches"][x]["status"].get("liveTime", {}).get("long", "")
                    text = f"**Liqa Adı:** `{leagueName}`\n\n" \
                           f"**Oyun Tarixi:** `{firstMatchTime}`\n\n" \
                           f"**Oyun vəziyyəti:** `{status}`\n\n" \
                           f"**Oyun neçənci dəqiqədədi:** `{liveTime}`\n\n" \
                           f"**Komandalar:** `{data['leagues'][i]['matches'][x]['home']['name']}`  __VS__  `{data['leagues'][i]['matches'][x]['away']['name']}`\n\n" \
                           f"**Nəticə:** `{score}`"
                           markup = types.InlineKeyboardMarkup()

for url in stringList.items():
    markup.add(types.InlineKeyboardButton(text=Oyunu Paylaş,
                                          callback_data="['url', url="https://telegram.me/share/url?url=https://t.me/ndfutbol")
                    if MessagesDB.get(data["leagues"][i]["matches"][x]["id"], None) is None:
                        message = await SendMessage(bot, text, updates_channel_id)
                        MessagesDB[data["leagues"][i]["matches"][x]["id"]] = message
                        print("5s-lik fasilə...")
                        await asyncio.sleep(5)
                    else:
                        editable: Message = MessagesDB[data["leagues"][i]["matches"][x]["id"]]
                        await EditMessage(editable, text)
                elif running is False:
                    if MessagesDB.get(data["leagues"][i]["matches"][x]["id"], None) is not None:
                        status_reason = f"{status}\n\n" \
                                        f"**Səbəb:** `{reason}`\n\n"
                        text = f"**Liqa adı:** `{leagueName}`\n\n" \
                               f"**Oyun Tarixi:** `{firstMatchTime}`\n\n" \
                               f"**Oyun Vəziyyəti:** `{status if (status == 'Finished') else status_reason}`\n\n" \
                               f"**Komandalar:** `{data['leagues'][i]['matches'][x]['home']['name']}`  __VS__  `{data['leagues'][i]['matches'][x]['away']['name']}`\n\n" \
                               f"**Nəticə:** `{score}`"
                               button = [
            [InlineKeyboardButton(text = 'Oyunu Paylaş', url="https://telegram.me/share/url?url=https://t.me/ndfutbol")],
        ]
                        editable: Message = MessagesDB[data["leagues"][i]["matches"][x]["id"]]
                        await EditMessage(editable, text)
        print("60s-lik fasilə...")
        await asyncio.sleep(60)

import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Hikari.events import register
from Hikari import telethn as tbot


PHOTO = "https://telegra.ph/file/3a0688ef26c90fdc706e7.jpg"

@register(pattern=("/alive"))
async def awake(event):
  PRIME = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Kazu Robot.** \n\n"
  PRIME += "ð¼ **I'm Working Properly** \n\n"
  PRIME += f"ð¼ **My TUAN : [Ò á´§Æ¶á´](https://t.me/kazuinhere)** \n\n"
  PRIME += f"ð¼ **Library Version :** `{telever}` \n\n"
  PRIME += f"ð¼ **Telethon Version :** `{tlhver}` \n\n"
  PRIME += f"ð¼ **Pyrogram Version :** `{pyrover}` \n\n"
  PRIME += "**Thanks For Adding Me Here â¤ï¸**"
  BUTTON = [[Button.url("Êá´Êá´â", "https://t.me/kaazuuBot?start=help"), Button.url("sá´á´á´á´Êá´â", "https://t.me/punyasejutaumat")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)

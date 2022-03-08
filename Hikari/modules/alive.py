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
  PRIME += "🌼 **I'm Working Properly** \n\n"
  PRIME += f"🌼 **My TUAN : [Ҡᴧƶᴜ](https://t.me/kazuinhere)** \n\n"
  PRIME += f"🌼 **Library Version :** `{telever}` \n\n"
  PRIME += f"🌼 **Telethon Version :** `{tlhver}` \n\n"
  PRIME += f"🌼 **Pyrogram Version :** `{pyrover}` \n\n"
  PRIME += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/kaazuuBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/punyasejutaumat")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PRIME,  buttons=BUTTON)

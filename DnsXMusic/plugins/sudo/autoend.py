#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.
#
from pyrogram import filters

from strings import get_command
from HarryXSarkar import app
from HarryXSarkar.misc import SUDOERS
from HarryXSarkar.utils.database import autoend_off, autoend_on

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**ᴜsᴀɢᴇ:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Aᴜᴛᴏ Eɴᴅ Sᴛʀᴇᴀᴍ Eɴᴀʙʟᴇᴅ.\n\nBᴏᴛ ᴡɪʟʟ ʟᴇᴀᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀғᴛᴇʀ 3 ᴍɪɴs ɪғ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ ᴡɪᴛʜ ᴀ ᴡᴀʀɴɪɴɢ ᴍᴇssᴀɢᴇ.."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("ᴀᴜᴛᴏᴇɴᴅ ᴅɪsᴀʙʟᴇᴅ")
    else:
        await message.reply_text(usage)

#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.
#
import math

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from HarryXSarkar.utils.formatters import time_to_seconds

def get_progress_bar(percentage):
    umm = math.floor(percentage)

    if 0 < umm <= 10:
        return "─▷─────────"
    elif 10 < umm <= 20:
        return "──▷────────"
    elif 20 < umm <= 30:
        return "───▷───────"
    elif 30 < umm <= 40:
        return "────▷──────"
    elif 40 < umm <= 50:
        return "─────▷─────"
    elif 50 < umm <= 60:
        return "──────▷────"
    elif 60 < umm <= 70:
        return "───────▷───"
    elif 70 < umm <= 80:
        return "────────▷──"
    elif 80 < umm <= 90:
        return "─────────▷─"
    elif 90 < umm <= 100:
        return "──────────▷"
    else:
        return "───────────"


def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    bar = get_progress_bar(percentage)  # using for getting the bar
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
          [
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=f"https://t.me/Dns_Official_Channel"
            ),
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍 💬", url=f"https://t.me/DNS_NETWORK"
          ),
        ],
        [InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="𝖢𝗅𝗈𝗌𝖾")],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
          [
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=f"https://t.me/Dns_Official_Channel"
            ),
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍 💬", url=f"https://t.me/DNS_NETWORK"
          ),
        ],
        [InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="𝖢𝗅𝗈𝗌𝖾")],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    bar = get_progress_bar(percentage)  # using for getting the bar
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
          [
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=f"https://t.me/Dns_Official_Channel"
            ),
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍 💬", url=f"https://t.me/DNS_NETWORK"
          ),
        ],
        [
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="𝖢𝗅𝗈𝗌𝖾"),
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
          [
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=f"https://t.me/Dns_Official_Channel"
            ),
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍 💬", url=f"https://t.me/DNS_NETWORK"
          ),
        ],
        [
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="𝖢𝗅𝗈𝗌𝖾"),
        ],
    ]
    return buttons


## By Anon
close_keyboard = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="〆 𝖢𝗅𝗈𝗌𝖾 〆", callback_data="𝖢𝗅𝗈𝗌𝖾")]]
)

## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}"
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"DnsPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"DnsPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"forceclose {videoid}|{user_id}"
            ),
        ],
    ]
    return buttons


## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❮",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data=f"forceclose {query}|{user_id}"
            ),
            InlineKeyboardButton(
                text="❯",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons


def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [InlineKeyboardButton(text="〆 ᴄʟᴏsᴇ 〆", callback_data="close")],
    ]
    return buttons

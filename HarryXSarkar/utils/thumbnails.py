#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License .
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.
#

from youtubesearchpython.__future__ import VideosSearch

from config import YOUTUBE_IMG_URL


async def gen_thumb(videoid):
    try:
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail
    except Exception as e:
        return YOUTUBE_IMG_URL


async def gen_qthumb(vidid):
    try:
        query = f"https://www.youtube.com/watch?v={vidid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail
    except Exception as e:
        return YOUTUBE_IMG_URL
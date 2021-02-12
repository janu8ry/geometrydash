from typing import Optional
import json

import aiohttp

from .objects import *


async def api_request(url: str, params: dict = None) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            return json.loads(await response.read())


async def _get_user_info(user_data: dict) -> Optional[Profile]:  # todo: icon
    obj = Profile()
    obj.name = user_data.get('username', None)
    obj.playerID = int(user_data.get('playerID', None))
    obj.accountID = int(user_data.get('accountID', None))
    obj.rank = user_data.get('rank', None) if user_data.get('rank', None) != 0 else None
    obj.stars = user_data.get('stars', None)
    obj.diamonds = user_data.get('diamonds', None)
    obj.coins = user_data.get('coins', None)
    obj.userCoins = user_data.get('userCoins', None)
    obj.demons = user_data.get('demons', None)
    obj.cp = user_data.get('cp', None)
    obj.friendRequests = user_data.get('friendRequests', None)
    obj.messages = getattr(RelationShip(), user_data.get('messages', 'off'))
    obj.commentHistory = getattr(RelationShip(), user_data.get('commentHistory', 'off'))
    obj.moderator = user_data.get('moderator', None)
    obj.youtube = user_data.get('youtube', None)
    obj.twitter = user_data.get('twitter', None)
    obj.twitch = user_data.get('twitch', None)
    if obj.name is not None:
        return obj
    else:
        return None


async def _get_level_info(level_data: dict) -> Optional[Level]:
    obj = Level()
    obj.name = level_data.get('name', None)
    obj.id = int(level_data.get('id', None))
    obj.description = level_data.get('description', None) if level_data.get('description', None) != "(No description provided)" else None
    obj.author = await _get_user_info(await api_request(f"https://gdbrowser.com/api/profile/{level_data.get('author', None)}")) if level_data.get('author', None) != "-" else None
    obj.playerID = int(level_data.get('playerID', None))
    obj.accountID = level_data.get('accountID', None) if level_data.get('accountID', None) != 0 else None
    obj.difficulty = level_data.get('difficulty', None)
    obj.downloads = level_data.get('downloads', None)
    obj.likes = level_data.get('likes', None)
    obj.disliked = level_data.get('disliked', None)
    obj.length = level_data.get('length', None)
    obj.stars = level_data.get('stars', None)
    obj.orbs = level_data.get('orbs', None)
    obj.diamonds = level_data.get('diamonds', None)
    obj.featured = level_data.get('featured', None)
    obj.epic = level_data.get('epic', None)
    obj.gameVersion = float(level_data.get('gameVersion', None))
    obj.version = level_data.get('version', None)
    obj.copiedID = int(level_data.get('copiedID', None))
    obj.twoPlayer = level_data.get('twoPlayer', None)
    obj.officialSong = level_data.get('officialSong', None)
    obj.customSong = level_data.get('customSong', None)
    obj.coins = level_data.get('coins', None)
    obj.verifiedCoins = level_data.get('verifiedCoins', None)
    obj.starsRequested = level_data.get('starsRequested', None)
    obj.ldm = level_data.get('ldm', None)
    obj.objects = level_data.get('objects', None)
    obj.large = level_data.get('large', None)
    obj.cp = level_data.get('cp', None)
    obj.difficultyFace = level_data.get('difficultyFace', None)
    obj.songName = level_data.get('songName', None)
    obj.songAuthor = level_data.get('songAuthor', None)
    obj.songSize = float(level_data.get('songSize', None).replace("MB", ""))
    obj.songID = level_data.get('songID', None)
    obj.songLink = level_data.get('songLink', None)
    obj.demonlist = level_data.get('demonlist', None)
    if obj.id is not None:
        return obj
    else:
        return None

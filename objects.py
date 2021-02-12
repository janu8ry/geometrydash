from typing import Optional, Union


class Level:
    def __init__(self):
        self.name = str()
        self.id = int()
        self.description = str()
        self.author = Profile()
        self.playerID = int()
        self.accountID = int()
        self.difficulty = str()
        self.downloads = int()
        self.likes = int()
        self.disliked = bool()
        self.length = str()
        self.stars = int()
        self.orbs = int()
        self.diamonds = int()
        self.featured = bool()
        self.epic = bool()
        self.gameVersion = float()
        self.version = int()
        self.copiedID = int()
        self.twoPlayer = bool()
        self.officialSong = int()
        self.customSong = int()
        self.coins = int()
        self.verifiedCoins = bool()
        self.starsRequested = int()
        self.objects = int()
        self.large = bool()
        self.cp = int()
        self.difficultyFace = str()
        self.songName = str()
        self.songAuthor = str()
        self.songSize = float()
        self.songID = int()
        self.songLink = str()
        self.demonlist = int()
        self.uploaded = str()
        self.updated = str()
        self.password = Union[bool, int]
        self.ldm = bool()
        self.dailyNumber = int()
        self.nextDaily = float()
        self.nextDailyTimestamp = str()


class Profile:
    def __init__(self):
        self.name = str()
        self.playerID = int()
        self.accountID = int()
        self.rank = int()
        self.stars = int()
        self.diamonds = int()
        self.coins = int()
        self.userCoins = int()
        self.demons = int()
        self.cp = int()
        self.friendRequests = bool()
        self.messages = RelationShip()
        self.commentHistory = RelationShip()
        self.moderator = str()
        self.youtube = str()
        self.twitter = str()
        self.twitch = str()


class RelationShip:
    @classmethod
    def all(cls):
        return 'all'

    @classmethod
    def friends(cls):
        return 'friends'

    @classmethod
    def off(cls):
        return 'off'

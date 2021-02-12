class BadArgument(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class UserNotFound(Exception):
    def __init__(self, user: str):
        super().__init__(f"cannot find user '{user}'")


class LevelNotFound(Exception):
    def __init__(self, level: str):
        super().__init__(f"cannot find level '{level}'")

from typing import Union, List

from .utils import api_request, _get_level_info, _get_user_info
from .objects import Level, Profile
from .errors import *

BASEURL = "https://gdbrowser.com/api"


async def search_level(query: Union[str, int], count=10) -> Union[List[Level], Level]:
    if count < 1 or count > 500:
        raise BadArgument("'count' param should be higher than 0, lower than 501")
    if isinstance(query, int):
        levels_list = await api_request(f"{BASEURL}/level/{query}")
        if levels_list == -1:
            raise LevelNotFound(str(query))
        return await _get_level_info(levels_list)
    else:
        levels_list = await api_request(f"{BASEURL}/search/{query}", params={'count': count})
        if levels_list == -1:
            raise LevelNotFound(query)
        return [await _get_level_info(level) for level in levels_list]


async def search_user(query: Union[str, int]) -> Profile:
    users_list = await api_request(f"{BASEURL}/profile/{query}")
    if users_list == -1:
        raise UserNotFound(str(query))
    else:
        return await _get_user_info(users_list)











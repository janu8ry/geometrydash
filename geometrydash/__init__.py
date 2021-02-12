"""
Geometry Dash API Wrapper
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A basic wrapper for Geometry Dash API.

:copyright: (c) 2020 janu8ry
:license: GPL-3.0, see LICENSE for more details.

"""

__title__ = 'geometrydash'
__author__ = 'janu8ry'
__license__ = 'GPL-3.0'
__copyright__ = 'Copyright 2021 janu8ry'
__version__ = '0.1a'

from collections import namedtuple

from .errors import *
from .geometrydash import *
from .objects import *

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=1, micro=0, releaselevel='alpha', serial=0)




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
__version__ = '1.0.0'

from collections import namedtuple

from .errors import *
from .geometrydash import *
from .objects import *

VersionInfo = namedtuple('VersionInfo', 'major minor micro')

version_info = VersionInfo(major=1, minor=0, micro=0)




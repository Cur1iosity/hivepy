__description__ = "Small wrapper for HexWay Hive API "
__author__ = "@Cur1iosity"
__email__ = "Cur1iosity@protonmail.com"
__licence__ = "MIT"
__version__ = "0.1.0"

from hivepy.hive_client import Hive
from hivepy.lib.models.project import Project
from hivepy.lib.models.issue import Issue

__all__ = [
        'Hive',
        'Project',
        'Issue'
]

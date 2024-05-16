import uuid

import pydantic

from hivepy.models.unknown_hive_object import UnknownHiveObject


class Group(UnknownHiveObject):
    id: uuid.UUID
    name: str
    description: str
    slug: str
    full_slug: str = pydantic.Field(alias='fullSlug')

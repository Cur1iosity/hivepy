import uuid
from datetime import datetime
from enum import StrEnum
from typing import Optional, List, Any

import pydantic

from hivepy.schema_management.models.base_schema import BaseSchema

asset_version = StrEnum('AssetVersion', ['COMPLEX', 'SIMPLE'])
score_method = StrEnum('ScoreMethod', ['COMPLEX', 'SIMPLE'])


class IssueSchema(BaseSchema):
    id: uuid.UUID
    name: str
    description: Optional[str] = pydantic.Field(default=None)
    is_default: bool = pydantic.Field(default=False, alias='isDefault')
    predefined_fields_settings: Optional[List[Any]] = pydantic.Field(default=None, alias='predefinedFieldsSettings')
    additional_fields_settings: Optional[List[Any]] = pydantic.Field(default=None, alias='additionalFieldsSettings')
    asset_version: str = pydantic.Field(default='SIMPLE', alias='assetVersion')
    score_method: str = pydantic.Field(default='SIMPLE', alias='scoreMethod')
    structures: Optional[List[Any]] = pydantic.Field(default=None)
    fields_order: List = pydantic.Field(alias='order')
    timestamp: Optional[datetime] = pydantic.Field(default=None)
    user_id: Optional[uuid.UUID] = pydantic.Field(default=None, alias='userId')

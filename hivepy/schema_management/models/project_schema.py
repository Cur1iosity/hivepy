import datetime
import uuid
from typing import Optional, List, Any

import pydantic

from hivepy.schema_management.models.base_schema import BaseSchema


class ProjectSchema(BaseSchema):
    """Project schema model."""
    id: uuid.UUID
    predefined_fields_settings: Optional[List[Any]] = pydantic.Field(default=None, alias='predefinedFieldsSettings')
    additional_fields_settings: Optional[List[Any]] = pydantic.Field(default=None, alias='additionalFieldsSettings')
    fields_order: List = pydantic.Field(alias='fieldsOrder')

    created: datetime.datetime
    updated: Optional[datetime.datetime] = pydantic.Field(default=None)
    version: int

import datetime
import uuid
from typing import Optional, List, ForwardRef, Any

import pydantic

from hivepy.schema_management.models.base_schema import BaseSchema


class ProjectSchema(BaseSchema):
    """Project schema model."""
    id: uuid.UUID
    predefined_fields_settings: List = pydantic.Field(default_factory=list, alias='predefinedFieldsSettings')
    additional_fields_settings: List[Any] = pydantic.Field(default_factory=list, alias='additionalFieldsSettings')
    fields_order: List = pydantic.Field(alias='fieldsOrder')

    created: datetime.datetime
    updated: Optional[datetime.datetime]
    version: int

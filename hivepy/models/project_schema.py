import datetime
import uuid
from typing import Dict, Optional, List

import pydantic

from hivepy.models.field import Field
from hivepy.models.unknown_hive_object import UnknownHiveObject


class ProjectSchema(UnknownHiveObject):
    """Project schema model."""
    id: uuid.UUID
    predefined_fields_settings: List = pydantic.Field(default_factory=list, alias='predefinedFieldsSettings')
    additional_fields_settings: List[Field] = pydantic.Field(default_factory=list, alias='additionalFieldsSettings')
    fields_order: List = pydantic.Field(alias='fieldsOrder')

    created: datetime.datetime
    updated: Optional[datetime.datetime]
    version: int

    @pydantic.field_validator('additional_fields_settings', mode='before')
    def validate_additional_fields_settings(cls, v: List[Dict]) -> List[Field]:
        """Validate additional fields settings."""
        return [Field(**field) for field in v]

    @property
    def field_names(self) -> List[str]:
        """Return field names."""
        return [field.name for field in self.additional_fields_settings]

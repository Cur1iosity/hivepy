import datetime
import uuid
from typing import Dict, Optional, List

from hivepy.models.base_model import BaseModel
import pydantic


class ProjectSchema(BaseModel):
    """Project schema model."""
    _raw: Dict = pydantic.PrivateAttr()
    id: uuid.UUID
    version: int
    updated: Optional[datetime.datetime]
    predefined_fields_settings: List = pydantic.Field(default_factory=list, alias='predefinedFieldsSettings')
    additional_fields_settings: List = pydantic.Field(default_factory=list, alias='additionalFieldsSettings')
    fields_order: List = pydantic.Field(alias='fieldsOrder')
    created: datetime.datetime

    @pydantic.model_validator(mode='before')
    def set_raw_data(cls, values: Dict) -> Dict:
        """Set raw data."""
        cls._raw = values
        return values

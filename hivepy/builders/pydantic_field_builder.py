from datetime import datetime, date
from typing import Optional

from pydantic import Field as PydanticField

from hivepy.models import Field as HivepyField

FIELD_TYPE_MAPPING = {
    'TEXT': str,
    'TEXT_SUGGESTED': str,
    'TEXT_MD': str,
    'INTEGER': int,
    'BOOLEAN': bool,
    'FLOAT': float,
    'FILE': bytes,
    'DATE': date,
    'DATETIME': datetime,
    'IMAGE': str,
    'LINK': str,
}


class PydanticFieldBuilder:
    """From hivepy.Field builds pydantic.Field."""
    @staticmethod
    def make_pydantic_field(hivepy_field: HivepyField) -> PydanticField:
        """Make pydantic.Field from hivepy.Field."""
        field_type = FIELD_TYPE_MAPPING[hivepy_field.type]
        field = field_type if hivepy_field.required else Optional[field_type]
        return field

    def __call__(self, hivepy_field: HivepyField) -> PydanticField:
        """Make pydantic.Field from hivepy.Field."""
        return self.make_pydantic_field(hivepy_field)

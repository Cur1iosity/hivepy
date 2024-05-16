import keyword
from typing import Dict, Optional, List, Any, Union

import pydantic

from hivepy.enums import FieldType
from hivepy.models.unknown_hive_object import UnknownHiveObject


class Field(UnknownHiveObject):
    """Field model."""
    name: str
    value: Optional[Any] = pydantic.Field(default=None)
    display_name: str = pydantic.Field(alias='displayName')
    type: FieldType

    hint: Optional[str] = pydantic.Field(default=None)
    placeholder: Optional[str] = pydantic.Field(default=None)
    placeholder_link_text: Optional[str] = pydantic.Field(default=None, alias='placeholderLinkText')
    placeholder_link_url: Optional[str] = pydantic.Field(default=None, alias='placeholderLinkUrl')

    allowed_values: Optional[Union[Dict, List]] = pydantic.Field(default=None, alias='allowedValues')

    hidden: bool
    initially_collapsed: Optional[bool] = pydantic.Field(default=None, alias='initiallyCollapsed')
    required: bool
    is_list: bool = pydantic.Field(alias='isList')

    @pydantic.field_validator('name', mode='before')
    def validate_name(cls, v: str) -> str:
        """Validate name."""
        if v.isidentifier() and not keyword.iskeyword(v):
            return v
        else:
            raise ValueError(f'Field "{v}" is not a valid identifier.')

    @pydantic.model_validator(mode='before')
    def validate_metadata(cls, v: Dict) -> Dict:
        """Validate metadata."""
        if not (metadata := v.pop('metadata')):
            return v
        [v.update({key: val}) for key, val in metadata.items()]
        return v

    def __str__(self) -> str:
        """Return string representation."""
        return self.value

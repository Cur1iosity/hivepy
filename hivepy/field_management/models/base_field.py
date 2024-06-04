from typing import List, Optional, Any, Dict, Union
from hivepy.field_management.enums import BaseFieldType
import pydantic


class BaseField(pydantic.BaseModel):
    display_name: str = pydantic.Field(alias='displayName')
    name: str
    type: Optional[BaseFieldType] = pydantic.Field(default=None)
    value: Optional[Any] = pydantic.Field(default=None)
    allowed_values: Optional[List[str]] = pydantic.Field(default=list(), alias='allowedValues')
    is_list: bool = pydantic.Field(default=False, alias='isList')
    required: bool = pydantic.Field(default=False)
    hidden: bool = pydantic.Field(default=False)
    initially_collapsed: Optional[bool] = pydantic.Field(default=None, alias='initiallyCollapsed')
    select: Optional[bool] = pydantic.Field(default=None)
    placeholder: Optional[str] = pydantic.Field(default=None)
    hint: Optional[str] = pydantic.Field(default=None)
    placeholder_link_text: Optional[str] = pydantic.Field(default=None)
    placeholder_link_url: Optional[str] = pydantic.Field(default=None)

    model_config = pydantic.ConfigDict(
        populate_by_name=True
    )

    def __str__(self) -> str:
        """Return string representation of object."""
        return f'{self.__class__.__qualname__}({", ".join(f"{key}={value}" for key, value in self.dict().items())})'

    def __call__(self) -> Any:
        """Return value of the field."""
        return self.value

    @pydantic.field_validator('allowed_values', mode='before')
    def flatten_allowed_values(cls, v: Optional[Union[List[Dict], List[str]]]) -> Optional[List[str]]:
        """Flatten allowed values."""
        if not v:
            return []

        if hasattr(v[0], 'values'):
            return [x['displayValue'] for x in v]

        return v

    @pydantic.model_validator(mode='before')
    def parse_metadata(cls, v: Dict) -> Dict:
        """Parse metadata."""
        if not (metadata := v.pop('metadata', {})):
            return v

        [v.update({key: val}) for key, val in metadata.items()]
        return v

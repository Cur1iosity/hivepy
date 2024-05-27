from typing import Optional

import pydantic

from hivepy.field_management.enums import FieldType
from hivepy.field_management.models import BaseField


class Field(BaseField):
    """Field class."""
    type: None = pydantic.Field(default=None, exclude=True)

    @pydantic.field_validator('type', mode='before')
    def clear_type(cls, v: Optional[FieldType]) -> None:
        """Clear type."""
        v = None
        return v


class Text(Field):
    """Text field."""
    @property
    def field_info(self) -> str:
        """Return field info."""
        return f'{self.name}: {self.value}'


class SingleTextSuggested(Field):
    """Text field with single suggested value."""
    ...


class MultiTextSuggested(Field):
    """Text field with suggested values."""
    ...


class Checkbox(Field):
    """Single checkbox field."""
    ...


class Checkboxes(Field):
    """Checkboxes field."""
    ...


class RadioButton(Field):
    """RadioButtons field."""
    ...


class Select(Field):
    """Select field."""
    ...


class MultiSelect(Field):
    """MultiSelect field."""
    ...


class Link(Field):
    """Link field."""
    ...


class TextMarkdown(Field):
    """Text field with markdown."""
    ...


class Image(Field):
    """Image field."""
    ...


class File(Field):
    """File field."""
    ...


class Float(Field):
    """Float field."""
    ...


class Integer(Field):
    """Integer field."""
    ...


class Date(Field):
    """Date field."""
    ...


class DateTime(Field):
    """DateTime field."""
    ...


FIELD_TYPE_MAP = {
    FieldType.INTEGER: Integer,
    FieldType.FLOAT: Float,
    FieldType.TEXT: Text,
    FieldType.SINGLE_TEXT_SUGGESTED: SingleTextSuggested,
    FieldType.MULTI_TEXT_SUGGESTED: MultiTextSuggested,
    FieldType.CHECKBOX: Checkbox,
    FieldType.CHECKBOXES: Checkboxes,
    FieldType.TEXT_MARKDOWN: TextMarkdown,
    FieldType.RADIOBUTTON: RadioButton,
    FieldType.SELECT: Select,
    FieldType.MULTISELECT: MultiSelect,
    FieldType.LINK: Link,
    FieldType.IMAGE: Image,
    FieldType.FILE: File,
    FieldType.DATE: Date,
    FieldType.DATETIME: DateTime,
}

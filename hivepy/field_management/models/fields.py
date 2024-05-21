from hivepy.field_management.enums import FieldType
from hivepy.field_management.models import BaseField


class Text(BaseField):
    """Text field."""
    ...


class SingleTextSuggested(BaseField):
    """Text field with single suggested value."""
    ...


class MultiTextSuggested(BaseField):
    """Text field with suggested values."""
    ...


class Checkbox(BaseField):
    """Single checkbox field."""
    ...


class Checkboxes(BaseField):
    """Checkboxes field."""
    ...


class RadioButton(BaseField):
    """RadioButtons field."""
    ...


class Select(BaseField):
    """Select field."""
    ...


class MultiSelect(BaseField):
    """MultiSelect field."""
    ...


class Link(BaseField):
    """Link field."""
    ...


class TextMarkdown(BaseField):
    """Text field with markdown."""
    ...


class Image(BaseField):
    """Image field."""
    ...


class File(BaseField):
    """File field."""
    ...


class Float(BaseField):
    """Float field."""
    ...


class Integer(BaseField):
    """Integer field."""
    ...


class Date(BaseField):
    """Date field."""
    ...


class DateTime(BaseField):
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

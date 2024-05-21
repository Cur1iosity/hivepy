import datetime
from enum import Enum, StrEnum


class BaseFieldType(StrEnum):
    """Enumeration of base field types."""
    TEXT = "TEXT"
    TEXT_SUGGESTED = "TEXT_SUGGESTED"
    TEXT_MARKDOWN = "TEXT_MD"
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    FLOAT = "FLOAT"
    FILE = "FILE"
    DATE = "DATE"
    DATETIME = "DATETIME"
    IMAGE = "IMAGE"
    LINK = "LINK"


class FieldType(StrEnum):
    """Enumeration of field types."""
    FLOAT = "FLOAT"
    INTEGER = "INTEGER"
    TEXT = "TEXT"
    TEXT_MARKDOWN = "TEXT_MD"
    SINGLE_TEXT_SUGGESTED = 'SINGLE_TEXT_SUGGESTED'
    MULTI_TEXT_SUGGESTED = "MULTI_TEXT_SUGGESTED"
    RADIOBUTTON = "RADIOBUTTON"
    CHECKBOX = "CHECKBOX"
    CHECKBOXES = "CHECKBOXES"
    SELECT = "SELECT"
    MULTISELECT = "MULTISELECT"
    DATE = "DATE"
    DATETIME = "DATETIME"
    LINK = "LINK"
    IMAGE = "IMAGE"
    FILE = "FILE"


class ValueType(Enum):
    """Enumeration of value types."""
    INTEGER = int
    FLOAT = float
    TEXT = str
    TEXT_MARKDOWN = str
    SINGLE_TEXT_SUGGESTED = str
    MULTI_TEXT_SUGGESTED = list
    CHECKBOX = bool
    RADIOBUTTON = str
    CHECKBOXES = list
    SELECT = str
    MULTISELECT = list
    DATE = datetime.date
    DATETIME = datetime.datetime
    LINK = str
    IMAGE = str
    FILE = bytes

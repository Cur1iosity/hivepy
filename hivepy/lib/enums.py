from enum import StrEnum, auto


class ObjectType(StrEnum):
    """Enumeration of object types."""
    ISSUE = auto()
    ISSUE_TEMPLATE = auto()
    ISSUE_SCHEME = auto()

    PROJECT = auto()
    PROJECT_TEMPLATE = auto()
    PROJECT_GROUP = auto()


class FieldType(StrEnum):
    """Enumeration of field types."""
    STRING = auto()
    INTEGER = auto()
    FLOAT = auto()
    MARKDOWN = auto()
    CHECKBOX = auto()
    CHECKBOXES = auto()
    SELECT = auto()
    RADIO_BUTTONS = auto()
    DATE = auto()
    DATETIME = auto()
    FILE = auto()
    IMAGE = auto()
    LINK = auto()


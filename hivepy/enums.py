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
    TEXT = "TEXT"
    TEXT_SUGGESTED = "TEXT_SUGGESTED"
    TEXT_MD = "TEXT_MD"
    INTEGER = "INTEGER"
    BOOLEAN = "BOOLEAN"
    FLOAT = "FLOAT"
    FILE = "FILE"
    DATE = "DATE"
    DATETIME = "DATETIME"
    IMAGE = "IMAGE"
    LINK = "LINK"

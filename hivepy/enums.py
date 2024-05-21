from enum import StrEnum, auto


class ObjectType(StrEnum):
    """Enumeration of object types."""
    ISSUE = auto()
    ISSUE_TEMPLATE = auto()
    ISSUE_SCHEME = auto()

    PROJECT = auto()
    PROJECT_TEMPLATE = auto()
    PROJECT_GROUP = auto()

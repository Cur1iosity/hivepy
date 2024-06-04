from enum import StrEnum, auto


class ClientMode(StrEnum):
    """Enumeration of client modes."""
    JSON = auto()
    RAW_ITEMS = auto()
    OBJECT = auto()


class ObjectType(StrEnum):
    ISSUE = auto()
    PROJECT = auto()
    USER = auto()

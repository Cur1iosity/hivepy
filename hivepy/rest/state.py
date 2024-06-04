from enum import StrEnum, auto


class State(StrEnum):
    """Enumeration of states."""
    NOT_CONNECTED = auto()
    CONNECTED = auto()
    DISCONNECTED = auto()

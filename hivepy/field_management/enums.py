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
    UUID = "UUID"
    IP = "IP"
    HOSTNAME = "HOSTNAME"
    ASSET = "ASSET"
    REQUEST = "REQUEST"
    DATASOURCE = "DATASOURCE"
    STATUS = "STATUS"
    CVSS_SCORE = "CVSS_BASE_SCORE"
    CVSS_VECTOR = "CVSS_BASE_VECTOR"


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
    UUID = "UUID"
    IP = "IP"
    HOSTNAME = "HOSTNAME"
    ASSET = "ASSET"
    REQUEST = "REQUEST"
    DATASOURCE = "DATASOURCE"
    STATUS = "STATUS"
    CVSS_SCORE = "CVSS_BASE_SCORE"
    CVSS_VECTOR = "CVSS_BASE_VECTOR"


class ValueType(Enum):
    """Enumeration of value types for different fields."""
    INTEGER = int
    FLOAT = float
    TEXT = str
    UUID = str
    STATUS = str
    TEXT_MARKDOWN = str
    SINGLE_TEXT_SUGGESTED = str
    MULTI_TEXT_SUGGESTED = list
    HOSTNAME = list
    IP = list
    ASSET = list
    REQUEST = list
    DATASOURCE = str
    CVSS_SCORE = int
    CVSS_VECTOR = str
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

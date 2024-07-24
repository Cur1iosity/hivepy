import json
from typing import Optional, Dict, Tuple


class HiveRestError(Exception):
    """Base exception for Hive rest client."""
    def __init__(self, params: Dict) -> None:
        """Initialize HiveRestError."""
        self.detail = params.get('detail')
        self.status = params.get('status')
        self.title = params.get('title')
        self.type = params.get('type')

    def __str__(self) -> str:
        """Return string representation of the exception."""
        return f'[{self.status}] {self.title}: {self.detail}'


class RestConnectionError(Exception):
    """Exception for connection errors."""
    pass


class ServerUrlNotDefinedError(Exception):
    """Exception for server URL not defined."""
    pass

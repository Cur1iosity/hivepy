from typing import Optional


class ClientError(Exception):
    """Base exception for Client."""
    def __init__(self, message, content=None):
        """Initialize ClientError."""
        super().__init__(message)
        self.content: Optional[str] = content


class ClientConnectionError(ClientError):
    """Exception for connection errors."""
    def __init__(self, message):
        """Initialize ClientConnectionError."""
        super().__init__(message)


class SocksProxyError(ClientConnectionError):
    """Exception for connection errors."""
    def __init__(self, message="Couldn't connect via provided socks proxy. Check it."):
        """Initialize ClientConnectionError."""
        super().__init__(message)

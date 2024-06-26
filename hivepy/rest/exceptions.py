class HiveRestError(Exception):
    """Base exception for Hive rest client."""
    pass


class RestConnectionError(HiveRestError):
    """Exception for connection errors."""
    pass


class ServerUrlNotDefinedError(HiveRestError):
    """Exception for server URL not defined."""
    pass

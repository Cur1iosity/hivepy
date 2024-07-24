from hivepy.rest.http_client import HTTPClient
from hivepy.rest.error_handler import ErrorHandler


@ErrorHandler
class HiveMiddleware(HTTPClient):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

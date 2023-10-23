from enum import StrEnum, auto
from typing import Dict, Self, Union

import requests.utils
from hive.lib.http_client.exceptions import *
from requests import Session, Response


class HTTPMethod(StrEnum):
    """Enumeration of HTTP methods."""
    GET = auto()
    PATCH = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()

    def __str__(self) -> str:
        """Return string representation of HTTP method."""
        return self.value.upper()


class HTTPClient:
    """Base implementation of the HTTP client."""
    session: Session = Session()

    def _send(self, method: HTTPMethod, *args, **kwargs) -> Union[Dict, bytes]:
        """Universal method for sending requests."""
        try:
            response: Response = self.session.request(method, *args, **kwargs)
            try:
                return response.json()
            except requests.JSONDecodeError:
                return response.content
        except requests.ConnectionError as e:
            if 'SOCKSHTTPSConnectionPool' in str(e):
                proxy = self.session.proxies.get('https')
                raise SocksProxyError(f'Couldn\'t connect via "{proxy}". Check it.')
            else:
                raise ClientConnectionError(e)

    def _update_params(self, **kwargs) -> Self:
        """Update session parameters if they are not None and exist in session."""
        [setattr(self.session, key, value) for key, value in kwargs.items()
         if value is not None and hasattr(self.session, key)]
        return self

    def get(self, *args, **kwargs) -> Union[Dict, bytes]:
        """Send GET request."""
        return self._send(HTTPMethod.GET, *args, **kwargs)

    def post(self, *args, **kwargs) -> Dict:
        """Send POST request."""
        return self._send(HTTPMethod.POST, *args, **kwargs)

    def put(self, *args, **kwargs) -> Dict:
        """Send PUT request."""
        return self._send(HTTPMethod.PUT, *args, **kwargs)

    def patch(self, *args, **kwargs) -> Dict:
        """Send PATCH request."""
        return self._send(HTTPMethod.PATCH, *args, **kwargs)

    def delete(self, *args, **kwargs) -> Dict:
        """Send DELETE request."""
        return self._send(HTTPMethod.DELETE, *args, **kwargs)

    def add_headers(self, headers: Dict) -> Self:
        """Method injects headers into session."""
        self.session.headers.update(headers)
        return self

    def update_params(self, **kwargs) -> Self:
        """Method updates session parameters."""
        self._update_params(**kwargs)
        return self

    @property
    def params(self):
        """Method to get session parameters."""
        return self.session.__dict__

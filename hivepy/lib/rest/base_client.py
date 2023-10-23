from enum import StrEnum, auto
from typing import Type, Dict, Optional, Self

from hive.lib.http_client.http_client import HTTPClient
from hive.lib.rest.exceptions import RestConnectionError


class State(StrEnum):
    """Enumeration of states."""
    NOT_CONNECTED = auto()
    CONNECTED = auto()
    DISCONNECTED = auto()


Route = StrEnum('Route', {
    'SESSION': 'session',
    'AUTH': 'session',
    'PROJECT': 'project',
    'FILES': 'files',

})


class BaseHiveClient:
    base_url: str = None
    route: Type[Route] = None

    def __init__(self):
        """Initialize RestHive."""
        self.state: State = State.NOT_CONNECTED
        self.http_client: HTTPClient = HTTPClient()

    @staticmethod
    def _get_routes() -> Type[Route]:
        """Get routes from routes.py."""
        return Route

    def _update_base_url(self, server: str, port: int, verify: bool) -> True:
        """Prepare base url."""
        if not server.startswith('http'):
            scheme = 'https://' if verify else 'http://'
            if not port:
                port = 443 if verify else 80
            self.base_url = f"{scheme}{server}:{port}/api".strip('/ ')
        else:
            self.base_url = server.strip('/ ')
            self.base_url += '/api' if not self.base_url.endswith('/api') else ''
        return True

    def _update_http_client(self, verify: bool, proxies: Optional[Dict] = None, proxy: Optional[str] = None) -> True:
        """Prepare http client."""
        proxies = proxies or {'http': proxy, 'https': proxy} or {}
        self.http_client.update_params(verify=verify, proxies=proxies)
        self.http_client.add_headers({'Content-Type': 'application/json'})
        return True

    def _update_routes(self, server: str, port: int, verify: bool) -> True:
        """Prepare urls."""
        self._update_base_url(server, port, verify)
        self.route = StrEnum('Url', {key: f'{self.base_url}/{value.strip("/")}'
                                     for key, value in Route.__members__.items()})
        return True

    def _preconnect_update(self, **kwargs) -> True:
        """Update settings before connecting."""
        self._update_routes(**{'server': kwargs['server'],
                               'port': kwargs['port'],
                               'verify': kwargs['verify'],
                               })

        self._update_http_client(**{'verify': (kwargs['verify']),
                                    'proxies': kwargs.get('proxies'),
                                    'proxy': kwargs.get('proxy')
                                    })

        return True

    def _authenticate(self, username: str, password: str) -> None:
        """Authenticate in Hive."""
        response = self.http_client.session.post(self.route.AUTH, json={
            'userLogin': username,
            'userPassword': password,
        })

        try:
            cookie = response.cookies.get('BSESSIONID')
            self.http_client.add_headers({'Cookie': f'BSESSIONID={cookie}'})
            self.state = State.CONNECTED
        except AttributeError:
            raise RestConnectionError('Could not get authentication cookie. Something wrong with credentials '
                                      'or server.')

    def connect(self,
                server: str,
                username: str,
                password: str,
                port: Optional[int] = None,
                verify: bool = True,
                proxies: Optional[Dict] = None,
                proxy: Optional[str] = None,
                ) -> Self:
        """Method connects to Hive instance."""
        self._preconnect_update(server=server, port=port, verify=verify, proxies=proxies, proxy=proxy)
        self._authenticate(username, password)
        return self

from typing import Dict


class Router:
    """Enumeration of routes."""
    SESSION = 'session'
    AUTH = 'session'
    PROJECT = 'project'
    PROJECT_GROUP = 'groups'
    PROJECT_TEMPLATE = 'project/templates'
    FILES = 'files'

    def __init__(self, base_url: str) -> None:
        """Initialize Router."""
        self._update_routes(base_url)

    def _get_routes(self) -> Dict:
        """Get routes."""
        return {attr: getattr(self, attr) for attr in dir(self) if not attr.startswith('_')}

    def _update_routes(self, base_url: str) -> None:
        """Update routes."""
        routes: Dict = self._get_routes()
        [setattr(self, attr, f"{base_url}/{routes[attr]}/") for attr in routes]
        setattr(self, 'AUTH', self.AUTH.rstrip('/'))  # Strange hive behavior with auth url
        return None

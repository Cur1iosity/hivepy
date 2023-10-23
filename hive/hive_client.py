from typing import TypeVar

from hive.lib.enums import ObjectType
from hive.lib.meta import wrap
from hive.lib.rest.base_client import BaseHiveClient

T = TypeVar('T', bound='HiveObject')


class Hive(BaseHiveClient):
    """Hive client."""
    @wrap(ObjectType.PROJECT, many=True)
    def get_projects(self) -> T:
        """Get projects."""
        return self.http_client.get(self.route.PROJECT)

    @wrap(ObjectType.PROJECT)
    def get_project(self, project_id: str) -> T:
        """Get project."""
        return self.http_client.get(f'{self.route.PROJECT}/{project_id}')

    @wrap(ObjectType.ISSUE, many=True)
    def get_issues(self, project_id: str, offset: int = 0, limit: int = -1) -> T:
        """Get project vulnerabilities."""
        kwargs = {'json': {}, 'params': {"offset": offset, "limit": limit}}
        return self.http_client.post(f'{self.route.PROJECT}/{project_id}/graph/issue_list', **kwargs).get('items')

    def update_issue(self, project_id: str, issue_id: str, **kwargs) -> T:
        """Update issue."""
        return self.http_client.patch(f'{self.route.PROJECT}/{project_id}/graph/issues/{issue_id}', json=kwargs)

    def get_file(self, project_id: str,  file_id: str) -> bytes:
        """Get file."""
        return self.http_client.get(f"{self.route.PROJECT}/{project_id}/graph/file/{file_id}")

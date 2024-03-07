from typing import TypeVar, List

# from hivepy.lib.enums import ObjectType
# from hivepy.lib.meta import wrap
from hivepy.lib.rest.base_client import BaseHiveClient

T = TypeVar('T', bound='HiveObject')


class Hive(BaseHiveClient):
    """Hive client."""

    # @wrap(ObjectType.GROUP, many=True)
    def get_groups(self) -> T:
        """Get project groups."""
        return self.http_client.get(self.router.GROUPS)

    def get_group(self, project_group_id: str) -> T:
        """Get project group."""
        return self.http_client.get(f'{self.router.GROUP}/{project_group_id}')

    def get_project_templates(self) -> T:
        """Get project templates."""
        return self.http_client.get(self.router.PROJECT_TEMPLATES)

    def get_project_template(self, template_id: str) -> T:
        """Get project template."""
        return self.http_client.get(f'{self.router.PROJECT_TEMPLATE}/{template_id}/')

    def get_projects(self) -> T:
        """Get group projects."""
        return self.http_client.get(self.router.PROJECTS)

    def get_project(self, project_id: str) -> T:
        """Get project."""
        return self.http_client.get(f'{self.router.PROJECT}/{project_id}')

    def get_issue_schemes(self) -> T:
        """Get issue scheme."""
        return self.http_client.get(self.router.ISSUE_SCHEMES)

    def get_issue_scheme(self, scheme_id: str) -> T:
        """Get issue scheme."""
        return self.http_client.get(f'{self.router.ISSUE_SCHEME}/{scheme_id}/')

    # @wrap(ObjectType.PROJECT_TEMPLATE, many=True)
    # def get_project_templates(self) -> T:
    #     """Get project templates."""
    #     return self.http_client.get(self.route.PROJECT_TEMPLATE)
    #
    # @wrap(ObjectType.PROJECT, many=True)
    # def get_projects(self) -> T:
    #     """Get projects."""
    #     return self.http_client.get(self.route.PROJECT)
    #
    # @wrap(ObjectType.PROJECT)
    # def get_project(self, project_id: str) -> T:
    #     """Get project."""
    #     return self.http_client.get(f'{self.route.PROJECT}/{project_id}')
    #
    # @wrap(ObjectType.ISSUE, many=True)
    # def get_issues(self, project_id: str) -> T:
    #     """Get project vulnerabilities."""
    #     kwargs = {'json': {}}
    #     return self.http_client.post(f'{self.route.PROJECT}/{project_id}/graph/issue_list', **kwargs).get('items')
    #
    # def update_issue(self, project_id: str, issue_id: str, **kwargs) -> T:
    #     """Update issue."""
    #     return self.http_client.patch(f'{self.route.PROJECT}/{project_id}/graph/issues/{issue_id}', json=kwargs)
    #
    # def get_file(self, project_id: str,  file_id: str) -> bytes:
    #     """Get file."""
    #     return self.http_client.get(f"{self.route.PROJECT}/{project_id}/graph/file/{file_id}")

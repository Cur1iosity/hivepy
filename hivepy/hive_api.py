import uuid
from typing import Optional, Dict, Self, List, Union

from hivepy.api_management.enums import ClientMode, ObjectType
from hivepy.api_management.mode_handler import ModeHandler
from hivepy.api_management.object_builder import Builder as ObjectBuilder
from hivepy.issue_management.issue import Issue
from hivepy.project_management.project import Project
from hivepy.rest import State, exceptions
from hivepy.middleware.hive_middleware import HiveMiddleware


@ModeHandler
class HiveApi:
    def __init__(self, mode=ClientMode.OBJECT, **kwargs) -> None:
        """Initialize HiveApi."""
        self.state: State = State.NOT_CONNECTED
        self.base_url: Optional[str] = None

        self.client: HiveMiddleware = HiveMiddleware()
        self.builder: ObjectBuilder = ObjectBuilder()
        self.mode: ClientMode = mode

        if kwargs:
            self.connect(**kwargs)

    def authenticate(self, username: str, password: str) -> None:
        """Authenticate in Hive."""
        response = self.client.session.post(f"{self.base_url}/session", json={
            'userLogin': username,
            'userPassword': password,
        })

        if not (cookie := response.cookies.get('BSESSIONID')):
            raise exceptions.RestConnectionError('Could not get authentication cookie. Something wrong with credentials'
                                                 ' or server.')
        self.client.add_headers({'Cookie': f'BSESSIONID={cookie}'})
        self.state = State.CONNECTED

    @staticmethod
    def create_base_url(url: str, port: Optional[int] = None) -> str:
        """Create base URL from server and port."""
        proto, hostname, *str_port = url.split(':')

        if not proto:
            raise exceptions.ServerUrlNotDefinedError('Protocol not defined in server URL.')

        if str_port:
            port = int(str_port[0])
            url = f'{proto}://{hostname}'

        if url.startswith('https') and not port:
            port = 443
        elif url.startswith('http') and not port:
            port = 80

        return f'{url.strip("/")}:{port}/api'

    def connect(self,
                url: str,
                username: str,
                password: str,
                port: Optional[int] = None,
                verify: bool = True,
                proxies: Optional[Dict] = None,
                proxy: Optional[str] = None,
                mode: Optional[ClientMode] = None,
                **kwargs,
                ) -> Self:
        """Connect to Hive."""
        self.base_url = self.create_base_url(url, port)
        if mode:
            self.mode = mode
        if proxies:
            self.client.update_params(proxies=proxies)
        if proxy:
            self.client.update_params(proxies={'http': proxy, 'https': proxy})
        if verify is False:
            self.client.update_params(verify=False)
        if cert := kwargs.get('cert'):
            self.client.update_params(cert=cert)
        self.authenticate(username, password)
        return self

    def get_session(self) -> Dict:
        """Get session information."""
        response = self.client.get(f'{self.base_url}/session')
        return response

    def get_session_token(self) -> str:
        """Get session token."""
        if self.state != State.CONNECTED:
            raise exceptions.RestConnectionError('Not connected to server.')
        return self.client.session.cookies.get("BSESSIONID")

    def set_session(self, token: str) -> None:
        """Set session token."""
        self.client.session.cookies.update({'BSESSIONID': token})

    def get_licence(self) -> Dict:
        """Get licence information."""
        response = self.client.get(f'{self.base_url}/licence')
        return response

    def get_users(self) -> List[Dict]:
        """Get all users."""
        response = self.client.get(f'{self.base_url}/user')
        return response

    def get_groups(self) -> Dict:
        """Get all groups."""
        response = self.client.get(f'{self.base_url}/groups')
        return response

    @ModeHandler.deserialize(to=ObjectType.PROJECT)
    def get_projects(self, **params) -> Union[List[Project], List[Dict]]:
        """Get all projects."""
        return self.client.post(f'{self.base_url}/project/filter', params=params)

    @ModeHandler.deserialize(to=ObjectType.PROJECT)
    def get_project(self, project_id: Union[str, uuid.UUID]) -> Union[Dict, Project]:
        """Get project by ID."""
        return self.client.get(f'{self.base_url}/project/{project_id}')

    def get_project_templates(self, **params) -> Dict:
        """Get all project templates."""
        return self.client.get(f'{self.base_url}/project/templates', params=params)

    def get_project_custom_fields(self) -> List[Dict]:
        """Get all project custom fields."""
        return self.client.get(f'{self.base_url}/project/schema/accessible/fields')

    @ModeHandler.deserialize(to=ObjectType.ISSUE)
    def get_issue(self, project_id: Union[str, uuid.UUID], issue_id: Union[str, uuid.UUID]) -> Union[Dict, Issue]:
        """Get issue by ID."""
        return self.client.get(f'{self.base_url}/project/{project_id}/graph/issues/{issue_id}')

    @ModeHandler.deserialize(to=ObjectType.ISSUE)
    def get_issues(self, project_id: str, offset: int = 0, limit: int = 100) -> Union[List[Issue], List[Dict]]:
        return self.client.post(
            url=f'{self.base_url}/project/{project_id}/graph/issue_list?offset={offset}&limit={limit}',
            json={})

    def get_file(self, project_id: str, file_id: str) -> bytes:
        return self.client.get(f'{self.base_url}/project/{project_id}/graph/file/{file_id}')

    def get_issues_schemas(self) -> List[Dict]:
        """Get all issues schemes."""
        response = self.client.get(f'{self.base_url}/customization/issues')
        return response

    def get_project_issue_scheme(self, project_id: Union[str, uuid.UUID]) -> Dict:
        """Get project issue scheme."""
        response = self.client.get(f'{self.base_url}/project/{project_id}/settings/issues')
        return response

    def get_project_issue(self, project_id: Union[str, uuid.UUID], issue_id: Union[str, uuid.UUID]) -> Dict:
        """Get project issue."""
        response = self.client.get(f'{self.base_url}/project/{project_id}/graph/issues/{issue_id}')
        return response

    def get_project_tasks(self, project_id: Union[str, uuid.UUID], **params) -> Dict:
        """Get project tasks."""
        response = self.client.post(f'{self.base_url}/project/{project_id}/tasks', params=params)
        return response

    def get_project_issue_sources(self, project_id: Union[str, uuid.UUID]) -> List[Dict]:
        """Get project issue sources."""
        response = self.client.get(f'{self.base_url}/project/{project_id}/graph/issues/sources')
        return response

    def get_project_issue_statuses(self, project_id: Union[str, uuid.UUID]) -> List[Dict]:
        """Get project issue statuses."""
        response = self.client.get(f'{self.base_url}/project/{project_id}/settings/issues/statuses')
        return response

    def get_project_checklists(self, project_id: Union[str, uuid.UUID]) -> List[Dict]:
        """Get project checklists."""
        response = self.client.get(f'{self.base_url}/project/{project_id}/graph/checklist')
        return response

    def get_project_apps(self, project_id: Union[str, uuid.UUID]) -> List[Dict]:
        """Get project apps."""
        response = self.client.get(f'{self.base_url}/project/{project_id}/graph/apps')
        return response

    def get_project_credentials(self, project_id: Union[str, uuid.UUID]) -> List[Dict]:
        """Get project credentials."""
        response = self.client.get(f'{self.base_url}/project/{project_id}/graph/nodes/credentials ')
        return response

    def get_project_description(self, project_id: Union[str, uuid.UUID]) -> Dict:
        """Get project description."""
        response = self.client.get(f'{self.base_url}/project/{project_id}/description')
        return response

    def get_checklist_templates(self) -> List[Dict]:
        """Get all checklist templates."""
        response = self.client.get(f'{self.base_url}/templates/checklists')
        return response

    def get_issues_templates(self) -> List[Dict]:
        """Get all issues templates."""
        response = self.client.get(f'{self.base_url}/templates/issues')
        return response

    def update_project(self, project_id: Union[str, uuid.UUID], data: Dict) -> Dict:
        """Update project."""
        files = {k: (None, v) for k, v in data.items()}
        response = self.client.put(f'{self.base_url}/project/{project_id}', files=files)
        return response

    def update_issue(self, project_id: Union[str, uuid.UUID], issue_id: Union[str, uuid.UUID], data: Dict) -> Dict:
        """Update issue."""
        response = self.client.patch(f'{self.base_url}/project/{project_id}/graph/issues/{issue_id}',
                                     json=data)
        return response

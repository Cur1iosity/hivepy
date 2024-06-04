from typing import Dict, Union

from hivepy.api_management.enums import ObjectType
from hivepy.issue_management.issue import Issue
from hivepy.issue_management.issue_builder import IssueBuilder
from hivepy.project_management.project import Project
from hivepy.project_management.project_builder import ProjectBuilder
from hivepy.schema_management.factories import SchemaFactory
from hivepy.schema_management.models.issue_schema import IssueSchema


class Builder:
    """Class into which other object builders injected."""
    def __init__(self) -> None:
        """Initialize builder."""
        self.schema_factory: SchemaFactory = SchemaFactory()
        self.project_builder: ProjectBuilder = ProjectBuilder(self.schema_factory)
        self.issue_builder: IssueBuilder = IssueBuilder(self.schema_factory)

    def build_project(self, project_data: dict) -> Project:
        """Build project."""
        return self.project_builder.build(project_data)

    def build_issue(self, issue_schema: IssueSchema, issue_data: Dict) -> Issue:
        """Build issue."""
        return self.issue_builder.build(issue_schema, issue_data)

    def build(self, object_type: ObjectType, *args, **kwargs):
        """Build object."""
        if object_type == ObjectType.PROJECT:
            return self.build_project(*args, **kwargs)
        if object_type == ObjectType.ISSUE:
            return self.build_issue(*args, **kwargs)

    def get_project_builder(self) -> ProjectBuilder:
        """Get project builder."""
        return self.project_builder

    def get_issue_builder(self) -> IssueBuilder:
        """Get issue builder."""
        return self.issue_builder

    def __call__(self, *args, **kwargs) -> Union[Issue, Project]:
        """Call."""
        return self.build(*args, **kwargs)

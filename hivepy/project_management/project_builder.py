from typing import Dict

import pydantic

from hivepy.project_management.project import Project
from hivepy.schema_management.builders.project_schema_builder import ProjectSchemaBuilder
from hivepy.schema_management.models.project_schema import ProjectSchema


class ProjectBuilder:
    """Project builder class."""
    def __init__(self, project_schema_builder=None) -> None:
        """Initialize the project builder with a template builder."""
        self.project_schema_builder: ProjectSchemaBuilder = project_schema_builder if project_schema_builder \
            else self.create_project_schema_builder()

    @staticmethod
    def create_project_schema_builder() -> ProjectSchemaBuilder:
        """Create a project schema builder."""
        return ProjectSchemaBuilder()

    def build(self, project_data: Dict) -> Project:
        """Build a project from the given project data."""
        data: Dict = project_data.pop('data', {})
        schema: Dict = project_data.pop('projectSchema', {})

        if schema and data:
            project_schema: ProjectSchema = self.project_schema_builder(schema)
            project_model = pydantic.create_model('Project',
                                                  **project_schema.model_dump(),
                                                  __base__=Project)
            return project_model(**data)
        else:
            return Project(**project_data)


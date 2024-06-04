from typing import Dict, Type, Optional, Any

import pydantic

from hivepy.project_management.project import Project
from hivepy.schema_management.factories.schema_factory import SchemaFactory
from hivepy.schema_management.models.project_schema import ProjectSchema


class ProjectBuilder:
    """Project builder class."""
    def __init__(self, schema_factory=None) -> None:
        """Initialize the project builder with a template builder."""
        self.schema_factory: SchemaFactory = schema_factory if schema_factory \
            else self.create_schema_factory()

    @staticmethod
    def create_schema_factory() -> SchemaFactory:
        """Create a project schema builder."""
        return SchemaFactory()

    def build(self, project_data: Dict) -> Project:
        """Build a project from the given project data."""
        data: Dict = project_data.pop('data', {})
        schema: Dict = project_data.pop('projectSchema', {})

        if schema and data:
            project_model = self.create_project_model(schema)
            return project_model(**data | project_data)
        else:
            return Project(**project_data)

    def create_project_model(self, schema: Dict) -> Type['Project']:
        """Create a project model from the given project schema."""
        project_schema: ProjectSchema = self.schema_factory.make_project_schema(schema)
        fields = project_schema.predefined_fields_settings + project_schema.additional_fields_settings
        schema_fields = {field.name: (Optional[Any], None) for field in fields}
        return pydantic.create_model('Project', **schema_fields, __base__=Project)

from typing import Dict

from hivepy.schema_management.factories.schema_factory import SchemaFactory
from hivepy.template_management.models.project_template import ProjectTemplate


class ProjectTemplateBuilder:
    """Project template builder. """

    def __init__(self, schema_factory) -> None:
        """Initiate project template builder."""
        self.schema_factory: SchemaFactory = schema_factory

    def build(self, project_data: Dict) -> ProjectTemplate:
        """Build project template."""
        project = project_data.copy()
        if schema := project.pop('projectSchema', {}):
            project['schema'] = self.schema_factory.make_project_schema(schema)
        return ProjectTemplate(**project)

    def __call__(self, project: Dict) -> ProjectTemplate:
        """Call. """
        return self.build(project)

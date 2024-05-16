from typing import Dict, Union, ForwardRef
from hivepy.models import BaseProject
from hivepy.builders.model_builder import ModelBuilder


class ProjectFactory:
    """Project factory."""
    model_builder: ModelBuilder = ModelBuilder()

    def create_project(self, project: Dict) -> Union['BaseProject', ForwardRef('Project')]:
        """Get project."""
        if not (schema := project.pop('projectSchema', {})):
            """If project is default, return BaseProject."""
            return BaseProject(**project)

        data = project.pop('data', {})

        model = self.model_builder(schema)
        project_object: model = model(**project)

        for key, value in data.items():
            field = getattr(project_object, key)
            field.value = value
        return project_object

    def __call__(self, project: Dict) -> Union['BaseProject', ForwardRef('Project')]:
        """Call create_project."""
        return self.create_project(project)

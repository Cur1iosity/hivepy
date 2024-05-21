from typing import Type, Dict

import pydantic

from hivepy.models import BaseProject, ProjectSchema, Field


class ModelBuilder:
    """Model builder."""
    def __init__(self) -> None:
        """Initialize ModelBuilder."""
        self.base_project_model: Type[BaseProject] = BaseProject
        self.schema_builder: ... = ...

    @classmethod
    def build_project_schema(cls, _schema: Dict) -> ProjectSchema:
        """Build project schema."""
        return ProjectSchema(**_schema)

    def build_project_model(self, _schema: Dict) -> Type[BaseProject]:
        """Build extra fields."""
        schema: ProjectSchema = self.build_project_schema(_schema)
        extra_fields = {field.name: (Field, field) for field in schema.additional_fields_settings}
        extra_fields |= {'project_schema': (ProjectSchema, schema)}

        model: Type[BaseProject] = pydantic.create_model(
            'Project',
            **extra_fields,
            __base__=self.base_project_model
        )
        return model

    def __call__(self, _schema: Dict) -> Type[BaseProject]:
        """Build model."""
        try:
            return self.build_project_model(_schema)
        except Exception as e:
            raise e

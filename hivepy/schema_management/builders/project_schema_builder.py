from hivepy.field_management import FieldBuilder
from hivepy.schema_management.models import ProjectSchema


class ProjectSchemaBuilder:
    """Class that builds a ProjectSchema object from a raw project schema dictionary."""
    field_builder = FieldBuilder()

    @classmethod
    def build(cls, project_schema: dict) -> ProjectSchema:
        """Build ProjectSchema object from raw data."""
        data = project_schema.copy()
        raw_fields = data.pop('additionalFieldsSettings', [])
        data['additionalFieldsSettings'] = [cls.field_builder.build(field) for field in raw_fields]
        return ProjectSchema(**data)

    def __call__(self, project_schema: dict) -> ProjectSchema:
        """Build ProjectSchema object from raw data."""
        return self.build(project_schema)

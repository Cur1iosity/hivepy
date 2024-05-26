from typing import Dict, ForwardRef, Callable

from hivepy.schema_management.builders.schema_builder import SchemaBuilder

Schema = ForwardRef('Schema')


def caching(func) -> Callable:
    """Caching decorator."""
    def wrapper(self, schema_type: str, schema: Dict) -> Schema:
        """Wrapper."""
        schema_id_version: str = f"{schema.get('id')}_{schema.get('version')}"
        if schema_id_version not in self.cache:
            self.cache[schema_id_version] = func(self, schema_type, schema)
        return self.cache[schema_id_version]
    return wrapper


class SchemaFactory:
    """Schema factory class."""
    def __init__(self):
        self.cache: Dict = {}  # {'schema_id_version': 'schema': Schema}
        self.schema_builder: SchemaBuilder = SchemaBuilder()

    @caching
    def make_schema(self, schema_type: str, schema: Dict) -> Schema:
        """Make schema."""
        return self.schema_builder(schema_type, schema)

    def make_issue_schema(self, schema: Dict) -> Schema:
        """Make issue schema."""
        return self.schema_builder('issue', schema)

    def make_project_schema(self, schema: Dict) -> Schema:
        """Make project schema."""
        return self.schema_builder('project', schema)

    def __call__(self, schema_type: str, schema: Dict) -> Schema:
        """Call."""
        return self.make_schema(schema_type, schema)

from typing import Dict, Type, List

from hivepy import builders


class ModelManager:
    """Model manager."""
    def __init__(self) -> None:
        self.model_cache: List = []
        self.model_builder: builders.ModelBuilder = builders.ModelBuilder()
        self.field_builder: builders.PydanticFieldBuilder = builders.PydanticFieldBuilder()

    def get_model_from_cache(self, schema_id: str, version: str) -> Type:
        """Get model from cache."""
        return next((model for model in self.model_cache
                     if model.schema.id == schema_id
                     and model.schema.version == version), None)

    def add_model(self, model: Type) -> None:
        """Add model to cache."""
        self.model_cache.append(model)

    def build_model(self, schema: Dict) -> Type:
        """Build model."""
        return self.model_builder(schema)

    def get_model(self, schema: Dict) -> Type:
        """Get model."""
        schema_id, version = schema['id'], schema['version']
        if not (model := self.get_model_from_cache(schema_id, version)):
            """If model not in cache, build model."""
            model = self.build_model(schema)
            self.add_model(model)
        return model

    def __call__(self, schema: Dict) -> Type:
        """Call get_model."""
        return self.get_model(schema)

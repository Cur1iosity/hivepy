from typing import Dict, ForwardRef

from hivepy.field_management.builder.field_model_builder import FieldModelBuilder
from hivepy.field_management.json_field_normalizer import JsonFieldNormalizer


class FieldBuilder:
    """Class that builds a Field object from a raw field dictionary."""
    def __init__(self) -> None:
        """Initialize FieldBuilder class."""
        self.field_model_builder = FieldModelBuilder()
        self.json_field_normalizer = JsonFieldNormalizer()

    def build(self, field: Dict) -> ForwardRef('Field'):
        """Make from BaseField object advanced Field model."""
        field = self.json_field_normalizer(field)
        model = self.field_model_builder(field)
        return model(**field)

    def __call__(self, field: Dict) -> ForwardRef('Field'):
        """Make from BaseField object advanced Field model."""
        return self.build(field)

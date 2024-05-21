from typing import Dict, ForwardRef

from hivepy.field_management.builder.field_model_builder import FieldModelBuilder


class FieldBuilder:
    """Class that builds a Field object from a raw field dictionary."""
    def __init__(self) -> None:
        """Initialize FieldBuilder class."""
        self.field_model_builder = FieldModelBuilder()

    def build(self, base_field: Dict) -> ForwardRef('Field'):
        """Make from BaseField object advanced Field model."""
        model = self.field_model_builder(base_field)
        return model(**base_field)

from typing import Dict

from hivepy.field_management.models.base_field import BaseField


class JsonFieldNormalizer:
    """Class that reshape raw field dictionary into BaseField dictionary."""
    @classmethod
    def build(cls, raw_field: Dict) -> Dict:
        """Build BaseField dictionary."""
        return BaseField(**raw_field).model_dump()

    def __call__(self, *args, **kwargs) -> Dict:
        """Call build."""
        return self.build(args[0] if args else kwargs)

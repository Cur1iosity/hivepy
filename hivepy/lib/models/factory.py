from typing import Type, Any, List
from hivepy.lib import models

objects = [obj for name, obj in vars(models).items() if isinstance(obj, type)]
object_mapper = {x.__name__: x for x in objects}


class Factory:
    """Factory that creates items."""
    @staticmethod
    def create_instance(class_type: Type, **kwargs) -> Any:
        """Create instance of class."""
        return class_type(**kwargs)

    def get_model_field_names(self, class_name: str) -> List[str]:
        """Get model field names."""
        return [x for x in set(self.get_attributes(class_name) + self.get_aliases(class_name)) if x]

    @staticmethod
    def get_attributes(class_name: str) -> List[str]:
        """Get attributes of class."""
        try:
            return list(object_mapper.get(camel_case(class_name)).model_fields.keys())
        except AttributeError:
            raise ModelNotFoundError(class_name)

    @staticmethod
    def get_aliases(class_name: str) -> List[str]:
        """Get aliases of class."""
        try:
            return [value.alias for value in object_mapper.get(camel_case(class_name)).model_fields.values()]
        except AttributeError:
            raise ModelNotFoundError(class_name)

    def __call__(self, class_name: str, **kwargs) -> Any:
        """Call creating instance of class."""
        try:
            class_type = object_mapper.get(camel_case(class_name))
            return self.create_instance(class_type, **kwargs)
        except TypeError:
            raise ModelNotFoundError(class_name)


class FactoryError(Exception):
    """Factory error."""
    def __init__(self, message: str = ''):
        self.message = message


class ModelNotFoundError(FactoryError):
    """Model not found error."""
    def __init__(self, message: str = ''):
        super().__init__(message=f"Model '{message}' not found. Check __init__.py in models package")


def camel_case(snake_str: str) -> str:
    """Convert snake string to camel string."""
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)

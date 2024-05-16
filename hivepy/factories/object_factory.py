from typing import Dict, Any

from hivepy.enums import ObjectType
from hivepy.factories.project_factory import ProjectFactory


class ObjectFactory:
    project_factory: ProjectFactory = ProjectFactory()

    def __init__(self) -> None:
        """Initialize factory."""
        self.factories: Dict = {
            ObjectType.PROJECT: self.project_factory
        }

    def get_object(self, object_type: ObjectType, object_data: Dict) -> Any:
        """Get object."""
        return self.factories[object_type](object_data)

    def __call__(self, object_type: ObjectType, object_data: Dict) -> Any:
        """Call get_object."""
        return self.get_object(object_type, object_data)

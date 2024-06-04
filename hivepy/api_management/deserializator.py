from typing import Type, Optional, Callable, ForwardRef

from hivepy.api_management.enums import ClientMode, ObjectType

HiveApi = ForwardRef('HiveApi')


class ModeHandler:
    """
    Class wrapper for HiveApi.
    If mode is set to JSON, response will be returned as is.
    If mode is set to RAW_ITEMS, response will be returned as list of items or raw item if only one.
    If mode is set to OBJECT, response will be deserialized to object using provided ObjectType.
    """
    def __init__(self, hive_cls) -> None:
        """Initialize mode handler."""
        self._hive_cls: Type['HiveApi'] = hive_cls
        self._instance: Optional['HiveApi'] = None

    def __call__(self, *args, **kwargs) -> HiveApi:
        """Call wrapped class."""
        if not self._instance:
            self._instance = self._hive_cls(*args, **kwargs)
            self._builder = self._instance.builder
        return self._instance

    def __getattr__(self, name: str) -> HiveApi:
        """Get attribute from wrapped class."""
        return getattr(self._instance, name)

    @staticmethod
    def deserialize(to: ObjectType) -> Callable:
        """Deserialize response to object."""
        def decorator(method) -> Callable:
            """Decorator."""
            def wrapper(self, *args, **kwargs):
                """Wrapper."""
                result = method(self, *args, **kwargs)
                if self.mode == ClientMode.JSON:
                    return result

                if hasattr(result, 'get'):  # Response is a dict
                    result = result.get('items', result)    # Get items from Dict
                if self.mode == ClientMode.RAW_ITEMS:
                    return result  # Return list of items or raw item if only one

                if self.mode == ClientMode.OBJECT:
                    if hasattr(result, 'append'):
                        return [self._builder.build(to, item) for item in result]
                    return self.builder.build(to, result)
            return wrapper
        return decorator

from typing import List, Union, Callable
from hivepy.lib.enums import ObjectType
from hivepy.lib.models.factory import Factory
import functools

factory = Factory()


def wrap(to_object: ObjectType, many: bool = False) -> Callable:
    """Wrap function to convert response to object."""
    def decorator(func) -> Callable:
        @functools.wraps(func)
        def wrapper(instance, *args, **kwargs) -> Union[List[ObjectType], ObjectType]:
            if many:
                return [factory(to_object, **x) for x in func(instance, *args, **kwargs)]
            else:
                return factory(to_object, **func(instance, *args, **kwargs))
        return wrapper
    return decorator


def json(func):
    """Wrap function to convert response to json."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Union[List[dict], dict]:
        return func(*args, **kwargs).json()
    return wrapper


def content(func):
    """Wrap function to convert response to content."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Union[List[dict], dict]:
        return func(*args, **kwargs).content
    return wrapper

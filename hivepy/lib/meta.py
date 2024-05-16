from typing import List, Union, Callable
from hivepy.enums import ObjectType
from hivepy.models import Factory
import functools

factory = Factory()


def switchover(limit: int = 100) -> Callable:
    """Switch simple loader to batch if limit is exceeded."""
    def decorator(func) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Union[List[ObjectType], ObjectType]:
            response = func(*args, **kwargs)
            count: int = response.get('totalCount', 0)
            return batch_load(limit)(*args, **kwargs) if count > limit else response
        return wrapper
    return decorator


@switchover()
def load(func) -> Callable:
    """Wrap function to convert response to object."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Union[List[ObjectType], ObjectType]:
        return func(*args, **kwargs)
    return wrapper


def batch_load(limit: int = 100) -> Callable:
    """Wrap function to convert response to object."""
    def decorator(func) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Union[List[ObjectType], ObjectType]:
            offset: int = 0
            items: List[ObjectType] = []
            while True:
                response = func(*args, offset=offset, limit=limit, **kwargs)
                items.extend(response.get('items', []))
                offset += limit
                if len(items) >= response.get('totalCount', 0):
                    break
            return items
        return wrapper
    return decorator


def wrap(to_object: ObjectType, many: bool = False) -> Callable:
    """Wrap function to convert response to object."""
    def decorator(func) -> Callable:
        @functools.wraps(func)
        def wrapper(instance, *args, **kwargs) -> Union[List[ObjectType], ObjectType]:
            if many:
                return [factory(to_object, **x) for x in load(func)(instance, *args, **kwargs)]
                # return [factory(to_object, **x) for x in func(instance, *args, **kwargs)]
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

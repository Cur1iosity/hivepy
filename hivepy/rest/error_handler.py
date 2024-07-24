import functools
import json
from typing import Callable, Any

from hivepy.rest import exceptions
from hivepy.rest.http_client.exceptions import ClientError


def method_decorator(func) -> Callable:
    """Decorator for methods."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """Wrapper for methods."""
        try:
            result = func(*args, **kwargs)
        except ClientError as e:
            error = json.loads(e.content)
            raise exceptions.HiveRestError(error)
        return result
    return wrapper


def ErrorHandler(cls) -> Any:
    """Decorator for classes."""
    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        # Обернуть все методы экземпляра, кроме __init__
        for attr_name in dir(self):
            if not attr_name.startswith("__"):  # Игнорируем служебные методы
                attr_value = getattr(self, attr_name)
                if callable(attr_value):
                    decorated_attr = method_decorator(attr_value)
                    setattr(self, attr_name, decorated_attr)

    cls.__init__ = new_init
    return cls

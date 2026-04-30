from functools import wraps
from datetime import datetime
from typing import Callable
import inspect


ALLOWED_LEVELS = ("INFO", "DEBUG", "ERROR")


def _prepare_level(level: str) -> str:
    level = level.upper()

    if level not in ALLOWED_LEVELS:
        raise ValueError(f"Unknown log level: {level}")

    return level


def _log_start(level: str, timestamp: str, func_name: str, args, kwargs):
    if level == "ERROR":
        return

    print(f"[{timestamp}] [{level}] Calling {func_name}")

    if level == "DEBUG":
        print(f"  Args: {args}")
        print(f"  Kwargs: {kwargs}")


def _log_result(level: str, timestamp: str, func_name: str, result):
    if level == "ERROR":
        return

    print(f"[{timestamp}] [{level}] {func_name} returned: {result}")


def _log_error(timestamp: str, func_name: str, error: Exception):
    print(f"[{timestamp}] [ERROR] {func_name} raised: {type(error).__name__}: {error}")


def log(level: str = "INFO"):
    """
    Logging decorator with configurable log level.

    Args:
        level: Log level (INFO, DEBUG, ERROR)

    Usage:
        @log(level="INFO")
        def my_function(x, y):
            return x + y
    """
    level = _prepare_level(level)

    def decorator(func: Callable):
        if inspect.iscoroutinefunction(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                timestamp = datetime.utcnow().isoformat()
                func_name = func.__name__

                _log_start(level, timestamp, func_name, args, kwargs)

                try:
                    result = await func(*args, **kwargs)

                    _log_result(level, timestamp, func_name, result)

                    return result

                except Exception as e:
                    _log_error(timestamp, func_name, e)
                    raise

            return async_wrapper

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            timestamp = datetime.utcnow().isoformat()
            func_name = func.__name__

            _log_start(level, timestamp, func_name, args, kwargs)

            try:
                result = func(*args, **kwargs)

                _log_result(level, timestamp, func_name, result)

                return result

            except Exception as e:
                _log_error(timestamp, func_name, e)
                raise

        return sync_wrapper
    return decorator

from functools import wraps
from datetime import datetime
from typing import Callable


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
    
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.utcnow().isoformat()
            func_name = func.__name__
            
            print(f"[{timestamp}] [{level}] Calling {func_name}")
            print(f"  Args: {args}")
            print(f"  Kwargs: {kwargs}")
            
            try:
                result = func(*args, **kwargs)
                
                print(f"[{timestamp}] [{level}] {func_name} returned: {result}")
                
                return result
                
            except Exception as e:
                print(f"[{timestamp}] [ERROR] {func_name} raised: {type(e).__name__}: {e}")
                raise
        
        return wrapper
    return decorator
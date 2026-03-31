import time
from typing import Callable, List, Any

def async_map_callback(arr: List[Any], transform: Callable, callback: Callable):
    """
    Callback-based async map.

    Args:
        arr: Input array
        transform: Transformation function
        callback: Callback function(error, result)
    """
    results = []

    try:
        for item in arr:
            result = transform(item)
            results.append(result)

        callback(None, results)
    except Exception as e:
        callback(e, None)


async_map_promise = None
async_map = None
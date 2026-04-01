import time
import asyncio
from typing import Callable, List, Any
from concurrent.futures import ThreadPoolExecutor

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


def async_map_promise(arr: List[Any], transform: Callable):
    """
    Promise-based async map using ThreadPoolExecutor.

    Returns:
        Future object that resolves to results
    """
    executor = ThreadPoolExecutor()

    def run():
        return [transform(item) for item in arr]
    
    return executor.submit(run)


async def async_map(arr: List[Any], transform: Callable):
    """
    Async/await version of map.

    Args:
        arr: Input array
        transform: Transformation function (can be async)
    
    Returns:
        List of transformed items
    """
    results = []

    for item in arr:
        if asyncio.iscoroutinefunction(transform):
            result = await transform(item)
        else:
            result = transform(item)
        results.append(result)

    return results
from collections import OrderedDict

def memoize(func=None, max_size=None):
    def decorator(f):
        cache = OrderedDict()

        def wrapper(*args):
            if args in cache:
                cache.move_to_end(args)
                return cache[args]
            
            result = f(*args)
            cache[args] = result

            if max_size and len(cache) > max_size:
                cache.popitem(last=False)

            return result
        
        return wrapper
    if func is None:
        return decorator
    else:
        return decorator(func)
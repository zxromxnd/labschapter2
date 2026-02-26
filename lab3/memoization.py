from collections import OrderedDict

def memoize(func=None, max_size=None, strategy='lru'):
    def decorator(f):
        cache = OrderedDict()
        frequency = {}

        def wrapper(*args):
            if args in cache:
                if strategy == 'lru':
                    cache.move_to_end(args)
                elif strategy == 'lfu':
                    frequency[args] += 1
                return cache[args]
            
            result = f(*args)
            cache[args] = result

            if strategy == 'lfu':
                frequency[args] = 1

            if max_size and len(cache) > max_size:
                if strategy == 'lru':
                    cache.popitem(last=False)
                elif strategy == 'lfu':
                    lfu_key = min(frequency, key=frequency.get)
                    del cache[lfu_key]
                    del frequency[lfu_key]

            return result
        return wrapper
    if func is None:
        return decorator
    else:
        return decorator(func)
                
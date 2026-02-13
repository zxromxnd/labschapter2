def incremental_counter(start=1):
    current = start
    while True:
        yield current
        current += 1
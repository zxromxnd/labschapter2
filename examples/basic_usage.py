from lab1.generators import incremental_counter, timeout_iterator

print("example 1: its basic usage")
print("running counter for 3 seconds..\n")

gen = incremental_counter()
timeout_iterator(gen, 3)

print("\ndone.")
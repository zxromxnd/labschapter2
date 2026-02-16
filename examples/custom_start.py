from lab1.generators import incremental_counter, timeout_iterator

print("example 2: custom starting number")
print("starting from 100, running for 2 seconds..\n")

gen = incremental_counter(100)
timeout_iterator(gen, 2)

print("\ndone.")
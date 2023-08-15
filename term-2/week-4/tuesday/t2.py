import time

start_time = time.time()

# write your code below this
roll_number = tuple(range(1,300)) # O(1) -> 0.000003, 0.00003

for r in roll_number: # n = 20
    print(f"Hi from O(n) we have roll number {r} \n") # O(1) * 20


# finish your code above this

# 21 * O(1)
# 31 * O(1)
# 1001 * O(1)
# (n + 1) * O(1) = N * O(1) + O(1) = (N + 1)

end_time = time.time()


print(f"Total time in seconds takes {end_time - start_time}")

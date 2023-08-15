import time

start_time = time.time()

# write your code below this
nums1 = tuple(range(1,1000))
nums2 = tuple(range(1,100))

for n in nums1: # n = 1000
    for m in nums2: # n = 1000
        print(n * m) # n * n


# finish your code above this

# (n2 + 1) * O(1) = N2 * O(1) + O(1) = (N2 + 1) => N * M

end_time = time.time()


print(f"Total time in seconds takes {end_time - start_time}")

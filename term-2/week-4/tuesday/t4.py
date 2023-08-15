import time

start_time = time.time()

# binary searching -> best real examples <- DB -> 1,2,3,4,5,
num = list(range(1,11))

searching = 7
# write your code below this
first = 0
last = len(num)

while True:
    mid = (first + last) // 2

    if searching > num[mid]:
        first = mid
    elif searching < num[mid]:
        last = mid
    else:
        print(f"found it in position {mid}")
        break
    

# [1,...10] # 10
# [1...5][6..10] # 5
# 2

# O(log2N)


# finish your code above this

end_time = time.time()


print(f"Total time in seconds takes {end_time - start_time}")

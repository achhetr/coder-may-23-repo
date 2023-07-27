# 100th prime number
# import time

# start_time = time.time()

# write a function which checks prime number
def is_prime(n):
    # iterate the from 1 to n
    for i in range(2, (n // 2 + 1)): # sqrt(n) + 1
        # check and return false when remainder is 0
        if n % i == 0:
            # return false if the remainder is 0
            return False

    # return true if the loop finishes
    return True

# write a function to get nth prime number
def get_nth_prime(nth):
    # save a variable with a value 100
    nth_prime = 1
    current = 2

    # iterate or loop for 100th time
    while True:
        current += 1

        # check for a prime
        if is_prime(current):
            nth_prime += 1

        # check whether the prime is 100th number
        if nth_prime == nth:
            # print
            print(f"{nth}th prime number is {current}")
            break


nth_prime = 101
# get_nth_prime(10000)

# end_time = time.time()

# print(f"Total time taken for nth prime is {end_time - start_time} seconds")

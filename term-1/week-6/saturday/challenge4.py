# calculate Factorial

# 5 -> 5 * 4 * 3 * 2 * 1
# integer
# positive

n = 10
factorial = 1
# for i in range(1, n + 1):
#     factorial *= i

num = n
while num >= 0:
    if num == 0:
        factorial *= 1
        break
    else:
        factorial *= num
        num -= 1

print("factorial of a number {} is {}".format(n, factorial))

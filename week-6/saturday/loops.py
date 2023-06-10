# why do we need loop

# iterate or iteration
# for i in range(100): # 100 times
#     print("hello")

# i = 0
# while True:
#     i += 1

#     if i == 100:
#         break

#     if i == 50:
#         continue

#     print("hello", i)


# bank account 100 dollar -> debit 10
# updated bank balance 90

# credit 10
# updated bank balance

# get balance

balance = 100

while True:
    bal = int(input("enter the value that needs to be credit or debit> "))

    print("Your current balance is ", balance)

    if bal == 0:
        continue

    if bal != 0:
        balance += bal
        
    print("Your updated balance is ", balance)

    if balance < 0:
        print("not sufficient balance exit")
        break

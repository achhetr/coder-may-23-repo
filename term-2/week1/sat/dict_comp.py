# newdict = {k: v for k, v in dictonary if condition == True}

num = {
    1: 1,
    2: 4,
    3: 9,
    4: 16
}

new_num = {k: str(v) + "a"  for k,v in num.items() if v % 2 == 0}
print(new_num)

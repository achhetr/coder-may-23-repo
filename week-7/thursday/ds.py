# list, tuple, dict and set


# list is a collection of data types
# ordered list
# mutuable type

[1,2,3,4] == [4,3,2,1]
[1,2,3,'a','b']

# last element of list -> list[length of an list - 1]

# tuple is collection of data types
# ordered tuple
# immutable

# performance reason
# tuple
b = 1,2


# sets
# collection of unique data types
a = {1,2,3}
b = {3,4,5}
a.union(b) # {1, 2, 3, 4, 5}
b.intersection(a) # {3}

# dict
# key -> str and value (collection of data types)
# unordered
user = {
    "name": "akash",
    "age": 55,
    "salary": 20
}
print(f"{user['name']} is {user['age']} years old and earns {user['salary']} an hour")

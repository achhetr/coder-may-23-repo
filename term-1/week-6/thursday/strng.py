# len(): Returns the length of a string.
# lower(): Converts a string to lowercase.
# upper(): Converts a string to uppercase.
# split(): Splits a string into a list of substrings based on a delimiter.
# join(): Concatenates a list of strings into a single string using a specified separator.

s = "George Zonnios" # <- database, csv, excel, pdf, apis or cloud

# len_s = len(s)
# print(s, "name has characters", len_s)

# automated system -> generate an email for you based on your name
# first_name = "Lukas"
# last_name = "Halloran"

# email = first_name + "." + last_name + "@billiondollarit.com"
# print(email.lower())
# print(email.upper())

names = s.split()
email = ".".join(names)
email += "@billiondollarit.com"
print(email.lower())

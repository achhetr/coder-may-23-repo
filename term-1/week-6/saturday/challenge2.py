# count the number of capital letters
sen = "Finance is the study and discipline of money, currency and capital assets. It is related to, but not synonymous with economics, which is the study of production, distribution, and consumption of money, assets, goods and services (the discipline of financial economics bridges the two). Finance activities take place in financial systems at various scopes, thus the field can be roughly divided into personal, corporate, and public finance.[a]"


count = 0
for c in sen:
    if c.isupper():
        count += 1

print("Total capital letters are", count)

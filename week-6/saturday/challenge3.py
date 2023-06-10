# remove spaces from string without inbuilt function

sen = "Finance is the study and discipline of money, currency and capital assets. It is related to, but not synonymous with economics, which is the study of production, distribution, and consumption of money, assets, goods and services (the discipline of financial economics bridges the two). Finance activities take place in financial systems at various scopes, thus the field can be roughly divided into personal, corporate, and public finance.[a]"


emp = 1

for c in sen:
    if c != " ":
        emp += c


print(emp)
print(sen.replace(" ", "") == emp)

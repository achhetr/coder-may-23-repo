# count vowels and consonants in the string

sen = "Finance is the study and discipline of money, currency and capital assets. It is related to, but not synonymous with economics, which is the study of production, distribution, and consumption of money, assets, goods and services (the discipline of financial economics bridges the two). Finance activities take place in financial systems at various scopes, thus the field can be roughly divided into personal, corporate, and public finance.[a]"

# identify what are vowels and consonant

# vowels (a,e,i,o,u)
# consonents (everything - vowels)

len_vowel = 0
len_consonant = 0
for c in sen:
    if c.lower() in ('a','e','i','o','u'):
        len_vowel += 1
    # elif c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ':
    #     pass
    # else:
    #     len_consonant += 1
    elif c.lower() in 'abcdefghijklmnopqrstuvwxyz':
        len_consonant += 1



print("number of vowels are", len_vowel)
print("number of consonants are", len_consonant)
print("number of total characters", len(sen))


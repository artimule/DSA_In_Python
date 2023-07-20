def nonrepeatingcharacter(s):
    #using hash table to store count
    c = [0 for i in range(256)]
    for i in s:
        c[ord(i)]+=1
    for i in range(len(s)):
        if c[ord(s[i])]==1:
            return s[i]
    return '$'
s='ashkdaks'
print(nonrepeatingcharacter(s))

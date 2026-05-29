# Pass - do nothing

str = "A, B, C, D"
str2= ''

for i in str :
    if i == ',' :
        pass
    else :
        str2 = str2 + i

print(str2)

'''
Output:
A B C D

'''
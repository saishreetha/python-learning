#Break

print("Enter an number: \n Enter z to exit :")

list =[]
while True :
    inp = input()
    if inp == 'z' :
#break - break the execution of the current block
        break

    list.append(int(inp))

print(list)

'''
Output:
Enter an number: 
Enter z to exit :
4
8
6
5
3
2
0
z
[4, 8, 6, 5, 3, 2, 0]

'''


#Continue

#Remove ',' from the string

str = "A, B, C, D, E, F, G"
str2= ''

for i in str :
    if i == ',' :
# Continue - continues to the next iteration
        continue
    str2 = str2 + i

print(str2)

'''
Output:
A B C D E F G

'''
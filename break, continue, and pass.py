print("Enter an number: \n Enter z to exit :")

list =[]
while True :
    inp = input()
    if inp == 'z' :
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
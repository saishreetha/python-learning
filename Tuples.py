# Tuples - Immutable - cannot be changed

tup = (2 , 3 , 4)
print(tup)

'''
tup[2] = 5 
print(tup)
( It will show error because Tuples cannot be changed , instead we can completely reassign them. )
The values cannot be changed individually.
'''

print(tup[1])
print(tup.index(2))

tup = (3,4,4,4,4,8,8,8,0,0,0,0,0,8,6,7,5,5,4,3,8)
print(tup.count(0))
print(tup.count(4))
print(tup.count(8))

for i in tup :
    print(i)

if 7 in tup :
    print("YES")

if 3 not in tup :
    print("NO")

if tup :
    print("Tup is not empty")

'''
Output :
(2, 3, 4)
3
0
5
5
5
3
4
4
4
4
8
8
8
0
0
0
0
0
8
6
7
5
5
4
3
8
YES
Tup is not empty

'''
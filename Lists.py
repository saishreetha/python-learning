cities = ["Chennai", "Madurai", "Trichy", "Coimbatore", "Salem"]
val = [22,87,39,67,55]
list1 = ["Chennai", 3, "Salem" , "Tirchy"]

print(cities[2])
print(cities[::2])
print(cities[::-1])
print(val)
print(list1[::4])
print(list1[::-2])
print(val[::-7])

#Modify

list1[3] = "Trichy"
print (list1)

#Append

cities.append ("Karur")
print(cities)

#Insert

cities.insert(3 ,"Thanjavur" )
print(cities)

#Removing using Del

del cities[3]
print(cities)

#Removing using pop()

delete = cities.pop(3)
print(delete + " has been deleted")
print(cities)

delete = cities.pop() #If they didn't give any index it will defaultly delete the last one.
print(delete + " has been deleted")
print(cities)

#Temoporary sort

print(sorted(cities))
print(sorted(val))
print(cities)

#Permanent sort

cities.sort()
print(cities)

#Rverse

cities.reverse()
print(cities)

#Length of a list

print(len(cities))


'''
Output :
Trichy
['Chennai', 'Trichy', 'Salem']
['Salem', 'Coimbatore', 'Trichy', 'Madurai', 'Chennai']
[22, 87, 39, 67, 55]
['Chennai']
['Tirchy', 3]
[55]
['Chennai', 3, 'Salem', 'Trichy']
['Chennai', 'Madurai', 'Trichy', 'Coimbatore', 'Salem', 'Karur']
['Chennai', 'Madurai', 'Trichy', 'Thanjavur', 'Coimbatore', 'Salem', 'Karur']
['Chennai', 'Madurai', 'Trichy', 'Coimbatore', 'Salem', 'Karur']
Coimbatore has been deleted
['Chennai', 'Madurai', 'Trichy', 'Salem', 'Karur']
Karur has been deleted
['Chennai', 'Madurai', 'Trichy', 'Salem']
['Chennai', 'Madurai', 'Salem', 'Trichy']
[22, 39, 55, 67, 87]
['Chennai', 'Madurai', 'Trichy', 'Salem']
['Chennai', 'Madurai', 'Salem', 'Trichy']
['Trichy', 'Salem', 'Madurai', 'Chennai']
4
'''
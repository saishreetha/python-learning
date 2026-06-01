n = 78

while True:

    if n % 20 == 0:
        print("Found it! The number is:", n)
        break
    n = n + 1


'''
Output :

Found it! The number is: 80

'''

str_ip = "34,5,2,8,9"
numbers_list = []

for character in str_ip:
    if character == ",":
        continue
    numbers_list.append(character)

print("The list of numbers is:", numbers_list)

'''
Output :

The list of numbers is: ['3', '4', '5', '2', '8', '9']
'''
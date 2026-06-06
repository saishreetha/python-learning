#Dictionary :
#Used to store key value pair

user = {'name' : 'Sai' , 'age' : '13' , 'gender' : 'female' , 'school' : 'Narayana e Techno'}

# Here, name , age , gender and school are called as " Key "
# Values are " 'Sai' , '13' , 'female' and 'Narayana e Techno' "
# We can easily retrieve the values from the key
# Example :

print(user['name'])
print(user['age'])
print(user)

# Adding a New Key value pair :

user['city'] = 'Chennai'
print(user)

# Modify :

user['city'] = 'Coimbatore'
print(user)

# Delete :

del user ['gender']
print(user)

# Looping :

for key , val in user.items() :
    print("Key : " + key)
    print("Val : " + str(val))

for key in user.keys():
    print(key)

for val in user.values():
    print(val)

for key in sorted (user.keys()) :
    print(user[key])

# List of Dictionaries :

users = []
user = {'name' : 'Sai' , 'age' : '23' , 'gender' : 'female'}
users.append(user)
user = {'name' : 'Ram' , 'age' : '26' , 'gender' : 'male'}
users.append(user)
user = {'name' : 'Vidhya' , 'age' : '25' , 'gender' : 'female'}
users.append(user)
user = {'name' : 'Ramya' , 'age' : '24' , 'gender' : 'female'}
users.append(user)

print(users)
print(users[0])
print(users[1])
print(users[2])
print(users[3])

print(users[2]['name'])

# List in dictionary :

user ['fav_food'] = ['poori' , 'pasta' , 'fried rice' , 'pizza']
print(user)
print(user['fav_food'])
print(user['fav_food'][0])
print(user['fav_food'][1])
print(user['fav_food'][2])
print(user['fav_food'][3])

'''
Output :

Sai
13
{'name': 'Sai', 'age': '13', 'gender': 'female', 'school': 'Narayana e Techno'}
{'name': 'Sai', 'age': '13', 'gender': 'female', 'school': 'Narayana e Techno', 'city': 'Chennai'}
{'name': 'Sai', 'age': '13', 'gender': 'female', 'school': 'Narayana e Techno', 'city': 'Coimbatore'}
{'name': 'Sai', 'age': '13', 'school': 'Narayana e Techno', 'city': 'Coimbatore'}
Key : name
Val : Sai
Key : age
Val : 13
Key : school
Val : Narayana e Techno
Key : city
Val : Coimbatore
name
age
school
city
Sai
13
Narayana e Techno
Coimbatore
13
Coimbatore
Sai
Narayana e Techno
[{'name': 'Sai', 'age': '23', 'gender': 'female'}, {'name': 'Ram', 'age': '26', 'gender': 'male'}, {'name': 'Vidhya', 'age': '25', 'gender': 'female'}, {'name': 'Ramya', 'age': '24', 'gender': 'female'}]
{'name': 'Sai', 'age': '23', 'gender': 'female'}
{'name': 'Ram', 'age': '26', 'gender': 'male'}
{'name': 'Vidhya', 'age': '25', 'gender': 'female'}
{'name': 'Ramya', 'age': '24', 'gender': 'female'}
Vidhya
{'name': 'Ramya', 'age': '24', 'gender': 'female', 'fav_food': ['poori', 'pasta', 'fried rice', 'pizza']}
['poori', 'pasta', 'fried rice', 'pizza']
poori
pasta
fried rice
pizza

'''
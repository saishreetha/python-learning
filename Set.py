# Set - Unique elements only we can store and it's not ordered
# If we repeated the same colour it will print the colour only one time.

cities = ["Chennai", "Madurai", "Trichy", "Coimbatore", "Salem", "Karur"]

colours = {'Red','Yellow','Green','Red'}
print (colours)

colour_list = list(colours)
print(colour_list)

set(cities)
print(cities)



'''

Output :
{'Red', 'Yellow', 'Green'}
['Red', 'Yellow', 'Green']
['Chennai', 'Madurai', 'Trichy', 'Coimbatore', 'Salem', 'Karur']

'''
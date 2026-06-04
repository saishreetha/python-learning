cities = ["Chennai", "Madurai", "Trichy", "Coimbatore", "Salem", "Karur"]
tn = cities
karnataka = ["Bangalore" , "Vellore" , "Vijayakanda", "Guntur"]
ap = ["Tirupathi", "Mysore" , "Udupi"]
india = [tn , karnataka , ap]

print(india)
print(india[0])
print(india[1])
print(india[1][2])

sh = [[1,2,3],[4,5,6],[7,8,9]]
print(sh[1][2])
sh[2][1] = 6*2
print(sh)

cities.remove("Karur")
print(tn)

cities.append("Thanjavur")
print(tn)

cities.append("Karur")
print(tn)

indian_states = india[1]
india[0][0] = "Kadalur"
print(indian_states[0][0])


'''
Output :
[['Chennai', 'Madurai', 'Trichy', 'Coimbatore', 'Salem', 'Karur'], ['Bangalore', 'Vellore', 'Vijayakanda', 'Guntur'], ['Tirupathi', 'Mysore', 'Udupi']]
['Chennai', 'Madurai', 'Trichy', 'Coimbatore', 'Salem', 'Karur']
['Bangalore', 'Vellore', 'Vijayakanda', 'Guntur']
Vijayakanda
6
[[1, 2, 3], [4, 5, 6], [7, 12, 9]]
['Chennai', 'Madurai', 'Trichy', 'Coimbatore', 'Salem']
['Chennai', 'Madurai', 'Trichy', 'Coimbatore', 'Salem', 'Thanjavur']
['Chennai', 'Madurai', 'Trichy', 'Coimbatore', 'Salem', 'Thanjavur', 'Karur']

'''
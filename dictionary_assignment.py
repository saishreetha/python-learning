favorite_foods = {
    'Ravi': 'pizza',
    'Priya': 'pasta',
    'Kiran': 'biryani',
    'Anita': 'pizza',
    'Arjun': 'fried rice',
    'Neha': 'pasta',
    'Vikram': 'poori',
    'Meera': 'biryani',
    'Sanjay': 'pizza',
    'Divya': 'dosa'
}

just_foods = list(favorite_foods.values())

score_board = {}
for food in just_foods:
    if food in score_board:

        score_board[food] = score_board[food] + 1
    else:

        score_board[food] = 1

sorted_foods = dict(sorted(score_board.items(), key=lambda item: item[1], reverse=True))

print("--- Most Popular Foods ---")
for food, score in sorted_foods.items():
    print(food, "-", score, "votes")
favorite_foods = {
    'Ravi': 'pizza',
    'Priya': 'pasta',
    'Kiran': 'biryani',
    'Anita': 'pizza',
    'Arjun': 'fried rice',
    'Neha': 'pasta',
    'Vikram': 'poori',
    'Meera': 'biryani',
    'Sanjay': 'pizza',
    'Divya': 'dosa'
}


just_foods = list(favorite_foods.values())


score_board = {}
for food in just_foods:
    if food in score_board:

        score_board[food] = score_board[food] + 1
    else:

        score_board[food] = 1

sorted_foods = dict(sorted(score_board.items(), key=lambda item: item[1], reverse=True))

print("--- Most Popular Foods ---")
for food, score in sorted_foods.items():
    print(food, "-", score, "votes")
favorite_foods = {
    'Ravi': 'pizza',
    'Priya': 'pasta',
    'Kiran': 'biryani',
    'Anita': 'pizza',
    'Arjun': 'fried rice',
    'Neha': 'pasta',
    'Vikram': 'poori',
    'Meera': 'biryani',
    'Sanjay': 'pizza',
    'Divya': 'dosa'
}


just_foods = list(favorite_foods.values())


score_board = {}
for food in just_foods:
    if food in score_board:

        score_board[food] = score_board[food] + 1
    else:

        score_board[food] = 1

sorted_foods = dict(sorted(score_board.items(), key=lambda item: item[1], reverse=True))

print(" --- Most Popular Foods --- ")
for food, score in sorted_foods.items():
    print(food, "-", score, "votes")

'''

Output :
   
---Most Popular Foods---
pizza - 3 votes
pasta - 2 votes
biryani - 2 votes
fried rice - 1 votes
poori - 1 votes
dosa - 1 votes   
    
'''
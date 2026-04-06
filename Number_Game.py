import random

num = random.randint(1, 20)

guess = int(input("Can you guess the number what I'm thinking? Its less than 20 :"))

while guess!=num :
    if guess > num :
        print("Your guess is higher")

    else :
        print("Your guess is lower")
    guess = int(input("Guess again: "))

print("YOU WON")

'''
Output :

Can you guess the number what I'm thinking? Its less than 20 : 15
Your guess is higher
Guess again: 10
Your guess is lower
Guess again: 11
Your guess is lower
Guess again: 12
YOU WON

'''
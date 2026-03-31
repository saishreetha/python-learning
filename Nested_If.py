#Nested If
#Logical Operators are : AND , OR

num = int(input("Enter a number: "))

if num > 99 and num < 1000 :
    if num % 2 == 0 :
        print(str(num) + " is a three digit even number")

    else :
        print(str(num) + " is not a three digit even number")

'''
Output :
Enter a number: 321
321 is not a three digit even number
'''
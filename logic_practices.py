list = [3, 4, 6, 7, 5, 1, 8]

for i in range(len(list)) :

    if i == 0 :
        list[i] >= list[i+1]

    elif i == len(list) -1 :
        list[i] >=  list[i-1]

    else :
        if list[i] >= list[i-1] and list[i] >= list[i+1] :
                                print(list[i])



'''
Output :

7

'''
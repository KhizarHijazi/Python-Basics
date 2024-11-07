# The user has to input 12 times, and we need to calculate the sum of the even numbers among those inputs."

n = 12
sum_of_evens = 0

for i in range (1, n+1):
    user_num = input("enter num 1 - 12 :")
    try :
        into_integer = int(user_num)
        if 1 <= into_integer <= n:
            if into_integer % 2 == 0:
                sum_of_evens += 1
        else : print('Invalid number, please enter a number between 1 and 12.')
    except ValueError:
        print('Invalid input, please enter a valid integer.')

print("sum of evens :" , sum_of_evens)

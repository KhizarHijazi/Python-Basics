import math  # Import the math module
import random


x, y, z = 1, 2, 3
print(x)
a = x 
x = 4
print(a , x) # iska output 1 , 4 hoga bcz  ka refrence change ho gya hy or a apny old refrence pr hy

print(z * 3 ) # ye multiply hoga 
print (z ** 3) # yw power count kr rha hy or iska output 27 hoga


"""
In Python, str(), repr(), and print() serve different purposes when it comes to representing and outputting data
repr()
Purpose: Generates an official string representation of an object, ideally one that can be used to recreate the object using eval(). It's meant for developers and debugging.
"""
car = ('BMW', 'Red')
print(repr(car))  # Output: Car('BMW', 'Red')
"""
 str()
Purpose: Generates a human-readable or informal string representation of an object. It's meant for end-users.
"""
car = ('BMW', 'Red')
print(str(car))  # Output: BMW, Red
"""
 print()
Purpose: Outputs the human-readable or informal string to the console (standard output).
"""
# g = x < y < z
g = x < y and y < z

print ("here : ",g)


rsl = math.floor(-3.9)
print(rsl) #output will be 3
rz = math.trunc(-3.5)  
print(rz) #output will be 3
resl = math.floor(-3.9)
print(resl) #output will be -4
rzl = math.trunc(-3.5)  
print(rzl) #output will be -3

#Key Difference between floor() & trunc()
#floor hmesha down value count krta hy or trunc 0 sy closest value count krta hy

"""
random methods >>
"""

randomNumber=random.randint(1 , 10)
print("randomNumber",randomNumber)

#hum random use krty hoye arry me sy b randomly koi item choose kr skty hen , example :
l1 = ['Khizar' , 'Hijazi' , 'Captain', 'leiutenant']
item =random.choice(l1)
print(item)
# we can also shuffle the arry
random.shuffle(l1)
print("shuffled l1 : ", l1 )
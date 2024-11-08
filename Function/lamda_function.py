"""Lamda Function"""
# Python's lambda functions are similar to JavaScript's arrow functions. Both are used to create small, anonymous functions quickly and inline, without the need to formally define them. Lamda Limited to a single expression  so it can’t contain multiple statements or more complex logic without wrapping in a standard function.

# simple function
def cost(price , discount):
    return price - discount

print(cost(70, 20))


# lamda function
cost = lambda price , discount : price - discount

print (cost(100 , 30))
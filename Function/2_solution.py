# When we pass one parameter and more args:
#asterisk (*) in Python refers to the * symbol. The * symbol, when placed before a parameter name (like *args), collects any extra positional arguments passed to the function into a tuple.When you use *args in a function, the arguments passed are always collected into a tuple.

def table(*args):
    print(type(args)) # <class 'tuple'>
    result = []
    for num in args:
        result.append(num *2)
    return result

print(table(1 ,2,3,4,5,6,7,8,9,10))

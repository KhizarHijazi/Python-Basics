"""Key Characteristics of Tuples"""
#Immutable: Once created, the elements of a tuple cannot be changed. You can't add, remove, or modify items in a tuple.

#Ordered: Tuples maintain the order of items, meaning you can access elements using their index.

#Heterogeneous Elements: Tuples can hold different types of data (e.g., integers, strings, lists, etc.).0

#Hashable: Since tuples are immutable, they can be used as keys in dictionaries, unlike lists.


new_tuple = ("js" , "python" ,"c_sharp", "php")
tes1 = new_tuple[:]
print(tes1) #('js', 'python', 'c_sharp', 'php')

test2 = new_tuple[0:2]
print(test2) #('js', 'python')

test3 = new_tuple[3]
print("test3 :",test3) #test3 : php

test4 = new_tuple[-2]
print(test4) # c#

#test5 = new_tuple[0] = "c++"
#print(test5)
# TypeError: 'tuple' object does not support item assignment
# tuple immuteable hy ye change nhi so skta

test6 = len(new_tuple)
print(test6) # 4

my_tuple = ("swift" , "c++")
test7 = new_tuple + my_tuple
print(test7) # ('js', 'python', 'c_sharp', 'php', 'swift', 'c++')

if "c++" in test7:
    print("in c++ code is compiled before execution")
    # in c++ code is compiled before execution

# ye method value ki counting krta hy k wo kitni bar a chuki hy
test8 = new_tuple.count("c_sharp")
print(test8) # 1

#agr hm new_tuple ko same valuse k sath return kr den to wo veriable ki tra treat hn gy like :
(js , python , c_sharp , php) = new_tuple
print(js) # js
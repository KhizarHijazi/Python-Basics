"""A dictionary in Python is a built-in data type that allows you to store and manage data as key-value pairs."""

my_dict = {
    "name" : "Captain",
    "age" : 80,
    "country" : "Pakistan"
}

# we can access value by key
test1 = my_dict.get("age")
print(test1) # 80

# we can change value by key 
test2 = my_dict["name"] = "Lieutenant"
print(test2)
print(my_dict) #{'name': 'Lieutenant', 'age': 80, 'country': 'Pakistan'}s

# is loop sy hm sirf keys access kr skty hen
for dic in my_dict:
    print(dic)
# name
# age
# country

#or is tra hm both keys and valuse ko access kr skty hen
for dic2 in my_dict:
    print(dic2 , my_dict[dic2])
#name Lieutenant
# age 80
# country Pakistans

"""The preferred method for key-value access"""
# agr key value dono ko access krna hy to ye preffered method hy
for key , value in my_dict.items():
    print(key , value)

# if statement
if "age" in my_dict:
    print("80 years old") # 80 years old

# we can add key value pair or ye last me add hogi
test3 = my_dict["job"] = "coding"
print(my_dict) # {'name': 'Lieutenant', 'age': 80, 'country': 'Pakistan', 'job': 'coding'}

# isi tra hm last sy key value pair ko remove b kr skty hen
test4 = my_dict.popitem()
print(my_dict) # {'name': 'Lieutenant', 'age': 80, 'country': 'Pakistan'}

# kisi b key value pair ko pop() method sy remove kiya ja skta hy. Dictionary me indexs nhi hoty is liye remove krny k liye pop ki curly baces me key dena prti hy
test5 = my_dict.pop("age")
print(my_dict) # {'name': 'Lieutenant', 'country': 'Pakistan'}

# dictionary ek object hy or hm object k andr b objects bna skty hen yani dic k andar dics
my_2nd_dic = {"rollnum" : {"Ali" : 1 , "usman": 2 , "hamza" : 3},
              "class&section" :{"five" : "A", "eight" : "D" , "Nine" :"B"}
              }
#itni bri dic me sy agr section D ko access krna hy to is tra kren gy :
test6 =my_2nd_dic["class&section"]["eight"]
print(test6)

test7 = my_2nd_dic.clear()
print("my_2nd_dic : ",my_2nd_dic) # my_2nd_dic :  {}

# agr hmary pas sirf keys hn to hm value ko veriable me store krwa kr  keys ko alag sy value asign kr skty hen or new dic create kr skty hen
keys = ["python" , "javascript" , "typescript"]
new_value = "scripting language"

new_dict = dict.fromkeys(keys , new_value)
print(new_dict)
# output
# {'python': 'scripting language', 'javascript': 'scripting language', 'typescript': 'scripting language'}
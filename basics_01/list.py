list_name= ['karachi','lahore','multan','islamabad','hyderabad']
test1 = list_name[:]
print(test1) # The output will be as it is bcz it doesn't include index numbers.

test2 = list_name[0:3]
print(test2) # ['karachi', 'lahore', 'multan']

test3 = list_name[:2]
print(test3) # ['karachi', 'lahore']

test4 = list_name[2:]
print(test4) # index will be start from 2 and output 2 to till the end :['multan', 'islamabad', 'hyderabad']

test5 = list_name[4]
print(test5) # targeted index 4 and output :hyderabd

test6 = list_name[4] = "faisalabad"
print(test6) # it will replace the index 4 from defined value.
print(list_name) # ['karachi', 'lahore', 'multan', 'islamabad', 'faisalabad']

# using slicing dicing
# test7_part1 = list_name[3:4] = "Peshawar"
# print(test7_part1) 
# print(list_name) # ['karachi', 'lahore', 'multan', 'P', 'e', 's', 'h', 'a', 'w', 'a', 'r', 'faisalabad'] 
# is output me string "peshawar" ek aary ki tra treat hwa hy is liye us ny is string ko arry me convert kr diya hy . agr is ko as a individual item pass krwana hy to value define krty waqt hmen isy arry ki tra treat krna hoga like :
test7_part2 = list_name[3:4] = ["Peshawar"]
print(test7_part2) 
print(list_name)

test8 = list_name[3:4] = [] # ye indexs ko empty kr deta hy yani remove
print(test8) 
print(list_name) # ['karachi', 'lahore', 'multan', 'faisalabad']

test9 = list_name.append("RYK") # ye add krta hy list k end me 
print(list_name) #['karachi', 'lahore', 'multan', 'faisalabad', 'RYK']

test10 = list_name.pop() # ye remove kr deta hy last index ko 
print(list_name) #['karachi', 'lahore', 'multan', 'faisalabad']

test11 = list_name.remove("multan") # ye generally kisi b list item ko remove krta hy
print(list_name) # ['karachi', 'lahore', 'faisalabad']

test12 = list_name.insert(0 , "Quetta") # ye diye gaye index pr item ko add kr deta hy
print(list_name) # ['Quetta', 'karachi', 'lahore', 'faisalabad']


"""Refrences and Copy"""

#jb ham kisi veriable ko 2nd varible as a value asign krty hen to dono ka refrence ek hi hota hy lkn agr hm copy generate kr den to refrance change ho jata hy.. Example :
#hmary pas test12 k according lis_name ki value ye hy :['Quetta', 'karachi', 'lahore', 'faisalabad']

list_name_2 = list_name # is me dono ka refrance same hy
list_name_copy = list_name.copy() # yhan pr list_name_copy ka refrance change ho gya hy q k iska refrance exact list_name ka nhi hy blky uski copy hy . is liye List_name_copy pr apply hony wala method list_name pr apply nhi hoga : example :
test13 = list_name_copy.insert(0 , "Kashmir")
print(list_name_copy) # ['Kashmir', 'Quetta', 'karachi', 'lahore', 'faisalabad']
print(list_name) # ['Quetta', 'karachi', 'lahore', 'faisalabad']
print(list_name_2) # ['Quetta', 'karachi', 'lahore', 'faisalabad'] 
# yhan list_name & list_name_2 ka output same hy q k inka refrance same hy . ham is me sy jis me b koi changes kren gy to dosry variable me b changes ho jaen gi q k refrance same hen or ye Data type "list" muteable hy. jbky imuteable data type me aisy nhi hota agrchy refrance same ho.

"""List Loop Syntax"""

squared_num = [x**2 for x in range(10)]
#x**2 > ye x ki power 2 hy
#for x in > ye loop hy
# range(10) > ye numbers ki range btata hy k ap ny kitny numbers tak loop run krna hy . ye 10 numbers tak loop run kry ga or result me each number 2 ki power sy multiply ho jaye ga . check this :
print(squared_num) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

cube_num = [y**3 for y in range(6)]
# ye 6 numbers tak cube print krdy ga. check this:
print(cube_num) # [0, 1, 8, 27, 64, 125]
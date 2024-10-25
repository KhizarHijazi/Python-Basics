name = 'Khizar Hijazi'
slice_name = name[0:6]
print(slice_name)

num_list = '123456789'
method1 = num_list[:] # is me coplete length consider hogi
print('method1:',method1)
method2 = num_list[0:8] # 0 to 7 index pr apply hoga yani last index count nhi hoga
print('method2:',method2)
method3 = num_list[0:7:2] # is me 3rd digit btata hy kitny indexes ko skip krna hy , agr 2 hy to 1 skip hoga or 3 hy to 2 index skip ho jaen gy
print('method3:',method3)
method4 = num_list[0:9:3] # is me 2 index skip hn gy q k last me 3rd digit me 3 hy
print('method4:',method4)


print(name.lower()) #khizarhijazi
print(name.upper()) #KHIZARHIJAZI
print(name.strip()) # ye method string k agy pechy sy gap ko khtm kr deta hy

print('replaced name :',name.replace("Hijazi" , "Faizan"))

#split method string ko list me change kr deta hy or by default kr deta hy
abc = "a ,b , c , d ,e ,f,g"
print("splited :",abc.split())

print("splited not by default :",abc.split(','))
#is me by default comma remove ho jaye ga or main string ka comma baqi rhy ga

alphabets = "jsddkloikyjyjhsadhkodsiuchhsxjdbjfhgjlfvlkksakcscgjkhc"
print('k counted for',alphabets.count('k'),'times')

food = 'beaf biryani'
drink = 'chaye'
otherthings = 'Paints ,brushes and canvas'
location = 'Amazon Jungle'
person = 'for a fascinating artist'
order = 'i ordered from foodpanda {} & {} and some other things like {}. Then I parceled it to the {}'
sbmit = order.format(food , drink ,otherthings,location)
print(sbmit)

# list to string method or join sy phly string ticks me kuch b add kr skty hen like comma , space , underscore etc ..
mobiles = ['samsung' , 'iphone' , 'vivo' , 'googlepixel']
list_to_string = ''.join(mobiles)
#list_to_string = '_'.join(mobiles) example
print(list_to_string)

print(len(list_to_string)) # ye string ki length btata hy


# In Python, if you want to iterate over each letter in a string, and that string is stored as an element of a list, you can use a loop. Here's an example:
# Loop over each letter in the string
for letter in list_to_string[0]:  # list_to_string[0] gives the string 
    print(letter)

#If your list contains multiple strings, you can iterate over each string in the list first and then over the letters inside the strings:
for string in list_to_string:
    for letter in string:
        print(letter)

#jb doubble qoutes ko as it is represent krna ho to phr us k sath backslash use krty hen :
qoute ="He said: \"she is realy brilliant\" "
print(qoute)


#Backslah Problem in String >>>
#backslash string ko line me break kr deta hy, 
path1 = 'c:\drive\folder\cwd\cd'
print(path1)
# like following statement ka out ye ho ga :
#c:\drive
# older\:cwd\cd
# is sy bachny k liye string ko raw string bnana prta hy or is k liye start me r lga dena hy
path2 = r'c:\drive\folder\cwd\cd'
print(path2)
#iska 2nd method ye hy double backslah use kren lkn print me ek hi show hoga like :
path3 = 'c:\\drive\\folder\\cwd\\cd'
#output : c:\drive\folder\cwd\cd
#But Developers mostly Raw String hi use krty hen.

#we can also ask a quetion using string 
animals = 'lion , hen , sparrow , goat, dear'
ask = "lion" in animals
print(ask)
#True
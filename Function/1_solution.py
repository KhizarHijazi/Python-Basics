# Basic function syntax
def sequare_of_num(number):
    #print(number ** 4)
    return number ** 4

sequare_of_num(3)
# agr hm isko kisi varibale me store krwa kr print kren to value none  aye gi :
result = sequare_of_num(3)
print(result) # yhan function call hwa or us ny 81 print kiya or then none. none is wja sy k hm ny function ko kuch return nhi kiya. function run hwa us ny print kiya lkn kuch return nhi kiya , function ko return krwana zrori hy jo powerfull technique hy or hm is tra sub function bna kr closure create kr skty hen.

def add (num1 , num2):
    return num1 + num2

print(add(5,7))
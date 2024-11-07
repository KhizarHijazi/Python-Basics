# print the multiplication table and skip 10 iteration

n = 3
for i in range(1 , 11):
    if i ==10:
        continue
    print (f"{n} X {i} =", n * i)

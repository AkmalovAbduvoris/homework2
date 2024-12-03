num = int(input("Son kiriting: "))
hold = int()
print("Natija: ", end='')
for i in range(1,num + 1):
    hold += i * i
    print(i,"^",i, end="")
    if i == num:
        print(" = ", end="")
    else:
        print(" + ", end="")
print(hold)
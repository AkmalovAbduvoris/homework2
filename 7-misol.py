from random import randint
n = randint(1,100)
random_son = randint(1,n)
ok= int()
for i in range(3):
    print(random_son)
    send = int(input("Son kiriting: "))
    if send == random_son:
        ok = 1
        print("Winner")
        break
if not ok:
    print("Looser")

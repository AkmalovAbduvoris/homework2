age = int(input("Yoshingizni kiriting: "))

for i in range(1, 201):
    if i == age:
        print("Sizning yoshingiz")
        continue
    print(i)
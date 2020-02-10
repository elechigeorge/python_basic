weight = input('Weight: ')
value = input("(L)bs or (K)g: ")


if value.lower() == "l":
    answer = int(int(weight) * 0.45)
    print(f"You are {answer} kilos")
elif value.lower() == "k":
    answer = int(int(weight) * 2.23)
    print(f"You are {answer} pounds")

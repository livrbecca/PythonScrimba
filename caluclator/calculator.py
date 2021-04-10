mode = input('Enter math operation(+,-,*,/): ')
n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))

if mode == "+":
    print(f"{n1} + {n2} is {n1 + n2}")
elif mode == "-":
    print(f"{n1} - {n2} is {n1 - n2}")
elif mode == "*":
    print(f"{n1} * {n2} is {n1 * n2}")
elif mode == "/":
    print(f"{n1} / {n2} is {n1 / n2}")
else:
    print("error, try again")

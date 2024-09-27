valid=False

while not valid:
    try:
        num=int(input("Input a number: "))
        while num%2==0:
            print(num, "Is divisible by 2 and is valid")
        valid=True
    except ValueError:
        print("Value Error")

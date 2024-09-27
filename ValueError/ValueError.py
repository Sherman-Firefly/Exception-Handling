try:
    number=int(input("Input a number: "))
    print("Number inputted is:", number)
    print(number[5])
except ValueError as ex:
    print("Exception: ", ex)
except IndexError as ex:
    print("Exception: ", ex)
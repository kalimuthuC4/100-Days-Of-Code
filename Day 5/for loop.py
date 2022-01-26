for number in range(1,101):
    if number % 3 == 0 and number % 5== 0:
        print("fizzbizz")
    elif number % 3 == 0:
        print("bizz")
    elif number % 5 == 0:
        print("fizz")
    else:
        print(number)
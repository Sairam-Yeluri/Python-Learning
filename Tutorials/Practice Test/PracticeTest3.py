for value in range(1,50):
    if((value%3 ==0) &(value % 5 ==0)):
        print("FizzBuzz")
    elif value%3 ==0:
        print("Fizz")
    elif value%5 ==0:
        print("Buzz")
    else:
        print(value)
def fizzBuzz():
    for i in range(0,101):
        # Using if else
        # if i % 3 == 0 and i % 5 == 0:
        #     print("FizzBuzz")
        # elif i % 3 == 0 :
        #     print("Fizz")
        # elif i % 5 == 0:
        #     print("Buzz")
        # else:
        #     print(i)
        # Using Ternary Operator
        output = "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i
        print(output) 

fizzBuzz()
# Path: fizzBuzz.py
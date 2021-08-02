# Function for nth fibonacci number - Dynamic Programing
# Taking 1st two fibonacci numbers as 1 and 1
# memoization:
FibArray = [1, 1]

def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n-1]
    else:
        temp_fib = (fibonacci(n - 1) + fibonacci(n - 2)) / fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib

number = int(input("Enter the size of Fibonacci Sequence: "))
number_with_commas = "{:,}".format(fibonacci(number))
print(number_with_commas)
print (FibArray)
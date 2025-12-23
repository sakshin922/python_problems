def sum_natural_numbers_recursive(n):
    
    if n < 1:
        return "Please enter a positive integer."
    elif n == 1:
        return 1
    else:
        return n + sum_natural_numbers_recursive(n - 1)


try:
    num = int(input("Enter a positive integer: "))
    result = sum_natural_numbers_recursive(num)
    print(f"The sum of natural numbers up to {num} is: {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
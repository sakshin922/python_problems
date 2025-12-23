def find_square_root_exponent(number):
 
  if number < 0:
    return "Error: Cannot find the real square root of a negative number."
  else:
    return number ** 0.5

# Example usage:
num = float(input("Enter a number: "))
result = find_square_root_exponent(num)
print(f"The square root of {num} is: {result}")
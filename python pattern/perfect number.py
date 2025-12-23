def is_perfect_number(num):
  
  if num <= 0:  
    return False

  sum_of_divisors = 0
  for i in range(1, num):  
    if num % i == 0:
      sum_of_divisors += i

  return sum_of_divisors == num


try:
  number = int(input("Enter an integer to check if it's a perfect number: "))
  if is_perfect_number(number):
    print(f"{number} is a perfect number.")
  else:
    print(f"{number} is not a perfect number.")
except ValueError:
  print("Invalid input. Please enter an integer.")
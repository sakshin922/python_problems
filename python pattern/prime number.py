def is_prime(num):
   
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If num is divisible by any number other than 1 and itself, it's not prime
    return True  # If no divisors are found, the number is prime

def print_primes_less_than(limit):
   
    print(f"Prime numbers less than {limit} are:")
    for number in range(2, limit):
        if is_prime(number):
            print(number)


print_primes_less_than(20)
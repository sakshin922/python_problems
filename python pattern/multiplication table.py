def print_multiplication_table(number, limit=10):
    
    print(f"--- Multiplication Table of {number} ---")
    for i in range(1, limit + 1):
        product = number * i
        print(f"{number} x {i} = {product}")

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter a number to print its table (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            
            num = int(user_input)
            print_multiplication_table(num)
        except ValueError:
            print("Invalid input. Please enter an integer or 'q' to quit.")
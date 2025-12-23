def count_occurrences_with_method(numbers, target_number):
   
    return numbers.count(target_number)

# Example usage:
my_list = [1, 5, 2, 8, 5, 3, 5, 9]
number_to_find = 5
occurrences = count_occurrences_with_method(my_list, number_to_find)
print(f"The number {number_to_find} appears {occurrences} times.")
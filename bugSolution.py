def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1, 0, 3, 0, 5]
average_with_zero = calculate_average(my_list_with_zero)
print(f"The average with zeros is: {average_with_zero}")

my_list_with_strings = [1, 2, "a", 4, 5]
average_with_strings = calculate_average(my_list_with_strings)
print(f"The average with strings is: {average_with_strings}") #This will now correctly calculate the average of only the numbers
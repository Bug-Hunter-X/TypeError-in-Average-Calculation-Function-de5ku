def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

data = [10, 20, 30, 40, 'a']
result = calculate_average(data)
print(f"Average: {result}") 
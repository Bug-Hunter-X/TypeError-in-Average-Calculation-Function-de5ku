def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage with potential error:
data = [10, 20, 30, 40, 'a']
result = calculate_average(data)
print(f"Average: {result}")
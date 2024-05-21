import random

def generate_unique_numbers(n, max_val):
    numbers = []
    seen = set()

    while len(numbers) < n:
        num = random.randint(1, max_val)

        # Ensure no number is exactly twice or half (when even) of any other
        if num not in seen and (2 * num) not in seen and (num // 2 not in seen or num % 2 != 0):
            numbers.append(num)
            seen.add(num)

    return numbers

def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        # First line: count of numbers
        file.write(f"{len(numbers)}\n")
        # Second line: numbers separated by a single space
        file.write(" ".join(map(str, numbers)) + "\n")

# Generate the list
n = 200000  # Number of integers
max_val = 10**9 // 2  # Maximum value
unique_numbers = generate_unique_numbers(n, max_val)

# Output to file
filename = "inworst"
write_numbers_to_file(filename, unique_numbers)

print(f"Generated numbers have been saved to {filename}.")

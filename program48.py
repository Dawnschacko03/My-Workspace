#program to find the missing number
numbers = [1, 2, 4, 5]

n = len(numbers) + 1

for i in range(1, n + 1):
    if i not in numbers:
        print("Missing number:", i)
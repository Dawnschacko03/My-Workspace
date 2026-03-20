#program to find the largest and smallest element in the list
numbers=[3,4,5]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest element:", largest)
print("Smallest element:", smallest)

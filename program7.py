#Sum of first N natural numbers
N = int(input("Enter a number: "))
total = 0

for i in range(1, N+1):
    total += i
    
    if i < N:
        print(i, "+", end=" ")
    else:
        print(i, end=" ")

print("=", total)
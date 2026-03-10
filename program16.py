#program to find sum of series s=(1)+(1+2)+(1+2+3)+...+(1+2+3+...+n)
n = int(input(""))
total = 0
for i in range(1, n + 1):
    temp_sum = 0
    
    for j in range(1, i + 1):
        temp_sum += j
        
    total += temp_sum
print("Sum of the series =", total)
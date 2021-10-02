n = int(input("Enter range:"))
for j in range(n):
    n1 = j
    sum = 0
    for i in str(n1):
        sum += int(i) ** len(str(j))
    if sum == n1:
        print(j)

# program to check whether given number is armstrong number or not
n = int(input("Enter Number: "))
sum = 0
for i in str(n):
    sum += int(i)**3
if sum == n:
    print("is Armstrong number")
else:
    print("is not Armstrong")

# with ou converting string
original_n_value = n
sum2 = 0
while(n>0):
    last_value = n % 10
    sum2 += last_value ** 3
    n = n//10
if sum2 == original_n_value:
    print("is Armstrong number")
else:
    print("is not Armstrong")
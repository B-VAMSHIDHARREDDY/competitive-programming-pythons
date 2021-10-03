# Program for factorial of a number
T = True
while(T):
    n = int(input("Enter number: "))
    fact = 1
    if n<0 or n == 0:
        print("Enter correct number?????")
    else:
        for i in range(1,n+1):
            fact = i * fact
        print("Factorial of given number is : ",fact)
        T = False

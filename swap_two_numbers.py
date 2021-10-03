a = int(input("Enter 'a' number: "))
b = int(input("Enter 'b' number: "))

# using temp variable
temp = a
a = b
b = temp
print(f"after swaping\na number is:{a} \nb number is:{b}")

# without usin temp

a = a + b
b = a - b
a = a - b
print(f"after swaping\na number is:{a} \nb number is:{b}")

a, b = b,a  # This line swap that two numbers

print(f"after swaping\na number is:{a} \nb number is:{b}")

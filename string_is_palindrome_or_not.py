string = input("Enter the Palindrome String: ")
# Using slicing
pali = string[ : :-1]
if pali == string:
    print("Given String is Palindrome")
else:
    print("Given String is Not Palindrome")


# without using slicing
print("---------------------------------------------")
pali = ''
for i in string:
    pali = i + pali
if pali == string:
    print("Given String is Palindrome")
else:
    print("Given String is Not Palindrome")
# using slicing method
string = input("Enter your string: ")
rev = string[::-1]
print(rev)
# without slicing
print("----------------")
Rev_string = ''
for i in string:
    Rev_string = i + Rev_string
print(Rev_string)


# n = int(input("enter the n number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(f'sum of 1 to {n} numbers is :{sum}')
def para(str):
    for i in range(len(str)):
        str = str.replace('()','')
    print(str)
    return len(str)
s = input()
res = para(s)
print(res)

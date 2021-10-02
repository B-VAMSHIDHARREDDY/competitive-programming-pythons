a = int(input())
d = {}
l = []
for _ in range(a):
    n,m = input().split(' ')
    n = int(n)
    m = int(m)
    count = 1
    for x in range(1,n):
        for y in range(1,n):
            for z in range(1,n):
                if (x + y + z) == n:
                    if 0 < (z <= y <= x):
                        if (x - y - z) > m:
                            count += 1
    l.append(count)
for i in l:
    print(i)


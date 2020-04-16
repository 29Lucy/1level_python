a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
i = 0
for x in range(1001):
    f = (a * x ** 3 + b * x ** 2 + c * x + d)
    if x != e:
        g = x - e
#    (ax³+bx²+cx+d) / (x - e) = 0
        if (f / g) == 0 and g != 0:
            i += 1

print(i)

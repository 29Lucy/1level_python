n = int(input())
print('+___ ' * n)
for i in range(1, n + 1):
    mT = ("|", i, "/ ")
    a, b, c = mT
    print(str(a)+str(b), c, end="")
print()
print('|__\\ ' * n)
print('|    ' * n)

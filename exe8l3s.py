a = 1
b = 1
x = 2
print(a)
print(b)
while x < 15:
    y = a + b
    print(y)
    a = b
    b = y
    x += 1
n = int(input("Digite a base: "))
m = int(input("Digite o expoente: "))
res = 1
x = 0
while x < m:
    res *= n
    x += 1
print(f"{n} elevado a {m} = {res}")

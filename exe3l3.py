n = int(input("Insira um número para a tabuada:"))
i = 0

for i in range(1, 11):
    res = n * i
    print(f"{n} x {i} ={res}" )
x = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    x.append(n)

maior = max(x)
menor = min(x)

print("Maior número:", maior)
print("Menor número:", menor)

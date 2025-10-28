n = int(input('Insira um número inteiro menor ou igual a 50:'))
if n <= 50:
    while n < 250:
        print(n)
        n *= 3
else:
    print('Número inválido!')
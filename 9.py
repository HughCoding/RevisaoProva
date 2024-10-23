alpha = float(input('Informe alpha: '))
x = float(input('Informe X: '))
if alpha > 0.1:
    print('Valor inválido para alpha')
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)

# resposta esperada =
# Para alpha > 0.1, ele retorna uma mensagem de erro.
# Para alpha <= 0.1 e x < 0, ele retorna o produto de alpha e x.
# Para alpha <= 0.1 e x >= 0, ele retorna o valor de x.

# Nao escrevi o que ele retorna apenas os valores de menor ou igual a e maior ou igual a
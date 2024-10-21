def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(soma_diagonal_principal(matriz))

#RESPOSTA = A, MARQUEI "E" NÃO PRESTEI ATENÇÃO QUE ERA A DIAGONAL PRINCIPAL, ESCOLHI A ALTERNATIVA QUE DEU COMO RESULTADO A DIAGONAL SECUNDARIA








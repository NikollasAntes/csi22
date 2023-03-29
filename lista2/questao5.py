def multiplicar_matrizes(A,B):
    
    rA = len(A)
    rB = len(B)
    cA = len(A[0])
    cB = len(B[0])

    if cA != rB:
        raise ValueError("Não é possível fazer a multiplicação das matrizes")
    
    M = [[0 for _ in range(cB)] for _ in range(rA)]

    for i in range(rA):
        for j in range(cB):
            for k in range(rB):
                M[i][j] += A[i][k] * B[k][j]

    return M

#A = [[1,2,3],[4,5,6]]
#B = [[7,8],[9,10],[11,12]]
#print(multiplicar_matrizes(A,B))

#C = [[1,2,3],[4,5,6],[7,8,9]]
#D = [[7,8],[9,10],[11,12]]
#print(multiplicar_matrizes(C,D))

#E = [[1,2,3],[4,5,6]]
#F = [[7,8],[9,10],[11,12],[13,14]]
#print(multiplicar_matrizes(E,F))

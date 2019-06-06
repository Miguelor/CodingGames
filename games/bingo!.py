# =============================================================================
# n = 1
# 
# bingos = [[[1, 67, 89, 69, 48],
#           [72, 65, 38, 85, 28],
#           [37, 29, 0, 54, 22],
#           [83, 80, 10, 75, 58],
#           [25, 35, 49, 87, 27]],
#          [[1, 67, 89, 69, 48],
#           [72, 65, 38, 85, 28],
#           [37, 29, 0, 54, 22],
#           [83, 80, 10, 75, 58],
#           [25, 35, 49, 87, 27]]]
# 
# resultados = [[[0,0,1,0,0], # Filas
#               [0,0,1,0,0], # Columnas
#               [0,0,1,0,0], # Diagonal
#               [0,0,1,0,0]], # Diagonal Inversa
#              [[0,0,1,0,0],
#               [0,0,1,0,0],
#               [0,0,1,0,0],
#               [0,0,1,0,0]]]
# 
# calls = [65, 4, 48, 59, 26, 24, 3, 60, 36, 29, 54, 47, 78, 32, 18, 9, 83, 90, 2, 50, 17, 45, 11, 20, 55, 33, 30, 64, 35, 75, 39, 81, 71, 70, 5, 52, 53, 46, 88, 6, 41, 66, 86, 67, 49, 38, 62, 31, 85, 27, 13, 84, 58, 1, 40, 80, 16, 82, 22, 76, 57, 37, 14, 19, 79, 73, 44, 68, 15, 43, 87, 72, 8, 42, 69, 12, 34, 89, 77, 21, 74, 51, 63, 25, 10, 61, 56, 28, 7, 23]
# =============================================================================

n = int(input())
bingos = list()
resultados = list()
for i in range(n) :
    bingo = list()
    resultado = list()
    for j in range(5) :
        bingo.append(list(map(int, input().split())))
        resultado = [[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]]
    bingos.append(bingo)
    resultados.append(resultado)

calls = list(map(int, input().split()))

line_ = len(calls)
bingo_ = len(calls)

for m in range(n): 
    for c in range(len(calls)):
    
        num = calls[c]
        for i in range(5) :
            for j in range(5) :
    
                if num == bingos[m][i][j] :
                    resultados[m][0][i] += 1 # Añadir a contador de filas
                    resultados[m][1][j] += 1 # Añadir a contador de columnas
    
                    if i == j :
                        resultados[m][2][i] += 1 # Añadir a contador de diagonal
                    if (i + j) == 4 :
                        resultados[m][3][i] += 1 # Añadir a contador de diagonal
    
                    if (
                        (5 in resultados[m][0] or 5 in resultados[m][1] or 
                        set(resultados[m][2]) == set([1]) or
                        set(resultados[m][3]) == set([1])) and c+1 < line_
                        ): #
    
                        line_ = c+1
    
                    if (
                        (set(resultados[m][0]) == set([5]) and 
                        set(resultados[m][1]) == set([5])) and c+1 < bingo_ 
                        ):
    
                        bingo_ = c+1

print(line_)
print(bingo_)
N: int
cont: int

N = int(input("Qual a ordem da matriz? "))

mat: [[int]] = [[0 for x in range (N)] for x in range (N)]

for i in range(0,N):
    for j in range(0,N):
        mat[i][j] = int(input(f"Elemento: [{i},{j}]:"))

print("DIAGONAL PRINCIPAL: ")

for i in range(0,N):
        print(mat[i][i],end=" ")

print("")

cont = 0

for i in range(0,N):
    for j in range(0,N):
        if mat[i][j] < 0:
           cont+=1

print(f"QUANTIDADE DE NEGATIVOS = {cont}",end="")
print("")


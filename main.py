from Board import Board
# from SearchEngine import SearchEngine
from BuscaCega import BuscaCega
from BuscaHeuristica import BuscaHeuristica

print("")
print("#"*30)
print(" "*7+"INICIANDO BUSCA")
print("#"*30)
print("\n")
mat = ""

while len(mat) != 9:
    print("Digite o Jogo como deseja resolver:(No formato: 0,2,1,5,6...[separados por virgula e sem espaços em branco])(Zero representa a posicao vazia)")
    mat = input()
    mat.strip() #para retirar espacoes em brando na volta
    mat = mat.split(",")
    if len(mat) > 9:
        print("Você digitou numeros a mais!!")
    elif len(mat) < 9:
        print("Você digitou números a menos!!!")

matrix = []
temp = []
for i in mat:
    temp.append(int(i))
    if len(temp) == 3:
        matrix.append(temp)
        temp = []
goalBoard = Board('goal')
scrambledBoard = Board('matrix', matrix)

buscaCega = BuscaCega(scrambledBoard, goalBoard)
buscaHeuristica = BuscaHeuristica(scrambledBoard, goalBoard)


print("Matriz objetivo:")
goalBoard.showNodeMatrix()
print("\n")

print("Matriz Inicial:")
scrambledBoard.showNodeMatrix()
print("\n")

opt = None
while opt != 0:
    try:
        print("Escolha o algoritimo de busca: \n 1 - Busca Cega\n2 - Busca heuristica(Numero de passos até a posicao correta)\n0 - Finalizar")
        opt = int(input())
    except ValueError:
        print("Você digitou um valor que não é um número!!!")
    print("\n")
    if opt == 1:
        print("####  INICIO BUSCA CEGA ####")
        print("\n")
        buscaCega.buscaCega()
        print("####   FIM BUSCA CEGA ####")
    elif  opt == 2:
        print("####  INICIO BUSCA HEURISTICA ####")
        print("\n")
        buscaHeuristica.buscaHeuristica()
        print("####   FIM BUSCA HEURISTICA ####")

    elif  opt == 0:
        print("Fim")
    else:
        print("Você digitou uma opção fora dos limites!!")
    print("\n")
    print("\n")


print("\n")
print("#"*30)
print(" "*4+"FINALIZANDO ALGORITMO")
print("#"*30)

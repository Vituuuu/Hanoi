import sys
mn = input('Bem vindo a torre de hanoi de Vitor e Bet voce deseja jogar?{S/N}:').upper()
if mn == 'N':
    print ('tchau'), sys.exit()

else:
    print ('''Regras:A Torre de Hanói é um quebra-cabeça que consiste em três hastes e discos de tamanhos diferentes
            que são posicionados na primeira haste de forma decrescente. O objetivo do quebra-cabeça
            é mover todos os discos para última haste.
            Para isso pode-se mover apenas um disco de cada vez para uma das hastes.
            Os discos podem ser empilhados, no entanto um disco nunca pode ser empilhado sobre outro disco menor que ele.''')
try:
    block =int(input ('Voce deseja jogar com quantos bloquinhos: '))

except ValueError:
    block = int(input('Voce deseja jogar com quantos bloquinhos: '))

a = list(range(1,block+1)[::-1])
b = []
c = []
marcio = 0
while marcio == 0:
    print("A -",a)
    print("B -",b)
    print("C -",c)
    if c == list(range(1,block+1)[::-1]):
        print("Parabés você GANHOU!!!")
        marcio+=1
        sys.exit()
    var = 0
    tira= input("De qual pilha você deseja retirar o objeto:").upper()
    coloca = input("Em qual pilha você deseja colocar esse objeto:").upper()
    if tira == "A":
        var = a.pop()
    elif tira == "B":
        var = b.pop()
    elif tira == "C":
        var= c.pop()
    else:
        print ("valor inválido")
        continue
    jooj= 0
    while jooj == 0:
        if coloca == "A":
            if len(a)==0:
                a.append(var)
                jooj+=1
            elif a[len(a)-1] < var:
                coloca= input("Digite uma pilha válida").upper()
            else:
                a.append(var)
                jooj+=1


        elif coloca == "B":
            if len(b)==0:
                b.append(var)
                jooj+=1
            elif b[len(b)-1] < var:
                coloca= input("Digite uma pilha válida:").upper()
            else:
                b.append(var)
                jooj+=1

        elif coloca == "C":
            if len(c) == 0:
                c.append(var)
                jooj+=1
            elif c[len(c)-1] < var:
                coloca=input("Digite uma pilha válida:").upper()
            else:
                c.append(var)
                jooj+=1


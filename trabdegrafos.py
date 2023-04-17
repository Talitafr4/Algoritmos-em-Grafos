
def inicio():
    while True:
        try:
            pergunta = int(input(
                "Digite se gostaria de 1-Escrever (Criar), 2-Ler (abrir) ou 3-Sobrescrever arquivo já escrito?\n"))
            print("Sua opção é: %s" % pergunta)
            nomearq = input("Qual é o nome do grafo?\n")
            nomearq = nomearq + ".txt"
            if (pergunta == 1):
                arq = open(nomearq, "a+")
                break
            elif (pergunta == 2):
                arq = open(nomearq, "r")
                teste = arq.read()
                if (teste == ''):
                    print("O arquivo está vazio!")
                else:
                    print(teste)
                break
            elif (pergunta == 3):
                arq = open(nomearq, "w")
                break
            else:
                raise Exception

        except EnvironmentError:
            print("O Arquivo não existe!")
        except:
            print("Não entendi, por favor tente de novo.")

    if ((pergunta == 1) or (pergunta == 3)):
        while True:
            try:
                n = int(input("Digite a quantidade de vértices:\n"))
                if (n <= 0):
                    raise Exception
                break

            except:
                print("Insira um valor válido (inteiro maior do que zero)")
        (matriz, m) = criamatriz(n, arq)
        printaarq(n, matriz, arq, m)

    while True:
        try:
            arq.close()
            break
        except OSError:
            print("Não consegui fechar, por favor tente novamente.")


def printaarq(n, aux, arq, m):

    for k in range(n):
        print("  %d\t" % k, end="", file=arq)
    print("\n"+("-"*(n*8)), file=arq)
    for i in range(n):
        print("%s%s" % (i, "|"), end="", file=arq)
        for j in range(n):
            print(" %d \t " % aux[i][j], end="", file=arq)

        print("|", file=arq)

    print("m=%s \n\n" % m, file=arq)


def criamatriz(n, arq):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append('-')
        matriz.append(linha)
    matriz = preencher_tabela(n, matriz)
    matriz, m = printaecalc(n, matriz)
    return matriz, m


def preencher_tabela(n, aux):
    for i in range(n):

        for j in range(n):
            if (i == j):
                aux[i][j] = 0
            elif ((aux[i][j] == '-') and (aux[j][i] == '-')):
                while True:
                    try:
                        pergunta = int(input(
                            "O vértice %d tem aresta com o vértice %d (responda 1 para sim ou 0 para não)\n" % (i, j)))
                        if ((pergunta == 0) or (pergunta == 1)):
                            aux[i][j] = pergunta
                            break
                        else:
                            print("Preencha somente 0 ou 1\n")

                    except ValueError:
                        print("Preencha somente 0 ou 1\n")

            else:
                aux[i][j] = aux[j][i]
    return aux


def printaecalc(n, aux):
    print("Seu grafo")
    m = 0
    for k in range(n):
        print("  %d\t" % k, end="")
    print()
    print("-"*(n*8))
    for i in range(n):
        print("%s%s" % (i, "|"), end="")
        for j in range(n):
            print(" %d \t " % aux[i][j], end="")
            if (aux[i][j] == 1):
                m += 1
        print("|")

    m = int(m/2)
    print("m=%d" % (m))
    return aux, m



# ______main________
inicio()

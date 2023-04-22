
def inicio():
    while True:
        try:
            pergunta = int(input(
                "Digite o número da opção:\n 1-Escrever (Criar) um arquivo\n 2-Ler (abrir) um arquivo\n"))
            print("Sua opção é: %s\n" % pergunta)
            
        
            if (pergunta == 2):
                tipo_arquivo = int(input("Digite o tipo de grafo:\n 1-Grafo simples\n 2-Grafo completo\n 3-Grafo bipartido completo\n 4-Grafo estrela\n"))
                print("Sua opção é: %s\n" % tipo_arquivo)
                if((tipo_arquivo<=0) or (tipo_arquivo>4)):
                    raise Exception
                elif(tipo_arquivo==1):
                    nomearq = input("Qual é o nome do grafo a ser lido?\n")
                    nomearq = nomearq + ".txt"
                elif(tipo_arquivo==2):
                    nl = input("Digite a quantidade de vértices:\n")
                    nomearq = "completo_" +str(nl)+".txt"
                elif(tipo_arquivo==3):
                    n1 = input("Digite o n1:\n")
                    n2 = input("Digite o n2:\n")
                    nomearq = "bipartido_completo_" + n1 + n2 + ".txt"
                else:
                    n = input("Digite o n:\n")
                    nomearq = "estrela_" + n + ".txt"
                arq = open(nomearq, "r")
                teste = arq.read()
                if (teste == ''):
                    print("\nO arquivo está vazio!\n")
                else:
                    print(teste)
                break

            elif(pergunta==1):
                break

            else:
                raise Exception

        except EnvironmentError:
            print("\nO Arquivo não existe!\n")
        except:
            print("\nNão entendi, por favor tente de novo.\n")

    if ((pergunta == 1) or (pergunta == 3)):
        while True:
            try:
                
                question = int(input(
                    "Digite:\n 1-Se quer escrever um grafo simples \n 2-Se quer escrever um grafo completo\n 3-Um grafo bipartido completo \n 4-Um grafo estrela\n"))
                print("Sua opção é: %s\n" % question)
                if((question<=0) or (question>4)):
                    raise Exception
                else:
                    if(question==3):

                        n1=int(input("Digite o n1:\n"))
                        n2=int(input("Digite o n2:\n"))
                        if((n1<=0) or (n2<=0)):
                            raise Exception
                        nomearq = "bipartido_completo_"+ str(n1) + str(n2) + ".txt"
                        arq = open(nomearq, "w")
                        n=n1+n2
                        matriz=criamatriz(n)
                        matriz = preencher_tabela(n, matriz,question,n1,n2)
                        matriz, m = printaecalc(n, matriz)
                        printaarq(n, matriz, arq, m)

                    elif(question==4):
                        
                        n=int(input("Digite o n:\n"))
                        if((n<=0)):
                            raise Exception
                        nomearq = "estrela_"+ str(n) + ".txt"
                        arq = open(nomearq, "w")
                        nt=n+1
                        matriz=criamatriz(nt)
                        matriz = preencher_tabela(nt, matriz,question,1,n)
                        matriz, m = printaecalc(nt, matriz)
                        printaarq(nt, matriz, arq, m)
                    elif(question==2):
                        n = int(input("Digite a quantidade de vértices:\n"))
                        if(n <= 0):
                            raise Exception
                        nomearq = "completo_"+ str(n) + ".txt"
                        arq = open(nomearq, "w")
                        matriz = criamatriz(n)
                        matriz = preencher_tabela(n, matriz,question,0,0)
                        matriz, m = printaecalc(n, matriz)
                        printaarq(n, matriz, arq, m)
                    else:
                        nomearq = input("Qual é o nome do grafo?\n")
                        nomearq = nomearq + ".txt"
                        arq = open(nomearq, "w")
                        n = int(input("Digite a quantidade de vértices:\n"))
                        if(n <= 0):
                            raise Exception
                        
                        matriz = criamatriz(n)
                        matriz = preencher_tabela(n, matriz,question,0,0)
                        matriz, m = printaecalc(n, matriz)                        
                        printaarq(n, matriz, arq, m)
                        


                break

            except Exception:
                print("\nNão entendi, por favor tente de novo.\n")
                
        


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
            print(" %s \t " % aux[i][j], end="", file=arq)

        print("|", file=arq)

    print("m=%s \n\n" % m, file=arq)


def criamatriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append('-')
        matriz.append(linha)
    
    return matriz


def preencher_tabela(n, aux,question,n1,n2):
    for i in range(n):

        for j in range(n):
            if (i == j):
                aux[i][j] = 0
            else:
                if((aux[i][j] == '-') and (aux[j][i] == '-')):
                    if(question==1):
                        while True:
                            try:
                                pergunta = int(input(
                                    "O vértice %d tem aresta com o vértice %d (responda 1 para sim ou 0 para não)\n" % (i, j)))
                                if ((pergunta == 0) or (pergunta == 1)):
                                    aux[i][j] = pergunta
                                    aux[j][i] = aux[i][j]
                                    break
                                
                                else:
                                    print("Preencha somente 0 ou 1\n")

                            except ValueError:
                                print("Preencha somente 0 ou 1\n")
                    else:
                        if((question==3) or (question==4)):
                            if(((i>=(n1)) ^ (j>=(n1)))):
                                aux[i][j]=1
                                aux[j][i]=1
                            else:
                                aux[i][j]=0
                                aux[j][i]=0
                                
                        else:
                            aux[i][j] = 1
                            aux[j][i] = 1

           

            
    return aux


def printaecalc(n, aux):
    print("Seu grafo:\n")
    m = 0
    for k in range(n):
        print(f" {k}\t", end="")
    print()
    print("-"*(n*8))
    for i in range(n):
        print("%s%s" % (i, "|"), end="")
        for j in range(n):
            print(f" {aux[i][j]} \t ", end="")
            if (aux[i][j] == 1):
                m += 1
        print("|")

    m = int(m/2)
    print("m=%d" % (m))
    return aux, m





# ______main________
inicio()

"""
ALUNO= Pedro Lunardelli Antunes

Python for beginners, simpplilearn, stackoverflow e python pool foram usados para ajudar na formatação da saída, nenhum código foi copiado.
Alterações foram feitas com o objetivo de evitar plagios e para adaptar aos conhecimentos do aluno (nenhum código de alto nível foi usado).

O CÓDIGO ABAIXO TEM COMO OBJETIVO LER ARQUIVOS DE TEXTO E BUSCAR TIPOS DE OPERAÇÕES ENTRE CONJUNTOS E OS CONJUNTOS A SEREM TRABALHADOS.
A SAÍDA DO PROGRAMA CONTÉM A OPERAÇÃO, OS CONJUNTOS E A RESPOSTA.
"""
#Abre o arquivo, só mudar o nome do arquvio de texto que quer analisar para iniciar
opening=open('TEST2.txt')

#Lê o arquivo e o separa em linhas.
readline=opening.read().splitlines()
matrix=[]
x=1
y=2
z=3

#Preenche a matriz criada com as colunas (rows). Cada uma contém o tipo de operação e os dois conjuntos.
for i in range(int(readline[0])):
    row=[]
    row.append(readline[x][0])
    row.append(readline[y])
    row.append(readline[z])
    matrix.append(row)
    x+=3
    y+=3
    z+=3
for i in matrix:
    print(i,"\n")

#Começo das operações, o "i" é limitado ao número de operações definido no começo do arquivo.
for i in range(int(readline[0])):
    #"anwser" é uma variável usada para a união, ela soma os dois conjuntos.
    anwser=matrix[i][1]+','+matrix[i][2]
    anwser=anwser.split(',')

    #"final" é uma lista para armazenar apenas o que sera imprimido de acordo com cada operação de conjuntos, ela reseta todo término de operação.
    final=[]
    
    #"matrix[i][0] é onde se encontram todos os tipos de operações a serem feitas. Cada operação possui uma regra única para preencher o "final".
    if matrix[i][0]=='U':
        for j in anwser:
            if j not in final:
                final.append(j)
        final=','.join(final)
        a='União'
    elif matrix[i][0]=='I':
        for j in matrix[i][1].split(','):
            if j in matrix[i][2].split(',') and j not in final:
                final.append(j)
        final=','.join(final)
        a='Interseção'
    elif matrix[i][0]=='D':
        for j in matrix[i][1].split(','):
            if j not in matrix[i][2].split(',') and j not in final:
                final.append(j)
        final=','.join(final)
        a="Diferença"
    elif matrix[i][0]=='C':
        for j in matrix[i][1].split(','):
            for h in matrix[i][2].split(','):
                final.append('('+j+','+h+')')
        final=','.join(final)
        a=("Produto cartesiano")

    #Imprime os resultados, "a" é o nome da operação, e os conjuntos usados variam de acordo com o "i", que incrementa com o recomeço do loop
    print(a+': conjunto 1{'+str(matrix[i][1])+'}, conjunto 2{'+str(matrix[i][2])+'}. Resultado: {'+str(final)+'}\n')

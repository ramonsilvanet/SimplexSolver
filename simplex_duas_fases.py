# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 19:09:10 2017

@author: UR4X
"""


def simplex(tabela, tipo_calculo):
    print("--------- Início Simplex -----------------")
    imprimir_tabela(tabela)
    print("--------- Simplex - 1a Fase -----------------")
    tabela_1a_fase = primeira_fase(tabela, tipo_calculo)
    print("--------- Simplex - 2a Fase -----------------")
    simplex_tableaux(tabela_1a_fase, 2, tipo_calculo)


def simplex_tableaux(tabela, fase, tipo_calculo):
    print("--------- Variáveis -----------------")
    # Encontrando as variáveis de entrada e de saída
    indice_coluna_pivot = 1
    for i in range(1, len(tabela[0]) - 1):
        if tabela[0][i] < tabela[0][indice_coluna_pivot]:
            indice_coluna_pivot = i

    print ("variável de entrada X" + str(indice_coluna_pivot))

    num_linhas_ignorar = 1

    if fase == 1:
        num_linhas_ignorar = 2

    indice_linha_pivot = 0
    menor_quociente = 999999
    vetor_resultado = [row[-1] for row in tabela]
    for i in range(num_linhas_ignorar, len(vetor_resultado)):
        if tabela[i][indice_coluna_pivot] > 0:
            resultado_parcial = vetor_resultado[i] / tabela[i][indice_coluna_pivot]
            if resultado_parcial > 0 and resultado_parcial < menor_quociente:
                indice_linha_pivot = i
                menor_quociente = resultado_parcial

    print ("variável de saída", tabela[indice_linha_pivot][0])

    # Encontrando o elemento pivot que será usado na alteração da linha da variável que sai
    elemento_pivot = tabela[indice_linha_pivot][indice_coluna_pivot]

    # Alterando a linha da variável que sai
    for i in range(1, len(tabela[indice_linha_pivot])):
        tabela[indice_linha_pivot][i] = tabela[indice_linha_pivot][i] / elemento_pivot

    # Alterando a tabela. Substituindo a variável que sai pela que entra, na 1a coluna.
    tabela[indice_linha_pivot][0] = "X" + str(indice_coluna_pivot)

    # Alterando as demais linhas da tabela.
    for i in range(len(tabela)):

        elemento_coluna_pivot = tabela[i][indice_coluna_pivot]

        if i == indice_linha_pivot:
            continue

        for j in range(1, len(tabela[0])):
            tabela[i][j] = tabela[i][j] - tabela[indice_linha_pivot][j] * elemento_coluna_pivot

    print("----------- Tabela Alterada ---------------")
    imprimir_tabela(tabela)

    # Verifica se foi encontrada a solução ótima.
    if verifica_solucao(tabela[0]) == False:
        simplex_tableaux(tabela, fase, tipo_calculo)
    elif fase == 2:
        print("----------- Resultado do Sistema ---------------")
        if tipo_calculo == "minimizar":
            print ("Resultado do Sistema:", round(tabela[0][-1], 3) * -1)
        else:
            print ("Resultado do Sistema:", round(tabela[0][-1], 3))
        for i in range(1, len(tabela)):
            print ("Valor da variável " + tabela[i][0] + ":", round(tabela[i][-1], 3))

        print ("As demais variáveis tem valor zero.")

    return tabela


def primeira_fase(tabela, tipo_calculo):
    tabela_alterada = []

    # Acrescentando uma linha a mais - Q - Função objetivo alterada
    linha_nova = ['Q']

    for j in range(1, len(tabela[0])):
        soma = 0
        for i in range(1, len(tabela)):
            soma += tabela[i][j]
        linha_nova.append(soma * -1)

    tabela_alterada.append(linha_nova)

    for i in range(len(tabela)):
        tabela_alterada.append(tabela[i])

        # Se a função for de minimização, multiplica todos os elementos da função
    # objetivo por -1 -> Minimização f(x) = Maximização -f(x)

    if tipo_calculo == 'minimizar':
        for j in range(1, len(tabela_alterada[1])):
            tabela_alterada[1][j] *= -1

    # Acrescentando as variáveis artificiais à tabela

    num_variaveis_artificiais = len(tabela_alterada) - 2

    for i in range(len(tabela_alterada)):
        temp = 2
        for j in range(num_variaveis_artificiais):
            if i == 0 or i == 1:
                tabela_alterada[i].append(0)
            else:
                if i - temp == 0:
                    tabela_alterada[i].append(1)
                    tabela_alterada[i][0] = "X" + str(len(tabela_alterada[i]) - 2)
                else:
                    tabela_alterada[i].append(0)
            temp += 1

    tabela_swap = []
    coluna_resultado = len(tabela_alterada[0]) - num_variaveis_artificiais - 1

    for i in range(len(tabela_alterada)):
        linha_swap = []
        for j in range(len(tabela_alterada[0])):
            if j != coluna_resultado:
                linha_swap.append(tabela_alterada[i][j])
        linha_swap.append(tabela_alterada[i][coluna_resultado])
        tabela_swap.append(linha_swap)

    tabela_alterada = tabela_swap[:]

    print ("----------- Tabela Alterada Fase 1 ---------------")

    imprimir_tabela(tabela_alterada)

    tabela_alterada = simplex_tableaux(tabela_alterada, 1, tipo_calculo)

    # Retirando as colunas com as variáveis artificiais e a linha
    # com a função objetivo alterada (Q)

    tabela_swap = []

    for i in range(1, len(tabela_alterada)):
        linha_swap = []
        for j in range(len(tabela_alterada[0])):
            if j not in range(len(tabela_alterada[0]) - num_variaveis_artificiais - 1, len(tabela_alterada[0]) - 1):
                linha_swap.append(tabela_alterada[i][j])
        tabela_swap.append(linha_swap)

    tabela_alterada = tabela_swap[:]

    print ("----------- Tabela Alterada - Final Fase 1 ---------------")

    imprimir_tabela(tabela_alterada)

    # Retorna a tabela alterada para que a fase 2 inicie

    return tabela_alterada


def define_variavel_entrada(linha):
    posicao = 1
    for i in range(1, len(linha) - 1):
        if linha[i] < linha[posicao]:
            posicao = i

    return posicao


def define_variavel_saida(indice_coluna_pivot, tabela):
    posicao = 0
    menor_quociente = 999999
    vetor_resultado = [row[-1] for row in tabela]
    for i in range(1, len(vetor_resultado)):
        if tabela[i][indice_coluna_pivot] > 0:
            resultado_parcial = vetor_resultado[i] / tabela[i][indice_coluna_pivot]
            if resultado_parcial > 0 and resultado_parcial < menor_quociente:
                posicao = i
                menor_quociente = resultado_parcial
    return posicao


def verifica_solucao(linha_funcao_objetivo):
    solucao_otima = True
    for i in range(1, len(linha_funcao_objetivo) - 1):
        if linha_funcao_objetivo[i] < 0:
            solucao_otima = False
            break
    return solucao_otima


def imprimir_tabela(tabela):
    print("Base", end='')

    for i in range(1, len(tabela[0]) - 1):
        print('\t', "X" + str(i), end='')

        print('\t', "Result", end='')
        print()

        for i in range((len(tabela))):
            for j in range(len(tabela[0])):
                if isinstance(tabela[i][j], str):
                    print(tabela[i][j], '\t', end='')
                    else:
                    print(round(tabela[i][j], 3), '\t', end='')
                    print()

            if __name__ == '__main__':
                print ("  Resolucao do sistema pelo método SIMPLEX ")

                """
            Minimizar: f(x) = 10X1 + 4X2 + 5X3
            Sujeito a: 8X1 + 3X2 + 4X3 >= 10
                       4X1 + 3X2 <= 8
                       X1 , X2 , X3 >= 0

            Minimizar: f(x) = 10X1 + 4X2 + 5X3
            Sujeito a: 8X1 + 3X2 + 4X3 - X4 >= 10
                       4X1 + 3X2 + X5 <= 8
                       X1 , X2 , X3 , X4 , X5 >= 0

                       X4 -> Variável de excesso
                       X5 -> variável de folga

            tabela_base = [[ 'Z', -10, -4,  -5,   0,  0,  0],
                           ['X4',   8,  3,   4,  -1,  0, 10],
                           ['X5',   4,  3,   0,   0,  1,  8]]

            simplex(tabela_base, 'minimizar')

            Resultado: Z=12,5  X1=1,25  X2=0    OK

            -----------------------------------------

            Minimizar: f(x) = -3X1 - 5X2
            Sujeito a: X1 <= 10
                       X2 <=  6
                       3X1 + 2X2 >= 18
                       X1 , X2 >= 0

            tabela_base = [[ 'Z',  3,  5,  0,  0,  0,  0],
                           ['X3',  1,  0,  1,  0,  0,  4],
                           ['X4',  0,  1,  0,  1,  0,  6],
                           ['X5',  3,  2,  0,  0, -1, 18]]

            simplex(tabela_base, 'minimizar')

            Resultado: Z=-42  X1=4  X2=6     OK

            -----------------------------------------

            Minimizar: f(x) = 16X1 + 12X2
            Sujeito a: 8X1 + 4X2 >= 5
                       2X1 + 6X2 >= 3
                       X1 , X2 >= 0

            tabela_base = [[ 'Z', -16, -12,  0,  0,  0],
                           ['X3',   8,   4, -1,  0,  5],
                           ['X4',   2,   6,  0, -1,  3]]

            simplex(tabela_base, 'minimizar')

            Resultado: Z=11,4  X1=0,45  X2=0,35    OK
            -----------------------------------------

            Maximizar: f(x)=10X1 + 12X2
            Sujeito a: 2X1 + 4X2 <= 10
                       X1 + X2 <= 100
                       X1 + 3X2 <= 270
                       X1 , X2 >= 0

            tabela_base = [[ 'Z', -10, -12,  0,  0,    0],
                           ['X3',   1,   1,  1,  0,  100],
                           ['X4',   1,   3,  0,  1,  270]]

            simplex(tabela_base, 'maximizar')

            Resultado: Z=1170,9 X1=15,15 X2=84,85       OK

            -----------------------------------------

            Maximizar: f(x)= 4X1 + X2
            Sujeito a: 2X1 + 3X2 <= 12
                       2X1 + X2 <= 8
                       X1 , X2 >= 0

            tabela_base = [[ 'Z', -4, -1,  0,  0,   0],
                           ['X3',  2,  3,  1,  0,  12],
                           ['X4',  2,  1,  0,  1,   8]]

            simplex(tabela_base, 'maximizar')

            Resultado: Z=16 X1=4 X2=0       OK

            ------------------------------------------

            Maximizar: f(x)= 6X1 - X2
            Sujeito a: 4X1 + X2 ≤ 21
                       2X1 + 3X2 ≥ 13
                       X1 - X2 = -1
                       X1 , X2 ≥ 0

            tabela_base = [[ 'Z', -6,  1,  0,  0,  0,   0],
                           ['X3',  4,  1,  1,  0,  0,  21],
                           ['X4',  2,  3,  0, -1,  0,  13],
                           ['X5', -1,  1,  0,  0,  0,   1]]

            simplex(tabela_base, 'maximizar')

            Resultado: Z=19 X1=4 X2=5       OK

            ------------------------------------------

            Minimizar: f(x)= X1 + X2 + X3
            Sujeito a: -X1 + X2 ≥ 1
                       2X1 - 2X2 - X3 = 2
                       X1 , X2 , X3 ≥ 0

            tabela_base = [[ 'Z', -1, -1, -1,  0,  0,   0],
                           ['X3', -1,  1,  0, -1,  0,   1],
                           ['X4',  2, -2, -1,  0,  0,   2]]

            simplex(tabela_base, 'minimizar')

            Resultado: Z=1  X1=1  X2=0  X3=0      OK

                           """

                tabela_base = [['Z', -1, -1, -1, 0, 0, 0],
                               ['X3', -1, 1, 0, -1, 0, 1],
                               ['X4', 2, -2, -1, 0, 0, 2]]

                simplex(tabela_base, 'minimizar')

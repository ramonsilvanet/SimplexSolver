
print "#" * 20
print "Iniciando o programa"
print "#" * 20
print ""

def simplex(tabela):
    mostrar_tabela(tabela)

def simplex_fase_i(tabela):
    print "fase I"

def simplex_fase_ii(tabela):
    print "fase II"

def mostrar_tabela(tabela):
    for i in range((len(tabela))):
        for j in range(len(tabela[0])):
            print tabela[i][j],'\t',
        print ''



#Forma canonica
tabela_base = [['Z', -3, -2, -5, 0, 0, 0, 0],
               ['X4', 1, 2, 3, 1, 0, 0, 430],
               ['X5', 3, 0, 2, 0, 1, 0, 460],
               ['X6', 1, 4, 0, 0, 0, 1, 420]]


simplex(tabela_base)
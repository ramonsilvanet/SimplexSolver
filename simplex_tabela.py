from __future__ import division
from numpy import *

class Tableau:

    def __init__(self, ppl):
        self.ppl = [1] + ppl
        self.rows = []
        self.cons = []

    def adic_restr(self, expression, value):
        self.rows.append([0] + expression)
        self.cons.append(value)

    def _pivot_coluna(self):
        low = 0
        idx = 0
        for i in range(1, len(self.ppl)-1):
            if self.ppl[i] < low:
                low = self.ppl[i]
                idx = i
        if idx == 0: return -1
        return idx

    def _pivot_linha(self, col):
        rhs = [self.rows[i][-1] for i in range(len(self.rows))]
        lhs = [self.rows[i][col] for i in range(len(self.rows))]
        ratio = []
        for i in range(len(rhs)):
            if lhs[i] == 0:
                ratio.append(99999999 * abs(max(rhs)))
                continue
            ratio.append(rhs[i]/lhs[i])
        return argmin(ratio)

    def exibir_tabela(self):
        print '\n', matrix([self.ppl] + self.rows)

    def _pivot(self, row, col):
        e = self.rows[row][col]
        self.rows[row] /= e
        for r in range(len(self.rows)):
            if r == row: continue
            self.rows[r] = self.rows[r] - self.rows[r][col]*self.rows[row]
        self.ppl = self.ppl - self.ppl[col] * self.rows[row]

    def _verificar_solucao(self):
        if min(self.ppl[1:-1]) >= 0: return 1
        return 0

    def resolver(self):

        # build full tableau
        for i in range(len(self.rows)):
            self.ppl += [0]
            ident = [0 for r in range(len(self.rows))]
            ident[i] = 1
            self.rows[i] += ident + [self.cons[i]]
            self.rows[i] = array(self.rows[i], dtype=float)
        self.ppl = array(self.ppl + [0], dtype=float)

        # solve
        self.exibir_tabela()
        while not self._verificar_solucao():
            c = self._pivot_coluna()
            r = self._pivot_linha(c)
            self._pivot(r,c)
            print '\npivot column: %s\npivot row: %s'%(c+1,r+2)
            self.exibir_tabela()

if __name__ == '__main__':

    """
    max z = 2x + 3y + 2z
    st
    2x + y + z <= 4
    x + 2y + z <= 7
    z          <= 5
    x,y,z >= 0
    """

    t = Tableau([-2,-3,-2])
    t.adic_restr([2, 1, 1], 4)
    t.adic_restr([1, 2, 1], 7)
    t.adic_restr([0, 0, 1], 5)
    t.resolver()
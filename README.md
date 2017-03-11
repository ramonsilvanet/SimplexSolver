# SimplexSolver

**Programa de Pós-Graduação em Ciência da Computação - PPCIC**

**Centro Federal de Educação Tecnológica Celso Suckow da Fonseca - CEFET/RJ**

## Disciplina de Pesquisa Operacional

### Fase I
- determine inicialmente uma partição FACTÍVEL **A = [B,N]**. Isso significa que precisamos de 2 vetores
de índices: básicos e não-básicos.

(b1, B2, B3,...,BN) e (N1, N2, N3,...,Nn.m)

onde,

B1,B2,B3,...BN são os índices das colunas da matriz *A* que pertecem a *B*, chamados de índices básicos.

e

N1,N2,N3,...,Nn.m são os índices das colunas da matriz *A* que não pertecem a *B*

os vetores das variáveis básicas e não básicas são respectivamente

    Xtb = (Xb1, Xb2,...,Xb.m)
    Xtn = (Xn1, Xn2,...,Xn.m)

**Faça a Iteração 1** { *ínicio da iteração do SImplex* }

**Passo 1:** { *cálculo da solução básica* }

    Xˆb = B_-1

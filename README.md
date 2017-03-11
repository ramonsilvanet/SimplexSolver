# SimplexSolver

**Programa de Pós-Graduação em Ciência da Computação - PPCIC**

**Centro Federal de Educação Tecnológica Celso Suckow da Fonseca - CEFET/RJ**

## Disciplina de Pesquisa Operacional


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

#### Passo 1: { *cálculo da solução básica* }

    Xˆb = B¹b (equivalente a resolver  Bxb = b)
    XˆN = 0

#### Passo 2: { *cáluculos dos custos relativos* }

**2.1** { *vetor multiplicador do Simplex* }

    λT = CTB B-1 ( equivalente a resolver Bt λ = CB )

**2.2** { *custos relativos* }

    CˆNj = CNj -  λTaNj; j=1,2,...n-m

**2.3** { *Determinar a variável a entrar na base* }

    CˆNk = MINIMO { CˆNj; j=1,2,...,n-m} (a variável Xnr entra na base)

#### Passo3: { *Teste de otimilidade* }

    Se CˆNk >= 0
        então
            FIM (a solução é ótima)

#### Passo 4: { *Cálculo da direção do simplex* }

    y = B-1 aNk (equivalente a resolver By = aNk)

#### Passo 5: { *Determinar o paso e a variável a sair da base* }

    Se y <= 0
      então
        PARE { o problema não tem solução ótima finita F(X) → ∞}
    Senão
      determine a variável a sair da base pela razão mínima

      Ê = X˜BR / ye = MINIMO { X˜Bi / yi, talque yi > 0; i = 1,2,...,m }

#### Passo 6 : {atualização : nova partição básica, troque A pela L-ésima coluna de B pela k-ésima coluna de N}

**Matriz básica nova :**
B = [ ab1, ab2, ..., abl-1, ank, abl+1, ..., abn]

**Matriz não-básica nova:**
N = [an1, an2, ..., ank-1, abl, ank+1, ..., an-m]



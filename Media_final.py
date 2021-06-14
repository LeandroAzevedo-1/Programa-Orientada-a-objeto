AC1 = int(input('Insira a nota da AC1: '))
AC2 = int(input('Insira a nota da AC2: '))
AC3 = int(input('Insira a nota da AC3: '))

NotaProva = int(input('Insira a nota da Prova: '))
mediaAC = ((AC1+AC2+AC3) /3 * 0.5)
mediaprova = NotaProva * 0.5
Nf = mediaAC + mediaprova
print(f'Sua nota final é {Nf:.2f}')
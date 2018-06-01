n = int(input())
for i in range(0, n):
    j1 = str(input())
    j2 = str(input())
    if j1 == j2:
        if j1 == 'pedra':
            print("Sem ganhador")
        elif j1 == 'papel':
            print("Ambos venceram")
        else:
            print("Aniquilacao mutua")
    elif j1 == 'ataque':
        print("Jogador 1 venceu")
    elif j2 == 'ataque':
        print("Jogador 2 venceu")
    elif j1 == 'pedra':
        print("Jogador 1 venceu")
    elif j2 == 'pedra':
        print("Jogador 2 venceu")

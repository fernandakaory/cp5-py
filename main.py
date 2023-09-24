import random
import csv

# Declaração de variaveis 'vazias':
palavras = []
roda = []
painel = []
acabou = False

# Leitura das palavras e adicionando em no list 'palavras':
with open('Palavras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for linha in csv_reader:
        palavras.extend(linha)

# Cadastrando os jogadores
print("-" * 60)
print("\nDigite o nome dos jogadores")
j1 = input('\tJogador 01: ')
j2 = input('\tJogador 02: ')
j3 = input('\tJogador 03: ')
print("-" * 60)

# Sorteando o primeiro jogador
jogadores = [j1, j2, j3]
indiceJogador = random.randint(0,2)

pontuacao = {j1: 0, j2: 0, j3: 0}
letras_adivinhadas_total = []

print('\n---A dica é: SAVANA---')

# Para cada palavra nas palavras originais, crie uma lista de underscores
for palavra in palavras:
    palavra_oculta = ["_" for _ in palavra]
    painel.append(palavra_oculta)

# Loop principal do jogo
while acabou == False:
    palavrasChutadas = []

    # Exibir o painel atual
    for i in range(len(palavras)):
        palavra_oculta = ""
        for letra in painel[i]:
            palavra_oculta += letra + " "
        print(f"Palavra {i + 1}: {palavra_oculta[:-1]}")

    # Exibir o jogador atual
    print(f"\nÉ a vez de {jogadores[indiceJogador]}")

    # Leitura da Roda e adicionando em no list 'roda':
    with open('Roda.txt', 'r') as txt_file:
        for linha in txt_file:
            roda.append(linha)
        escolha_item = random.choice(roda)
        print(f"Resultado da roda: {escolha_item}")

    if escolha_item != "PERDEU TUDO\n" and escolha_item !="PASSA A VEZ\n":
        #pergunta se quer chutar
        chutar_palavra = False
        total_espacos_nao_adivinhados = sum(palavra.count("_") for palavra in painel)
       
        if total_espacos_nao_adivinhados <= 3:
            resposta = input("Deseja chutar a palavra? (S para sim, qualquer outra tecla para não): ").upper()
            if resposta == "S":
                # Lógica para o jogador tentar adivinhar a palavra
                print(("Chute as palavras na ordem aparente do painel: ").upper())
                for i in range(1,4,1):
                    chute = input().upper()
                    palavrasChutadas.append(chute)
                    
                print(palavrasChutadas,palavras)
                if palavrasChutadas == palavras:
                    print("Palavra correta! Você ganhou pontos extras.")
                    pontuacao[jogadores[indiceJogador]] += 10  # Pontos extras para adivinhar a palavra
                    break
                else:
                    print("Palavra incorreta. Próximo jogador.")
                    indiceJogador = (indiceJogador + 1) % len(jogadores)
                    pontuacao[jogadores[indiceJogador]] = 0

        # Lógica para adivinhar uma letra
        letra = input("Escolha uma letra: ").upper()

        # Verificar se a letra já foi adivinhada
        if letra in letras_adivinhadas_total:
            print("\nEssa letra já foi adivinhada. Tente novamente.")
            continue

        # Adicionar a letra à lista de letras adivinhadas
        letras_adivinhadas_total.append(letra)

        # Verificar se a letra está em alguma das palavras
        acertou = False
        letraAcertada = 0
        for i in range(len(palavras)):
            palavra = palavras[i]
            if letra in palavra:
                acertou = True
                # Atualizar o painel da palavra
                for j in range(len(palavra)):
                    if palavra[j] == letra:
                        painel[i][j] = letra
                        letraAcertada +=1
        pontuacao[jogadores[indiceJogador]] += letraAcertada

        if acertou:
            print("\nLetra correta!")
            print(f"Pontuação da rodada: {pontuacao}")
            print(f"Letras chutada: {letras_adivinhadas_total}")
        
        else:
            print("\nLetra incorreta. Próximo jogador.")
            # escolha_item = 'PASSA A VEZ\n'
            indiceJogador = (indiceJogador + 1) % len(jogadores)
            

        # Verificar se alguém ganhou
        # todas_palavras_adivinhadas = True
        todas_palavras_adivinhadas = True
        for palavra in painel:
            if "_" in palavra:
                todas_palavras_adivinhadas = False
        if todas_palavras_adivinhadas:
            acabou = True

          

    elif escolha_item == 'PASSA A VEZ\n':
        # Alternar para o próximo jogador
        indiceJogador = (indiceJogador + 1) % len(jogadores)
    else:
        pontuacao[jogadores[indiceJogador]] = 0
        indiceJogador = (indiceJogador + 1) % len(jogadores)

print("\nParabéns! Todas as palavras foram adivinhadas.")

# Calcula o vencedor pela quantidade de pontos
maior = -1
for jogador, pontuacao_atual in pontuacao.items():
    if pontuacao_atual > maior:
        maior = pontuacao_atual
        vencedor = jogador

print(f"\nPontuação final: {pontuacao}\n")
print(f"{vencedor} é o vencedor!")
print("Fim do jogo!!!")


from lógica_forca import salvar_palavras, palavra_inesperada, verificar_acerto, examinar_vitoria, analisar_derrota
from interface_forca import clear_screen, desenhar_bonequinho, exibir_palavra_misteriosa, exibir_mensagem_vitoria, exibir_mensagem_derrota, pedir_letra, perguntar_se_deseja_arriscar

import colorama
from colorama import Fore, Back, Style

colorama.init()
colorama.just_fix_windows_console()



def mostrar_dica(palavra: str) -> None:
    """
        Exibe uma dica sobre a palavra sorteada.
    
        Esta função imprime na tela quantas letras a palavra sorteada contém. 
        É útil para ajudar o jogador a ter uma ideia do comprimento da palavra 
        que ele precisa adivinhar.
    
        Parâmetros:
        palavra (str): A palavra que foi sorteada para o jogo. 
    
        Retorna:
        None: Esta função não retorna nenhum valor; ela apenas imprime a dica na tela.
    """

    """Exibe quantas letras a palavra sorteada tem, como uma dica."""
    print(f"Dica a palavra tem {len(palavra)} letras.")


def exibir_ranking(ranking):
    """
        Exibe o ranking dos jogadores com base nos dados armazenados em um arquivo.

        Esta função lê o arquivo 'ranking.txt', que contém os nomes dos jogadores 
        e suas respectivas pontuações, e imprime uma lista ordenada dos jogadores 
        com suas pontuações. Os jogadores são apresentados em ordem decrescente 
        de pontuação.

    """
    """Exibe o ranking com base nos dados do arquivo."""
    with open('ranking.txt', encoding='utf-8') as arq:
        linhas = arq.readlines()
        ranking = []
        
        for i in range(0, len(linhas), 2):
            jogador = linhas[i].strip()
            pontuação = int(linhas[i + 1].strip())
            ranking.append([pontuação, jogador])

        # Ordenar a lista de jogadores pela pontuação
        ordenada = sorted(ranking, reverse=True)
        print("\nRanking dos jogadores:")
        
        for pontuação, jogador in ordenada:
            print(f"{jogador}: {pontuação} pontos")

def escolher_nível(nível):
    """
    Seleciona o conjunto de palavras baseado no nível escolhido e exibe uma mensagem de introdução ao jogo.

    Parâmetros:
    nível (int): O nível de dificuldade selecionado pelo jogador.
                 - 1: Profissões
                 - 2: Desenhos Animados
                 - 3: Comidas
                 - 4: Doramas

    Retorna:
    list: Uma lista de palavras correspondente ao nível escolhido, obtida do arquivo apropriado.
          Retorna None se o nível for inválido.
    
    Exibe:
    Uma mensagem de boas-vindas personalizada para cada nível, utilizando cores específicas.
    """

    if nível == 1:
        palavras = salvar_palavras(f'palavras_profissões{nível}.txt') 
        print(Back.WHITE + Fore.LIGHTMAGENTA_EX + "VAI COMEÇAR O JOGO DA FORCA" + Style.RESET_ALL)
        print(Back.WHITE + Fore.BLUE + "Adivinhe o nome de uma Profissão - Nível 01" + Style.RESET_ALL)

    elif nível == 2:
        palavras = salvar_palavras(f'palavras_desenhos{nível}.txt') 
        print(Back.WHITE + Fore.LIGHTRED_EX + "VAI COMEÇAR O JOGO DA FORCA" + Style.RESET_ALL)
        print(Back.WHITE + Fore.GREEN + "Adivinhe o nome de um Desenho Animado - Nível 02" + Style.RESET_ALL)

    elif nível == 3:
        palavras = salvar_palavras(f'palavras_comidas{nível}.txt') 
        print(Back.WHITE + Fore.LIGHTGREEN_EX + "VAI COMEÇAR O JOGO DA FORCA" + Style.RESET_ALL)
        print(Back.WHITE + Fore.YELLOW + "Adivinhe o nome de uma Comida - Nível 03" + Style.RESET_ALL)
    
    elif nível == 4:
        palavras = salvar_palavras(f'palavras_doramas{nível}.txt') 
        print(Back.WHITE + Fore.LIGHTBLACK_EX  + "VAI COMEÇAR O JOGO DA FORCA" + Style.RESET_ALL)
        print(Back.WHITE + Fore.RED + "Adivinhe o nome de um Dorama - Nível 04" + Style.RESET_ALL)

    else:
        print('Parabéns! Você chegou ao fim.')
    
    return palavras

def verificar(letra, palavra, pala_misteriosa):
    """
    Verifica se a letra fornecida está presente na palavra e atualiza a palavra misteriosa.

    Parâmetros:
    letra (str): A letra fornecida pelo jogador para adivinhar.
    palavra (str): A palavra secreta que o jogador deve adivinhar.
    pala_misteriosa (str): A versão parcialmente revelada da palavra secreta, com letras acertadas
    e os espaços restantes ainda ocultos.

    Retorna:
    str: A palavra misteriosa atualizada com as letras corretas reveladas, caso a letra esteja na palavra.

    Exibe:
    A palavra misteriosa atualizada após a verificação.

    A função utiliza as funções auxiliares:
    - verificar_acerto: Atualiza a palavra misteriosa com a letra acertada.
    - exibir_palavra_misteriosa: Exibe a palavra misteriosa com as letras reveladas.

    Exemplo de uso:
    pala_misteriosa = verificar('A', 'ABACATE', 'A_A_A__')
    """
    if letra in palavra.upper():
        pala_misteriosa = verificar_acerto(palavra, letra, pala_misteriosa)
        exibir_palavra_misteriosa(pala_misteriosa)


def iniciar_jogo(palavras):
    """
    Inicializa a palavra e a palavra misteriosa para o jogo.
    
    Parâmetros:
    palavras (list): A lista de palavras disponíveis para o nível.
    
    Retorna:
    tuple: A palavra escolhida e a palavra misteriosa com underscores.
    """
    palavra = palavra_inesperada(palavras)
    pala_misteriosa = list('_' * len(palavra))
    return palavra, pala_misteriosa


def analisar_letra(palavra, pala_misteriosa, letra, tentativas, acertos):
    """
    Processa a letra fornecida pelo jogador, verificando se está correta ou não.
    
    Parâmetros:
    palavra (str): A palavra secreta que o jogador deve adivinhar.
    pala_misteriosa (list): A versão parcialmente revelada da palavra secreta.
    letra (str): A letra fornecida pelo jogador.
    tentativas (int): O número atual de tentativas erradas.
    acertos (int): O número atual de acertos.
    
    Retorna:
    tuple: A palavra misteriosa atualizada, o número de tentativas, e o número de acertos.
    """
    if letra == ' ':
        print('Espaço detectado. Nenhuma tentativa será contada.')
        return pala_misteriosa, tentativas, acertos
    
    if letra in palavra.upper():
        pala_misteriosa = verificar_acerto(palavra, letra, pala_misteriosa)
        print(f'Bom trabalho! A letra {letra} está na palavra.')
        acertos += 1
    else:
        print(f'A letra {letra} não está na palavra.')
        tentativas += 1
    return pala_misteriosa, tentativas, acertos


def arriscar_palavra(palavra, pontuação):
    """
    Permite ao jogador arriscar a palavra completa após acumular 3 acertos.
    
    Parâmetros:
    palavra (str): A palavra secreta que o jogador deve adivinhar.
    pontuação (int): A pontuação atual do jogador.
    
    Retorna:
    tuple: A pontuação atualizada e uma flag indicando se o jogo terminou.
    """
    chute = input('Digite a palavra completa: ').upper()
    if chute == palavra.upper():
        exibir_mensagem_vitoria(palavra)
        pontuação += 100
        return pontuação, True
    else:
        exibir_mensagem_derrota(palavra)
        print(f'Sua pontuação atual é {pontuação} pontos')
        return pontuação, False


def jogar_nível(palavras, pontuação):
    """
    Gerencia o jogo dentro de um nível específico, permitindo ao jogador adivinhar letras
    e, se for o caso, arriscar a palavra após 3 acertos.

    Parâmetros:
    palavras (list): Lista de palavras para o nível atual.
    pontuação (int): Pontuação atual do jogador.
    """

    palavra, pala_misteriosa = iniciar_jogo(palavras)  
    tentativas = 0  
    acertos = 0  
    mostrar_dica(palavra)  

    while True:  
        desenhar_bonequinho(tentativas)  
        exibir_palavra_misteriosa(pala_misteriosa)  
        letra = pedir_letra()  
        
        pala_misteriosa, tentativas, acertos = analisar_letra(palavra, pala_misteriosa, letra, tentativas, acertos)  
        
        print(f'Pontuação: {pontuação}, Acertos: {acertos}')  
        
        if verificar_vitoria(pala_misteriosa, palavra):  
            pontuação += 100  
            break  

        if acertos >= 3:
            exibir_palavra_misteriosa(pala_misteriosa)  
            opcao = perguntar_se_deseja_arriscar()  
            if opcao == 'S':  
                pontuação, terminou = arriscar_palavra(palavra, pontuação) 
                if terminou:  
                    break  
                else:
                    return pontuação

        if verificar_derrota(tentativas, palavra):  
            return pontuação  

    return pontuação  


def verificar_vitoria(pala_misteriosa, palavra):
    """
    Verifica se o jogador venceu.

    Parâmetros:
    acertos (int): Número de acertos do jogador.
    pala_misteriosa (list): A palavra misteriosa que o jogador está tentando adivinhar.
    palavra (str): A palavra correta.

    Retorna:
    bool: True se o jogador venceu, False caso contrário.
    """
    if examinar_vitoria(pala_misteriosa):
        exibir_mensagem_vitoria(palavra)
        return True
    return False


def verificar_derrota(tentativas, palavra):
    """
    Verifica se o jogador perdeu.

    Parâmetros:
    tentativas (int): O número de tentativas feitas pelo jogador.
    palavra (str): A palavra correta.

    Retorna:
    bool: True se o jogador perdeu, False caso contrário.
    """
    if analisar_derrota(tentativas):
        desenhar_bonequinho(tentativas)
        exibir_mensagem_derrota(palavra)
        return True
    return False

def renovar_ranking(jogador, pontuação, ranking):
    """
    Atualiza o arquivo de ranking, registrando o nome do jogador e sua pontuação.

    Parâmetros:
    jogador (str): O nome do jogador que terminou o jogo.
    pontuação (int): A pontuação obtida pelo jogador.

    Funcionalidade:
    - Abre o arquivo 'ranking.txt' em modo de adição (append).
    - Escreve o nome do jogador e a pontuação em linhas separadas.
    - Usa codificação UTF-8 para garantir compatibilidade com caracteres especiais.

    Exemplo de uso:
    renovar_ranking('João', 300)
    """
    ranking[jogador] = pontuação
    with open('ranking.txt', 'a', encoding='utf-8') as arq:
        arq.write(f'{jogador}\n')
        arq.write(f'{pontuação}\n')


def jogo_da_forca():
    """
    Executa o jogo da forca, permitindo que o jogador avance por diferentes níveis.

    Cada nível apresenta um tema diferente (profissões, desenhos animados, comidas, doramas).
    O jogador tenta adivinhar a palavra correta letra por letra, com a opção de arriscar a palavra completa.

    O jogo termina quando o jogador vence todos os níveis ou esgota as tentativas em um nível.
    """
    ranking = {}  # Lista para armazenar os jogadores e suas pontuações

    while True:
        jogador = input("Digite seu nome, jogador(a). Se quiser sair digite 'N': ")
        if jogador.upper() == 'N':
            break

        pontuação = 0
        nível = 1

        while nível <= 4:  # Loop para permitir o progresso de nível
            if nível != 1:
                próximo = input(f'Deseja ir para o próximo nível? (S/N)')
                if próximo.upper() == 'N':
                    break
            palavras = escolher_nível(nível)
            pontuação = jogar_nível(palavras, pontuação)

            if pontuação == 0:
                print(f"Fim de jogo, {jogador}! Sua pontuação total foi: {pontuação} pontos.")
                break
            
            if nível == 4:
                print(f"PARABÉNS! VOCÊ CHEGOU AO FIM, {jogador}!")
                break
 
            nível += 1
          

        renovar_ranking(jogador, pontuação, ranking)
        print(f"Fim de jogo, {jogador}! Sua pontuação total foi: {pontuação} pontos.")
        

        # Pergunta se há mais jogadores
        jogadores = input("Há mais jogadores? (S/N): ").strip().upper()
        if jogadores != 'S':
            exibir_ranking(ranking)
            break  # Encerra o loop se não houver mais jogadores
        

    print("Obrigado por jogar!")


if __name__ == "__main__":
    jogo_da_forca()
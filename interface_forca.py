import os
import colorama
from colorama import Fore, Back, Style
import time

colorama.init()
colorama.just_fix_windows_console()


def clear_screen() -> None:
    """
    Limpa a tela do terminal.
    Utiliza o comando do sistema operacional para limpar a tela.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def animar_bonequinho() -> None:
    """
    Anima o bonequinho da forca.
    A animação é repetida 4 vezes para simular o movimento do boneco.
    """
    frames = [
        [
            "  _____ ",
            " |     |",
            " |     O",
            " |    /|\\",
            " |    / \\",
            " |",
            "_|_"
        ],
        [
            "  _____ ",
            " |     |",
            " |     O",
            " |   /|\\ ",
            " |   / \\ ",
            " |",
            "_|_"
        ],
        [
            "  _____ ",
            " |     |",
            " |     O",
            " |    /|\\",
            " |   / \\ ",
            " |",
            "_|_"
        ],
        [
            "  _____ ",
            " |     |",
            " |     O",
            " |   /|\\ ",
            " |    / \\",
            " |",
            "_|_"
        ],
    ]

    for _ in range(4):  
        for frame in frames:
            os.system('cls' if os.name == 'nt' else 'clear')  
            for line in frame:
                print(line)
            time.sleep(0.3)


def desenhar_bonequinho(tentativas: int) -> None:
    """
    Desenha o bonequinho com base no número de tentativas incorretas.
    """
    estagios = [
        """
          _____ 
         |     |
         |     
         |    
         |     
         |    
        _|_
        """,
        """
          _____ 
         |     |
         |     O
         |    
         |     
         |    
        _|_
        """,
        """
          _____ 
         |     |
         |     O
         |     |
         |     
         |    
        _|_
        """,
        """
          _____ 
         |     |
         |     O
         |    /|
         |     
         |    
        _|_
        """,
        """
          _____ 
         |     |
         |     O
         |    /|\\
         |     
         |    
        _|_
        """,
        """
          _____ 
         |     |
         |     O
         |    /|\\
         |    / 
         |    
        _|_
        """,
        """
          _____ 
         |     |
         |     O
         |    /|\\
         |    / \\
         |    
        _|_
        """
    ]
    print(estagios[tentativas])


def exibir_palavra_misteriosa(pala_misteriosa: list[str]) -> None:
    """Exibe a palavra oculta com as letras já descobertas."""
    print(Fore.GREEN + ' '.join(pala_misteriosa) + Style.RESET_ALL)


def exibir_mensagem_vitoria(palavra: str) -> None:
    """Exibe uma mensagem de vitória."""
    print(Fore.GREEN + f'Parabéns! Você adivinhou a palavra {palavra}!' + Style.RESET_ALL)


def exibir_mensagem_derrota(palavra: str) -> None:
    """Exibe uma mensagem de derrota."""
    print(Fore.RED + f'Você perdeu! A palavra correta era {palavra}.' + Style.RESET_ALL)


def pedir_letra() -> str:
    """Solicita uma letra ao jogador."""
    return input('Digite uma letra: ').upper()



def perguntar_se_deseja_arriscar() -> str:
    """Pergunta se o jogador quer arriscar a palavra completa."""
    return input('Você quer arriscar a palavra? (S/N): ').upper()

def jogo_da_forca(palavras_por_nivel: dict[int, list[str]]) -> None:
    nivel_atual = 1
    max_niveis = 4

    while nivel_atual <= max_niveis:
        palavras = palavras_por_nivel[nivel_atual]
        palavra = palavras[0].upper()  # Escolhe a primeira palavra da lista do nível atual
        pala_misteriosa = list('_' * len(palavra))
        tentativas = 0
        max_tentativas = 6
        acertos = 0


        while tentativas < max_tentativas:
            clear_screen()
            desenhar_bonequinho(tentativas)
            exibir_palavra_misteriosa(pala_misteriosa)

            letra = pedir_letra()

            if letra in palavra:
                pala_misteriosa = verificar_acerto(palavra, letra, pala_misteriosa)
                acertos += 1

                if '_' not in pala_misteriosa:
                    exibir_mensagem_vitoria(palavra)
                    break

                if acertos >= 3:
                    opcao = perguntar_se_deseja_arriscar()
                    if opcao == 'S':
                        chute = input('Digite a palavra completa: ').upper()
                        if chute == palavra:
                            exibir_mensagem_vitoria(palavra)
                            break
                        else:
                            exibir_mensagem_derrota(palavra)
                            return  # O jogo acaba se o chute for incorreto
            else:
                print(Fore.RED + f'A letra {letra} não está na palavra.' + Style.RESET_ALL)
                tentativas += 1

        if tentativas == max_tentativas:
            desenhar_bonequinho(tentativas)
            exibir_mensagem_derrota(palavra)
            return  # O jogo acaba se o jogador perder

        # Avançar para o próximo nível
        nivel_atual += 1
        if nivel_atual <= max_niveis:
            print(Fore.YELLOW + f"\nPrepare-se para o Nível {nivel_atual}!" + Style.RESET_ALL)
            time.sleep(2)

    print(Fore.GREEN + "Parabéns! Você completou todos os níveis!" + Style.RESET_ALL) 
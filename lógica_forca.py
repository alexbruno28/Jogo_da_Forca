import random as rd

def salvar_palavras(arquivo='palavras_profissões.txt') -> list[str]:
    """
    Carrega as palavras de um arquivo.

    Esta função lê um arquivo de texto contendo palavras e as retorna em uma lista.
    
    Parâmetros:
    arquivo (str): O nome do arquivo de onde as palavras serão carregadas. O padrão é 'palavras_profissões.txt'.

    Retorna:
    list[str]: Uma lista contendo as palavras carregadas do arquivo.
    """
    with open (arquivo, 'r', encoding='utf-8') as f:
        return [linhas.strip() for linhas in f.readlines()]


def salvar_palavras_2(arquivo='palavras_desenhos.txt') -> list[str]:
    """
    Carrega as palavras de um arquivo.

    Esta função lê um arquivo de texto contendo palavras relacionadas a desenhos e as retorna em uma lista.

    Parâmetros:
    arquivo (str): O nome do arquivo de onde as palavras serão carregadas. O padrão é 'palavras_desenhos.txt'.

    Retorna:
    list[str]: Uma lista contendo as palavras carregadas do arquivo.
    """
    with open (arquivo, 'r', encoding='utf-8') as f:
        return [linhas.strip() for linhas in f.readlines()]
    

def salvar_palavras_3(arquivo='palavras_comidas.txt') -> list[str]:
    """
    Carrega as palavras de um arquivo.

    Esta função lê um arquivo de texto contendo palavras relacionadas a comidas e as retorna em uma lista.

    Parâmetros:
    arquivo (str): O nome do arquivo de onde as palavras serão carregadas. O padrão é 'palavras_comidas.txt'.

    Retorna:
    list[str]: Uma lista contendo as palavras carregadas do arquivo.
    """
    with open (arquivo, 'r', encoding='utf-8') as f:
        return [linhas.strip() for linhas in f.readlines()]


def salvar_palavras_4(arquivo='palavras_doramas.txt') -> list[str]:
    """
    Carrega as palavras de um arquivo.

    Esta função lê um arquivo de texto contendo palavras relacionadas a doramas e as retorna em uma lista.

    Parâmetros:
    arquivo (str): O nome do arquivo de onde as palavras serão carregadas. O padrão é 'palavras_doramas.txt'.

    Retorna:
    list[str]: Uma lista contendo as palavras carregadas do arquivo.
    """
    with open (arquivo, 'r', encoding='utf-8') as f:
        return [linhas.strip() for linhas in f.readlines()]


def palavra_inesperada(lista: list[str]) -> str:
    """
    Seleciona uma palavra aleatória de uma lista.

    Sorteia uma palavra de uma lista de palavras fornecida como argumento.

    Args:
        lista (list): Lista de palavras para o sorteio.

    Returns:
        str: A palavra sorteada aleatoriamente.
    """

    tamanho = len(lista)
    sorteio = rd.randint(0,tamanho -1)    
    palavra_inesperada = lista[sorteio]
    return palavra_inesperada



def encontrar(palavra: str, letra: str) -> list[int]:
    """
    Encontra todas as posições de uma letra em uma palavra.

    Percorre a palavra e retorna uma lista contendo os índices em que a letra aparece.

    Args:
        palavra (str): A palavra onde se deseja encontrar a letra.
        letra (str): A letra que se quer procurar na palavra.

    Returns:
        list: Lista de índices onde a letra aparece na palavra.
    """
    posicoes = []

    for i in range(0,len(palavra)):

        if palavra[i].upper() == letra:
            posicoes.append(i)
    return posicoes


def verificar_acerto(palavra: str, letra: str, pala_misteriosa: list[str]) -> list[str]:
    """
    Atualiza a palavra oculta com a letra encontrada.

    Esta função recebe a palavra correta, a letra que foi adivinhada e a palavra misteriosa atual.
    Se a letra estiver na palavra, suas posições são reveladas na palavra misteriosa.

    Parâmetros:
    palavra (str): A palavra correta que o jogador está tentando adivinhar.
    letra (str): A letra que o jogador adivinhou.
    pala_misteriosa (list[str]): A representação atual da palavra oculta.

    Retorna:
    list[str]: A lista atualizada da palavra misteriosa com a letra adicionada nas posições corretas.
    """
    posicoes = encontrar(palavra, letra)
    for pos in posicoes:
        pala_misteriosa[pos] = letra
    return pala_misteriosa


def examinar_vitoria(pala_misteriosa: list[str]) -> bool:
    """
    Verifica se o jogador completou a palavra.

    Esta função analisa a representação atual da palavra oculta e determina se
    não existem mais caracteres sublinhados, o que indicaria que o jogador
    adivinhou todas as letras da palavra.

    Parâmetros:
    pala_misteriosa (list[str]): A representação atual da palavra oculta.

    Retorna:
    bool: True se o jogador completou a palavra, False caso contrário.
    """
    return '_' not in pala_misteriosa


def analisar_derrota(tentativas: int):
    """
    Verifica se o jogador perdeu o jogo.

    Esta função compara o número de tentativas feitas pelo jogador com o número
    máximo de tentativas permitidas. Se o jogador atingir ou ultrapassar esse
    limite, a função retorna True, indicando que o jogador perdeu.

    Parâmetros:
    tentativas (int): O número atual de tentativas feitas pelo jogador.
    max_tentativas (int): O número máximo de tentativas permitidas (padrão é 6).

    Retorna:
    bool: True se o jogador perdeu, False caso contrário.
    """
    return tentativas == 6 
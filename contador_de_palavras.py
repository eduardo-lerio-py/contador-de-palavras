import string


def cortar_palavras(frase):
    tabela = str.maketrans("", "", string.punctuation)
    return frase.lower().translate(tabela).split()


def contar_palavras(palavras):
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem


def palavra_mais_comum(contagem):
    mais_comum = ""
    maior = 0
    for palavra, vezes in contagem.items():
        if vezes > maior:
            maior = vezes
            mais_comum = palavra
    return mais_comum, maior


def main():
    frase = input("Insira a frase: ")
    palavras = cortar_palavras(frase)
    if not palavras:
        print("Não há palavras!")
        return
    contagem = contar_palavras(palavras)
    mais_comum, maior = palavra_mais_comum(contagem)
    print(f"Sua frase tem {len(palavras)} palavras."
          f"\nA palavra mais comum foi {mais_comum}, aparecendo {maior} vezes.")


if __name__ == "__main__":
    main()

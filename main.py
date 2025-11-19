import unicodedata

def remover_acentos(txt):
    return ''.join(
        c for c in unicodedata.normalize('NFD', txt)
        if unicodedata.category(c) != 'Mn'
    )

def cifra_cesar(texto, chave, modo):
    if modo == 2:
        chave = -chave

    resultado = ""
    for c in texto:
        base = remover_acentos(c)
        if 'a' <= base <= 'z':
            v = (ord(base) - ord('a') + chave) % 26
            resultado += chr(v + ord('a'))
        elif 'A' <= base <= 'Z':
            v = (ord(base) - ord('A') + chave) % 26
            resultado += chr(v + ord('A'))
        else:
            resultado += base
    return resultado

def main():
    print("=== Cifra de César ===")
    try:
        opcao = int(input("Digite 1 para Criptografar ou 2 para Descriptografar:\n> "))
    except ValueError:
        print("Entrada inválida.")
        return

    texto = input("Digite a palavra a ser Criptografada ou Descriptografada:\n> ")
    try:
        chave = int(input("Digite o Shift (chave):\n> "))
    except ValueError:
        print("Entrada inválida.")
        return

    resultado = cifra_cesar(texto, chave, opcao)
    print(f"\nResultado: {resultado}")


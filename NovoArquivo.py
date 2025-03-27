def calcular_unleashed(ano):
    if ano > 2008:
        return ano - 2008
    else:
        return 2008 - ano

def main():
    try:
        ano = int(input("Digite um ano: "))
        unleashed = calcular_unleashed(ano)
        print(f"O ano descrito está a {unleashed:.2f} anos de distância do lançamento de Sonic Unleashed OMG!!")
    except ValueError:
        print("ESCREVE CERTO UM ANO DESGRAMA")

main()
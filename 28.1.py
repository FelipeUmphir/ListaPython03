#Início
def ajuste(PA, VM):
    if (VM >= 1000) and (PA >= 80):
        NP = (PA * 0.95)
    elif (1000 > VM >= 500) and (80 > PA >= 30):
        NP = (PA * 1.15)
    elif (VM < 500) and (PA < 30):
        NP = (PA * 1.1)
    else:
        NP = PA
    print(f"O novo preço do produto é {NP} reais")

def main():
    PA = float(input("Digite o preço atual do produto:"))
    VM = float(input("Digite a média mensal do produto:"))
    ajuste(PA, VM)

main()
#Fim
#Início
A = 0
B = 0
C = 0
D = 0

def raiz():
    global A, B, C, D

    A = int(input('Digite o valor do coeficiente a:'))
    B = int(input('Digite o valor do coeficiente b:'))
    C = int(input('Digite o valor do coeficiente c:'))

    D = (B ** 2) - (4 * A * C)
    
    if (D >= 0):
        print("Existem raízes reais")
        if (D == 0):
            R1 = (-B) / 2 * A
            print(f"O valor da raiz é {R1}")
        else:
            R1 = (-B + D ** 0.5) / 2 * A
            R2 = (-B - D ** 0.5) / 2 * A
            print(f"O valor das raízes é {R1} e {R2}")
    else:
        print("Não existem raízes reais")

def main():
    raiz()

main()
#Fim
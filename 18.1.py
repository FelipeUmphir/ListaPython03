#Início
x = 0
y = 0
d = 0

def subtração():
    global x, y, d

    x = int(input("Digite o 1º valor:"))
    y = int(input("Digite o 2º valor:"))

    if (x >= y):
        d = (x - y)
    else:
        d = (y - x)
    print(f"A diferença do maior pelo menor é {d}")

def main():
    subtração()

main()
#Fim
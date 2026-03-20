#Início
x = 0
y = 0

def crescente():
    global x, y

    x = int(input("Digite o 1º valor:"))
    y = int(input("Digite o 2º valor:"))

    if (x > y):
        print(f"Os valores em ordem crescente são: {y} e {x}")
    else:
        print(f"Os valores em ordem crescente são: {x} e {y}")

def main():
    crescente()

main()
#Fim

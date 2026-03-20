#Início
x = 0
y = 0

def maior():
    global x, y
    
    x = int(input("Digite o 1º valor:"))
    y = int(input("Digite o 2º valor:"))

    if (x >= y):
        print(f"O maior valor é {x}")
    else:
        print(f"O maior valor é {y}")

def main():
    maior()

main()
#Fim
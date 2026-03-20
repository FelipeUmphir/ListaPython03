#Início
x = 0
x1 = 0
x2 = 0

def divisível():
    global x, x1, x2

    x = int(input("Digite um valor:"))
    x1 = (x % 2)
    x2 = (x % 3)
    
    if (x1 == 0):
        print("É divisível por 2")
    else:
        print("Não é divisível por 2")
    if (x2 == 0):
        print("É divisível por 3")
    else:
        print("Não é divisível por 3")

def main():
    divisível()

main()
#Fim
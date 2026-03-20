#Início
x = 0
y = 0

def multiplo():
    global x, y

    x = int(input("Digite o 1º valor:"))
    y = int(input("Digite o 2º valor:"))
    
    if (x >= y):
        z = (x % y)
        if (z == 0):
            print("O maior valor é multiplo do menor")
        else:
            print("O maior valor não é multiplo do menor")
    else:
        z = (y % x)
        if (z == 0):
            print("O maior valor é multiplo do menor")
        else:
            print("O maior valor não é multiplo do menor")

def main():
    multiplo()

main()
#Fim
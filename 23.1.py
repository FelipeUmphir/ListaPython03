#Início
A = 0
B = 0
C = 0
D = 0
valores = 0

def crescente():
    global A, B, C, D, valores

    A = int(input("Digite a 1ª valor:"))
    B = int(input("Digite a 2ª valor:"))
    C = int(input("Digite a 3ª valor:"))
    D = int(input("Digite a 4ª valor:"))
    
    valores = [A, B, C, D]
    valores.sort()
    print(f"Os valores em ordem crescente são: {valores}")

def main():
    crescente()

main()
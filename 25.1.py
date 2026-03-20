#Início
HI = 0
HF = 0
MI = 0
MF = 0
IT = 0
FT = 0
DF = 0
DH = 0
DM = 0

def duração():
    global HI, HF, MI, MF, IT, FT, DF, DH, DM

    HI = int(input("Digite a hora de início do jogo:"))
    HF = int(input("Digite a hora de termino do jogo:"))
    MI = int(input("Digite o minuto de início do jogo:"))
    MF = int(input("Digite o minuto de termino do jogo:"))
    
    IT = MI + (HI * 60)
    FT = MF + (HF * 60)
    
    if (HF < HI):
        DF = (FT + 1440) - IT
    else:
        DF = (FT - IT)
    
    DH = (DF // 60)
    DM = (DF % 60)
    print(f"O tempo do jogo foi de {DH} horas e {DM} minutos")

def main():
    duração()

main()
#Fim

import time

ligado = False
tempo = 0
temperatura = 0

def ligar(novo_tempo, nova_temperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado = True 
        tempo = novo_tempo
        temperatura = nova_temperatura
        print(f'maquina de louça ligado por {tempo} segundos na temperatura {temperatura}')
        iniciar_cronometro(tempo)
        desligar()
    else:
        print("o maquina de louça esta ligado")

        def desligar():
            global ligado
            if ligado:
                 ligado = False
                 print('maquina de louça esta desligado')
            else:
                print('maquina de louça esta desligado')

def status():
    if ligado:
        print(f'tempo {tempo} segundos /n potencia: {temperatura}')
    else:
        print(f"desligar")

def iniciar_cronometro(segundos):
    while segundos>0:
        print(f"tempo restante: {segundos} segundos")
        time.sleep(1)
        segundos -=1 # segundos = segundos -1
    print("\n tempo esgotado")

#predefiniçoes do microondas

def vidro():
    ligar(120, 100)

def plastico():
    ligar(60, 21)

def metal():
    ligar(120, 30)

opcao = int(input("escolha 1 para vidro, 2 para plastico, 3 para metal:"))
if opcao==1:
    vidro()
elif opcao==2:
    plastico()
elif opcao==3:
    metal()

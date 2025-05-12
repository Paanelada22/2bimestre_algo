import time

ligado = False
tempo = 0
potencia = 0

def ligar(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True 
        tempo = novo_tempo
        potencia = nova_potencia
        print(f'microondas ligado por {tempo} segindos na potencia {potencia}')
        iniciar_cronometro(tempo)
        desligar()
    else:
        print("o microondas esta ligado")

        def desligar():
            global ligado
            if ligado:
                 ligado = False
                 print('microondas esta desligado')
            else:
                print('microondas esta desligado')

def status():
    if ligado:
        print(f'tempo {tempo} segundos /n potencia: {potencia}')
    else:
        print(f"desligar")

def iniciar_cronometro(segundos):
    while segundos>0:
        print(f"tempo restante: {segundos} segundos")
        time.sleep(1)
        segundos -=1 # segundos = segundos -1
    print("\n tempo esgotado")

#predefiniçoes do microondas

def pipoca():
    ligar(30, 100)

pipoca()
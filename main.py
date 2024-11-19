from recursos.funcoes import limparTela
import pygame
import random
import time

pygame.init()
tamanho = (1000,592)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("recursos/icone.ico")

pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")

branco = (255,255,255)
preto = (0,0,0)
#fundo = pygame.image.load("recursos/ADICIONE O FUNDO DE 3 PISTAS AQUI.png")
fundo = pygame.image.load("recursos/fundo.png")
carroVermelho = pygame.image.load("recursos/carro1.png")
carroAmarelo = pygame.image.load("recursos/carro2.png")
carroAzul = pygame.image.load("recursos/carro3.png")
fundo2 = pygame.image.load("recursos/telaFinal.png")
#fundo2 = pygame.image.load("recursos/ADICIONE O FUNDO FINAL AQUI.png")

#ALTERE AS POSIÇÕES DE ACORDO COM O TAMANHO DA PISTA AQUI:
movXCar1 = 0
movXCar2 = 0
movXCar3 = 0
posYCar1 = 45
posYCar2 = 115
posYCar3 = 190
dPixel = 0



vitoria = pygame.mixer.Sound("recursos/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("recursos/trilha.mp3")
pygame.mixer.music.play(-1) #-1 looping, 1,2 3 vezes
somDaVitoria = False

acabou = False


while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
   
    tela.fill( branco )
    tela.blit(fundo, (0,0))
    tela.blit(carroVermelho, (movXCar1,posYCar1))
    tela.blit(carroAmarelo, (movXCar2,posYCar2))
    tela.blit(carroAzul, (movXCar3,posYCar3))
    
    #fórmulas:
    dist_1_2 = abs(movXCar1 - movXCar2)
    dist_1_3 = abs(movXCar1 - movXCar3)
    dist_2_3 = abs(movXCar2 - movXCar3)
    
    d1_2 = f"Distância Carro Vermelho-Amarelo: {dist_1_2}"
    d1_3 = f"Distância Carro Vermelho-Azul: {dist_1_3}"
    d2_3 = f"Distância Carro Amarelo-Azul: {dist_2_3}"
    
    if movXCar1 >= movXCar2 and movXCar1 >= movXCar3:
        vencedor = 'Vermelho'
        if movXCar2 >= movXCar3:  # se o carro amarelo é o segundo colado
            dPixiel = movXCar1 - movXCar2
            secLugar = 'Amarelo'
            tercLugar = 'Azul'
            car2_car3 = movXCar2 - movXCar3
        else:  #o carro azul é o segundo colocado
            dPixiel = movXCar1 - movXCar3
            secLugar = 'Azul'
            tercLugar = 'Amarelo'
            car2_car3 = movXCar3 - movXCar2

    elif movXCar2 >= movXCar1 and movXCar2 >= movXCar3:
        vencedor = 'Amarelo'
        if movXCar1 >= movXCar3:  #se o carro vermelho é o segundo colocado
            dPixiel = movXCar2 - movXCar1
            secLugar = 'Vermelho'
            tercLugar = 'Azul'
            car2_car3 = movXCar1 - movXCar3
        else:  #o carro azul é o segundo colocado
            dPixiel = movXCar2 - movXCar3
            secLugar = 'Azul'
            tercLugar = 'Vermelho'
            car2_car3 = movXCar3 - movXCar1

    else:  #o carro azul é o vencedor
        vencedor = 'Azul'
        
        if movXCar1 > movXCar2:  #o carro vermelho é o segundo colocado
            dPixiel = movXCar3 - movXCar1
            secLugar = 'Vermelho'
            tercLugar = 'Amarelo'
            car2_car3 = movXCar3 - movXCar1
        else:  #o carro amarelo é o segundo colocado
            dPixiel = movXCar1 - movXCar2
            secLugar = 'Amarelo'
            tercLugar = 'Vermelho'
            car2_car3 = movXCar2 - movXCar1

    #textos vencedors
    fonte = pygame.font.Font('freesansbold.ttf',24) #ttf é o arquivo da font
    textovencedor = fonte.render(f'{vencedor} está {dPixel} pixels na frente do carro {secLugar}', True, branco)
    tela.blit(textovencedor, (135,25))

    fonte = pygame.font.Font('freesansbold.ttf',20)#ttf é o arquivo da font
    textoSegundo = fonte.render(f'{secLugar} está {car2_car3} pixels na frente do carro {tercLugar}', True, branco)
    tela.blit(textoSegundo, (135,50))
    
    if not acabou :
        movXCar1 = movXCar1 + random.randint(0,8)
        movXCar2 = movXCar2 + random.randint(0,8)
        movXCar3 = movXCar3 + random.randint(0,8)
    else:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
    
    if movXCar1 > 1000:
        movXCar1 = 0
        posYCar1 = 340
        
    if movXCar2 > 1000:
        movXCar2 = 0
        posYCar2 = 420
    
    if movXCar3 > 1000:
        movXCar3 = 0
        posYCar3 = 490
    
    fonte = pygame.font.Font("freesansbold.ttf",64)
    textoVermelho = fonte.render("Vermelho Ganhou!", True, branco)
    textoAmarelo = fonte.render("Amarelo Ganhou!", True, branco)
    textoAzul = fonte.render("Azul Ganhou!", True, branco)
    
    #variavel das dist
    textoDist_1_2 = fonte.render(d1_2, True, branco)
    textoDist_1_3 = fonte.render(d1_3, True, branco)
    textoDist_2_3 = fonte.render(d2_3, True, branco)
    
    distanciaPixel = 0
    if movXCar1 >= movXCar2 and movXCar1 >= movXCar3:
        firstPlace = 'Vermelho'
        if movXCar2 >= movXCar3:  # se o carro amarelo é o segundo colado
            distanciaPixel = abs(movXCar1 - movXCar2)
            secondPlace = 'Amarelo'
            thirdPlace = 'Azul'
            distancia_segundo_terceiro = abs(movXCar2 - movXCar3)
        else:  #o carro azul é o segundo colocado
            distanciaPixel = abs(movXCar1 - movXCar3)
            secondPlace = 'Azul'
            thirdPlace = 'Amarelo'
            distancia_segundo_terceiro = abs(movXCar3 - movXCar2)

    elif movXCar2 >= movXCar1 and movXCar2 >= movXCar3:
        firstPlace = 'Amarelo'
        if movXCar1 >= movXCar3:  #se o carro vermelho é o segundo colocado
            distanciaPixel = abs(movXCar2 - movXCar1)
            secondPlace = 'Vermelho'
            thirdPlace = 'Azul'
            distancia_segundo_terceiro = abs(movXCar1 - movXCar3)
        else:  #o carro azul é o segundo colocado
            distanciaPixel = abs(movXCar2 - movXCar3)
            secondPlace = 'Azul'
            thirdPlace = 'Vermelho'
            distancia_segundo_terceiro = abs(movXCar3 - movXCar1)

    else:  #o carro azul é o vencedor
        firstPlace = 'Azul'
        if movXCar1 > movXCar2:  #o carro vermelho é o segundo colocado
            distanciaPixel = abs(movXCar3 - movXCar1)
            secondPlace = 'Vermelho'
            thirdPlace = 'Amarelo'
            distancia_segundo_terceiro = abs(movXCar3 - movXCar1)
        else:  #o carro amarelo é o segundo colocado
            distanciaPixel = abs(movXCar1 - movXCar2)
            secondPlace = 'Amarelo'
            thirdPlace = 'Vermelho'
            distancia_segundo_terceiro = abs(movXCar2 - movXCar1)
    
    if acabou == True:
        if acabou:
            tela.blit(fundo2, (0,0))
            # Ajuste na tela final do game - Junin
            #tela.fill(branco)

            #commit de tela de fundo
            #tela.blit(ADICIONE O FUNDO FINAL AQUI, (0,0))

        fonte_final = pygame.font.SysFont("freesansbold.ttf", 32)
        distancia_primeiro_segundo = abs(movXCar1 - movXCar2) if firstPlace == 'Vermelho' and secondPlace == 'Amarelo' or firstPlace == 'Amarelo' and secondPlace == 'Vermelho' else abs(movXCar1 - movXCar3) if firstPlace == 'Vermelho' else abs(movXCar2 - movXCar3)
        distancia_segundo_terceiro = abs(movXCar2 - movXCar3) if thirdPlace == 'Azul' else abs(movXCar1 - movXCar2)

        titulo_vencedor = fonte_final.render(f'{firstPlace} Ganhou!', True, branco)

        # Textos para cada colocação com distâncias
        # Textos ajustados aqui - Junin
        texto_vencedor_final = fonte_final.render(f'1º lugar: Carro {firstPlace}', True, branco)
        texto_distancia_1_2 = fonte_final.render(f'Vantagem sobre o 2º lugar: {distancia_primeiro_segundo} pixels', True, branco)
        texto_segundo_final = fonte_final.render(f'2º lugar: Carro {secondPlace}', True, branco)
        texto_distancia_2_3 = fonte_final.render(f'Vantagem sobre o 3º lugar: {distancia_segundo_terceiro} pixels', True, branco)
        texto_terceiro_final = fonte_final.render(f'3º lugar: Carro {thirdPlace}', True, branco)

        tela.blit(texto_vencedor_final, (140, 170)) 
        tela.blit(texto_distancia_1_2, (140, 200))  
        tela.blit(texto_segundo_final, (140, 255))  
        tela.blit(texto_distancia_2_3, (140, 285))  
        tela.blit(texto_terceiro_final, (140, 340))
        # Distâncias dos textos ajustadas - Junin

        
    
    if posYCar1 == 340 and movXCar1 >= 908 and (movXCar1 > movXCar2 and movXCar3):
        tela.blit(textoVermelho, (140,80))
        acabou = True
    
    elif posYCar2 == 420 and movXCar2 >= 908 and (movXCar2 > movXCar1 and movXCar3):
        tela.blit(textoAmarelo, (140,80))
        acabou = True
    
    elif posYCar3 == 490 and movXCar3 >= 908 and (movXCar3 > movXCar1 and movXCar2):
        tela.blit(textoAzul, (140,80))
        acabou = True
    
    pygame.display.update()
    clock.tick(80)
pygame.quit()

#teste
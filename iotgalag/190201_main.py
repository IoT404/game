import pygame

WHITE         = (48, 48, 48)
displaywidth  = 470
displayheight = 840
displayobj    = None
clock         = None
imgback       = pygame.image.load('image/back.png')


def iotsetcaption(caption):
    pygame.display.set_caption(caption)

def iotbackdraw():
    global displayobj
    global imgback

    displayobj.blit(imgback, (0, 0))

def iotgo():
    global displayobj
    global clock

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            pygame.quit()
            break
        displayobj.fill(WHITE)
        iotbackdraw()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

def base():
    global displayobj
    global clock

    pygame.init()
    iotsetcaption("IoT Game")
    displayobj = pygame.display.set_mode((displaywidth, displayheight))
    clock = pygame.time.Clock()

    iotgo()

base()
import pygame

WHITE         = (48, 48, 48)
displaywidth  = 470
displayheight = 840
displayobj    = None


def iotsetcaption(caption):
    pygame.display.set_caption(caption)

def base():
    global displayobj

    pygame.init()
    iotsetcaption("IoT Game")
    displayobj = pygame.display.set_mode((displaywidth, displayheight))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            pygame.quit()
            break

base()
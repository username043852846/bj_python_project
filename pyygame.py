import pygame
pygame.init()
display_width = 800
displat_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 , 0)
car_width = 73

gameDisplay = pygame.display.set_mode((display_width, displat_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
carImg = pygame.image.load('자동차.png')
def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y))
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface,textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, Textrect = text_objects(text, largetext)
    TextRect.center = ((display_width / 2), (displat_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
def crash():
    message_display('you gg')
def game_loop():
    x = (display_width * 0.45)
    y = (display_width * 0.8)
    # x = 100
    # y = 0
    x_change = 0
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LEFT:
                     x_change = -5
                 if event.key == pygame.K_RIGHT:
                     x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(white)
        car(carImg, x, y)
        if x > display_width - car_width or x < 0:
            crash()
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
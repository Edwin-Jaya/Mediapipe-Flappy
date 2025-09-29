import pygame
from game import Game

pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()
game = Game()
image = pygame.image.load("./assets/bg.png")

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

    keys = pygame.key.get_pressed()

    if game.state == "menu" and keys[pygame.K_SPACE]:
        game.reset()


    elif game.state == "playing" and keys[pygame.K_SPACE]:
        game.bird.jump()


    elif game.state == "game_over":
        if keys[pygame.K_r]:
            game.reset()
        elif keys[pygame.K_m]:
            game.state = "menu"


    game.update()
    screen.blit(image,(0,0))
    # screen.fill(255,255,255))
    game.draw(screen)
    pygame.display.update()
    clock.tick(30)

pygame.quit()

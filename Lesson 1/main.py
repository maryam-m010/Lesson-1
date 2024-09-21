import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
title = pygame.display.set_caption("RECTANGLES")
screen.fill("pink")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.QUIT

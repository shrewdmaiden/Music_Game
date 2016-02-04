__author__ = 'gregory'

import pygame
import random

class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()
        white = (255,255,255)
        Notes_dict = {'c4': pygame.image.load('C4.png'),'d4': pygame.image.load('D4.png')}
        notes = list(Notes_dict.values())
        note = random.choice(notes)
        while 1:
            dt = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            screen.fill(white)
            screen.blit(note,(10,10))
            pygame.display.flip()



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 750))
    Game().main(screen)

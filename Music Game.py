__author__ = 'gregory'

import pygame
import random

class Game(object):
    Notes_dict = {'c': pygame.image.load('C4.png'),'d': pygame.image.load('D4.png'),'e': pygame.image.load('D4.png'),'f': [pygame.image.load('F4.png'),pygame.image.load('F3.png')],'g': [pygame.image.load('G3.png'),pygame.image.load('G4.png')],'a': pygame.image.load('A3.png'),'b': pygame.image.load('B3.png')}
    def update_note(self):
        notes = list(Game.Notes_dict.values())
        note = random.choice(notes)
        return note
    def main(self, screen):
        clock = pygame.time.Clock()
        white = (255,255,255)
        card = Game.update_note(self)

        while 1:
            dt = clock.tick(40)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

                if event.type == pygame.KEYDOWN:
                    card = Game.update_note(self)

            screen.fill(white)
            screen.blit(card,(10,10))
            pygame.display.flip()



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 750))
    Game().main(screen)

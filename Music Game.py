__author__ = 'gregory'

import pygame
import random

class Game(object):
    #Notes_dict = {'c': pygame.image.load('C4.png'),'d': pygame.image.load('D4.png'),'e': pygame.image.load('D4.png'),'f': [pygame.image.load('F4.png'),pygame.image.load('F3.png')],'g': [pygame.image.load('G3.png'),pygame.image.load('G4.png')],'a': pygame.image.load('A3.png'),'b': pygame.image.load('B3.png')}
    def update_note(self,dict):
        self.notes = list(dict.keys())
        self.note = random.choice(self.notes)
        return self.note
    def main(self, screen):
        clock = pygame.time.Clock()
        white = (255,255,255)
        notes_dict = {pygame.image.load('C4.png'):'c',pygame.image.load('D4.png'):'d',pygame.image.load('E4.png'):'e',pygame.image.load('F4.png'):'f',pygame.image.load('F3.png'):'f',pygame.image.load('G4.png'):'g',pygame.image.load('G3.png'):'g',pygame.image.load('A3.png'):'a',pygame.image.load('B3.png'):'b'}
        card = Game.update_note(self,notes_dict)
        answer = notes_dict[card]
        response = ""
        while 1:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c and answer == "c":
                        response = "correct"
                    elif event.key == pygame.K_d and answer == "d":
                        response = "correct"
                    elif event.key == pygame.K_e and answer == "e":
                        response = "correct"
                    elif event.key == pygame.K_f and answer == "f":
                        response = "correct"
                    elif event.key == pygame.K_g and answer == "g":
                        response = "correct"
                    elif event.key == pygame.K_a and answer == "a":
                        response = "correct"
                    elif event.key == pygame.K_b and answer == "b":
                        response = "correct"
                    else:
                        response = "wrong"
                    card = Game.update_note(self,notes_dict)
                    answer = notes_dict[card]

            font = pygame.font.Font('freesansbold.ttf',52)
            TextSurf = font.render(response,True,(0,0,0))
            screen.fill(white)
            screen.blit(card,(10,10))
            screen.blit(TextSurf,(500,600))

            pygame.display.flip()



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 750))
    Game().main(screen)

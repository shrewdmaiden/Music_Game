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
        notes_dict = {pygame.image.load('C4.png'):'c',
                      pygame.image.load('D4.png'):'d',
                      pygame.image.load('E4.png'):'e',
                      pygame.image.load('F4.png'):'f',
                      pygame.image.load('F3.png'):'f',
                      pygame.image.load('G4.png'):'g',
                      pygame.image.load('G3.png'):'g',
                      pygame.image.load('A3.png'):'a',
                      pygame.image.load('A4.png'):'a',
                      pygame.image.load('B4.png'):'b',
                      pygame.image.load('C5.png'):'c',
                      pygame.image.load('E3.png'):'e'}
        card = Game.update_note(self,notes_dict)
        answer = notes_dict[card]
        background = pygame.image.load('Book.png')
        response = ""
        running = 1
        correctcount = 0
        wrongcount = 0
        while running:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c and answer == "c":
                        response = "correct"
                        correctcount += 1
                    elif event.key == pygame.K_d and answer == "d":
                        response = "correct"
                        correctcount += 1
                    elif event.key == pygame.K_e and answer == "e":
                        response = "correct"
                        correctcount += 1
                    elif event.key == pygame.K_f and answer == "f":
                        response = "correct"
                        correctcount += 1
                    elif event.key == pygame.K_g and answer == "g":
                        response = "correct"
                        correctcount += 1
                    elif event.key == pygame.K_a and answer == "a":
                        response = "correct"
                        correctcount += 1
                    elif event.key == pygame.K_b and answer == "b":
                        response = "correct"
                        correctcount += 1
                    else:
                        response = "wrong"
                        wrongcount += 1
                    card = Game.update_note(self,notes_dict)
                    answer = notes_dict[card]
            if pygame.time.get_ticks()>=90000:
                running = 0

            clockfont = pygame.font.SysFont("vivaldi", 40)
            clocktext = clockfont.render("Time left: "+str((90000-pygame.time.get_ticks())//60000)+":"+str((90000-pygame.time.get_ticks())//1000%60).zfill(2), True, (0,0,0))
            correcttext = clockfont.render("Correct: "+str(correctcount), True, (0,0,0))
            wrongtext = clockfont.render("Wrong: "+str(wrongcount),True,(0,0,0))
            font = pygame.font.SysFont('vivaldi',52)
            TextSurf = font.render(response,True,(0,0,0))
            screen.blit(background,(0,0))
            screen.blit(card,(525,150))
            screen.blit(TextSurf,(650,540))
            screen.blit(clocktext,(200,150))
            screen.blit(correcttext,(200,200))
            screen.blit(wrongtext,(200,250))
            pygame.display.flip()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            finalcorrect = font.render("Correct: "+str(correctcount),True,(0,0,0))
            finalwrong = font.render("Wrong: "+str(wrongcount),True,(0,0,0))
            if correctcount == 0:
                accuracy = 0
            else:
                accuracy = round(correctcount/(correctcount+wrongcount)*100,2)
            finalaccuracy = font.render("Accuracy: "+str(accuracy)+"%",True,(0,0,0))
            screen.blit(background,(0,0))
            screen.blit(finalcorrect,(200,200))
            screen.blit(finalwrong,(190,300))
            screen.blit(finalaccuracy,(160,400))
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 750))
    Game().main(screen)

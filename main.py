import pygame as py
from square import Squares
import random as r

if __name__ == "__main__":
    py.display.init()
    window = py.display.set_mode((700,700))
    py.display.set_caption("Game of Life")
    
    game_test = True
    while(game_test):
        # making the square_list
        square_list = list(); x = 0; y = 0;
        for i in range(70*70):
            randnum = r.randint(0,5)
            if(x > 690): x = 0; y += 10
            if(randnum == 1):
                square_list.append(Squares(x, y, False, i))
            else: square_list.append(Squares(x, y, True, i))
            x += 10
        
        # square_list[2061].set_dead(False) # i = 2061 
        # # square_list[2061+1].set_dead(False)
        # # square_list[2061-1].set_dead(False)
        # square_list[2061-70].set_dead(False)
        # square_list[2061+70].set_dead(False)
        # square_list[2061+70+1].set_dead(False)
        # square_list[2061-70-1].set_dead(False)
        # square_list[2061+70-1].set_dead(False)
        # square_list[2061-70+1].set_dead(False)
        
        running_test = True

        while(running_test):
            pressed_keys = py.key.get_pressed()
            py.time.wait(1000)
            for event in py.event.get():
                if event.type == py.QUIT:
                    game_test = False
                    running_test = False
                    break;
                
                if event.type == py.MOUSEBUTTONDOWN:
                    running_test = False
                    break

                
                # if event.type == py.MOUSEBUTTONDOWN:
                #     for square in square_list:
                #         square.check_dead(square_list)
                #         square.draw(window)
            for square in square_list:
                square.check_dead(square_list)
                square.draw(window)
            alive_counter = 0
            for square in square_list:
                if(square.get_dead() is False): alive_counter += 1
            
            if(alive_counter == 0):
                running_test = False;
                break
            

            py.display.update()
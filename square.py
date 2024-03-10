import pygame as py
class Squares:
    __slots__ = ("x", "y", "isdead", "index")
    def __init__(self, _x, _y, _isdead, _index):
        self.x = _x; self.y = _y; self.isdead = _isdead
        self.index = _index
    
    def set_pos(self, _x:int, _y:int)->None: self.x = _x; self.y = _y

    def get_pos(self)->tuple: return(self.x, self.y)

    def set_dead(self, _isdead)->None: self.isdead = _isdead

    def get_dead(self)->bool: return self.isdead

    def check_dead(self, square_list: list):
        counter = 0; i = self.index

        if(i > 1 and i < (len(square_list)-1)):
            if(square_list[i].get_dead() is False):
                counter += 1
            if(square_list[i-1].get_dead() is False): # if square to left is alive
                counter += 1

            if(square_list[i+1].get_dead() is False): # if square to right is alive
                counter += 1
            
            if(i > 72):
                if(square_list[i-70].get_dead() is False): # if square above is alive
                    counter += 1
                
                if(square_list[i - 70 - 1].get_dead() is False): # if square to top left is alive
                    counter += 1
                
                if(square_list[i - 70 + 1].get_dead() is False): # if square to top right is alive
                    counter += 1
            
            if(i < len(square_list) - 71):
                if(square_list[i + 70].get_dead() is False): # if square below is alive
                    counter += 1
                
                if(square_list[i + 70 - 1].get_dead() is False): # if square to bottom left is alive
                    counter += 1
                
                if(square_list[i + 70 + 1].get_dead() is False): # if square to bottom right is alive
                    counter += 1
        
        if(counter < 2): self.isdead = True; 
        elif(counter == 3): self.isdead = False;
        else: self.isdead = True;
                


    def draw(self, window)->None:
        if(self.isdead is True): py.draw.rect(window, (0,0,0), py.Rect(self.x,self.y,10,10))
        else: py.draw.rect(window, (255,255,255), py.Rect(self.x,self.y,10,10))

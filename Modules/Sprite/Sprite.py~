

import pygame
import Modules.Sprite.SpriteLoader

class Sprite():
        def __init__ (self, images, angle):
            '''
            images is a list of sequential images
            angle - how to rotate the images
            '''
            pics = images
            self.angle = angle
                
            self.sprites = pics
            self.set_current_sprite(0)
            
        def set_current_sprite(self, i):
            if ( i>len(self.sprites) ):
                print ( "!!! Modules.Sprite.Sprite set_current_sprite too large index for sprite" )
            self.current_sprite = i
            
        def current(self):
            return pygame.transform.rotate(self.sprites[self.current_sprite], self.angle)
            
        def next(self):
                '''
                Returns true if the sprite was the last 
                '''
                if ( self.current_sprite+1<len(self.sprites) ):
                        self.current_sprite+=1
                        return False
                else:
                        self.current_sprite = 0
                        return True
                        
        def from_loader(name, surname, scale, rotation):    
                return Sprite( Modules.Sprite.SpriteLoader.singleton.load ( name, surname, scale ), rotation)
                

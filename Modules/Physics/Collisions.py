'''
Checks for collisions in the world.
it collides objects only in it's register
with objects in Modules.World.world
'''
from __future__ import absolute_import

import pygame
from Modules.Register import Register
from Modules.Vector25D import Vector25D
class Collisions(Register):
        def __init__(self, world):
                Register.__init__(self)
                print ("iii Modules.Physics.Modules.Collisions loaded")
                self.world = world
                
        def tick(self):
                for obj1 in self.items():
                        r1 = obj1.rect
                        for obj2 in self.world.objects:
                                r2 = obj2.rect
                                if obj1 != obj2:          
                                        if pygame.sprite.collide_rect(obj1, obj2): 
                                                if pygame.sprite.collide_mask(obj1, obj2):
                                                        obj1.collision(obj2)
                                                        
                                        

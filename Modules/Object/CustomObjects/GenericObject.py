import pygame
from Modules.Vector25D import Vector25D
import Modules.World

import math
import random

class GenericObject():
        '''
        GENERIC CLASS, ALL OBJECT BEHAVIOUR TO BE DERIVED FROM THAT
        
        this is a root object, which keeps the track of it's childen.
        this may be equal to a SpriteGroup class in pyGame
        '''
        def __init__(self, parts):
                '''
                object creation procedure
                
                Arguments:
                - parts: the parts of an object of type GenericObjectPart
                '''
                
                self.parts = parts
                
                self.init_HP()
                self.init_bounding_box()
                self.init_redrawables()
                
                self.init_vectors()
                
                self.init_center_of_mass()
                self.init_surface()
                
                self.init_parent()
                
                self.init()
                
                #self.mask = pygame.mask.Mask((1,1))
                
                '''
                How is it better to load the objects???
                '''
        def init(self):
                pass
        '''
        Initialization procedures
        '''
        
        def init_HP(self):
                self.HP = 0
                for name, part in self.parts.items():
                        self.HP+=part.HP
        
        def init_parent(self):
                for name, part in self.parts.items():
                        part.parent = self
                        part.init_after_parent()
                
        def init_vectors(self):
                self.A = Vector25D()
                self.V = Vector25D()
                self.P = Vector25D()
                
        def init_surface(self):
                xcorr = self.center_of_mass_correction[0] #self.initial_rect.x+self.center_of_mass_correction[0]
                ycorr = self.center_of_mass_correction[1] #self.initial_rect.y+self.center_of_mass_correction[1]
                
                #write in a more appropriate way
                if xcorr < 0:
                        xcorr = -xcorr
                if ycorr < 0:
                        ycorr = -ycorr
                        
                self.center_of_mass_correction -= Vector25D(xcorr, ycorr)
                        
                '''
                multiplication x2 is definitely a good thing
                '''        
                        
                self.surface_static = pygame.Surface ( (self.initial_rect.w+xcorr*2,
                                                        self.initial_rect.h+ycorr*2), flags=pygame.HWSURFACE ).convert_alpha()
                self.surface_buffer = pygame.Surface ( (self.initial_rect.w+xcorr*2,
                                                        self.initial_rect.h+ycorr*2), flags=pygame.HWSURFACE ).convert_alpha()
                self.mask = pygame.mask.from_surface ( self.surface_static )                                        
                self.rect = self.initial_rect
                
               
                        
        def init_redrawables(self):
                self.redrawables = []
                for name, part in self.parts.items():
                        if part.redraw == True:
                                self.redrawables += [part]
        
        def init_bounding_box(self):
                '''
                recalculates the bounding box of an Object
                
                return: Rect meaning the boundary of the surface
                '''
                x,y,w,h=0,0,0,0
                for key,part in self.parts.items():
                        if part.rect.x < x:
                                x = part.rect.x
                        if part.rect.y < y:
                                y = part.rect.y
                        if part.rect.w*math.sin(part.pos[2]/180*math.pi)+part.rect.x-x > w:
                                w = part.rect.w+part.rect.x+x
                        if part.rect.h*math.cos(-part.pos[2]/180*math.pi)+part.rect.y-y > h:
                                h = part.rect.h+part.rect.y+y
                w-=x
                h-=y
                x=0
                y=0
                self.initial_rect = pygame.Rect(x,y,w,h)
                
        def draw(self, to):
                rect = self.surface_static.get_rect()
                       
                self.surface_buffer.fill ( (0,0,0, 0) )
                # Blitting to the buffering surface
                self.surface_buffer.blit(self.surface_static, (0,0) )
                
                for dynamic_part in self.redrawables:
                        dynamic_part.dynamic_redraw()
                        
                # rotation of a whole object
                blit_surf = pygame.transform.rotate(self.surface_buffer, self.P[2]).convert_alpha()
                
                self.rect = self.current_rect = blit_surf.get_rect()
                self.rect.x = self.P[0]-self.current_rect.w/2
                self.rect.y = self.P[1]-self.current_rect.h/2
                
                self.mask = pygame.mask.from_surface ( blit_surf )
                
                
                # Current position ALWAYS points to the center of an object
                to.blit(blit_surf, (self.P[0]-self.current_rect.w/2, self.P[1]-self.current_rect.h/2) )  
                
        def part_remove(self, child):
                '''
                removes part from this object
                '''
                
                for name, obj in self.parts:
                        if child == obj:
                                del self.parts[name]
                                break
                                
                self.init_center_of_mass()
                
        def part_remove_by_name(self, name):
                del self.parts[name]
                
                # Redraw everything in our object
                self.init_center_of_mass()
                self.init_surface()
                self.static_blit()
                
        # Update self variables
        def update(self):   
                '''self.width = self.rect.x+self.rect.w
                self.height = self.rect.y+self.rect.h'''
        
        def get_center(self):
                return Vector25D(self.current_rect.w/2, self.current_rect.h/2)
                
        def init_center_of_mass(self):
                cm = Vector25D()
                
                full_mass = 0
                for name, part in self.parts.items():
                        cm = (cm + Vector25D((part.rect.w/2+part.rect.x), (part.rect.h/2+part.rect.y))*part.mass)
                        full_mass += part.mass
                self.center_of_mass = cm/full_mass
                self.mass = full_mass
                
                # For the graphical part
                self.center_of_mass_correction = self.center_of_mass - Vector25D((self.initial_rect.w+self.initial_rect.x)/2, (self.initial_rect.h+self.initial_rect.y)/2)
                
                # The I tensor for the Torque computation
                self.I = self.mass*(self.initial_rect.w**2+self.initial_rect.h**2)/12
                
                
        def blit_static(self):
                self.surface_static.fill ( (0,0,0, 0) )
                for name, part in self.parts.items():
                        part.static_redraw()
                
        def get_controls(self):
                return self.controls
 

        def collision(self, obj):
                # Generic objects do not collide, can count as lucky dodge
                pass
        
        def destroy(self):
                Modules.World.world.remove(self)
                '''names=[]
                for name, part in self.parts.items():
                    names+=[name]
                for name in names:
                        del self.parts[name]'''
        
        def show_damage(self, n):
                degree = random.random()*360
                V = Vector25D(1, 1)
                V = V.rotate(degree)
                V = V*100
                Modules.World.world.add_text ( str(int(-n)), self,0.9862327044933592, 0.5, V )
                
        def damage(self, n):
                self.HP-=n
                self.show_damage(n)
                if self.hp_lost():
                        self.destroy()
                        
        def hp_lost(self):
                '''
                Messaging for derivatives
                '''
                if self.HP<=0:
                        return True
                return False
                
class GenericObjectPart(pygame.sprite.Sprite) :
        '''
        GENERIC CLASS, ALL OBJECT PART BEHAVIOUR TO BE DERIVED FROM THIS
        '''
        def __init__(self, name, HP, mass, pos, redraw, images, custominfo):
                '''
                object creation procedure
                
                Arguments:
                - HP: hit points amount
                - mass: mass of the object
                - images: {'name':pygame.sprite.Image}
                - controls: {'name':coeff}
                - custominfo: {'name':custom}
                '''
                self.init_name (name)
                
                
                self.init_HP_mass ( HP, mass )
                self.init_pos ( pos )
                self.init_redraw ( redraw )
                self.init_images ( images )
                
                # Set the rectangle ourselves
                self.init_rect ( )
                
                self.init()
                self.init_custom_info (custominfo)
                
                '''
                Initialize this variable in a better way
                '''
                
                pygame.sprite.Sprite.__init__(self)
        
        
        '''
        Initialization, called by default constructor. Better to overload these!!
        '''
        
        def init ( self ):
                pass
               
        def init_name( self, name ):
                self.name = name
        
        def init_HP_mass ( self, HP, mass ):
                self.HP = HP
                self.mass = mass
                
        def init_pos (self, pos):
                self.pos = pos
                
        def init_redraw(self, redraw):
                self.redraw = redraw    
                
        def init_images(self, images):
                '''
                Every image has to be of the same size here!!!
                '''
                self.images = images  
                
                for name, image in self.images.items():
                        self.rect = self.images[name].get_rect()
                        self.images[name] = pygame.transform.rotate(image, self.pos[2])  
                        
        def init_after_parent(self):
                pass
                
        def init_rect (self):
                if len(self.images)>1:
                        print ( "www Modules.Object.CustomObjects.GenericObject.GenericObjectPart.init_rect Image count > 1" )
                        
                rect = None
                for name, image in self.images.items():
                        rect = self.images[name].get_rect()
                        break        
                x = self.pos.v[0]
                y = self.pos.v[1]
                x+=(self.rect.w-rect.w)/2
                y+=(self.rect.h-rect.h)/2
                
                self.pos = Vector25D(x,y,self.pos[2])
                
                self.rect = pygame.Rect( x, y, rect.w, rect.h )

        def init_custom_info (self, custominfo):
                if len(custominfo) > 0:
                        print ( "www Modules.Object.CustomObjects.GenericObject.GenericObjectPart.__init__ custom info for generic object" )
                        
                        
        '''
        Initialization END
        '''
        
        def get_event_function(self):
                print ( "www Modules.Object.CustomObjects.GenericObject.GenericObjectPart.get_event_function called for generic object" )

        '''
        Helpers
        '''    
        
        def blit_static(self, image):
                self.parent.surface_static.blit( image, (self.pos[0]-self.parent.center_of_mass_correction[0], 
                                                         self.pos[1]-self.parent.center_of_mass_correction[1]) )  
                         

        def blit_dynamic(self, image):
                self.parent.surface_buffer.blit( image, (self.pos[0]-self.parent.center_of_mass_correction[0], 
                                                         self.pos[1]-self.parent.center_of_mass_correction[1]) )  
        def static_redraw(self):
                for name, img in self.images.items():
                        self.blit_static(img)
                        break

                

        def collision(self, part):
                print ( "collision of generic object")
                pass


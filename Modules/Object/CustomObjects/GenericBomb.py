'''
02.12.2010 Andrej Cizov

Engine class
'''
from Modules.Object.CustomObjects.GenericObject import GenericObject
import Modules.World
from Modules.Config import get
from Modules.World import World
from Modules.Vector25D import Vector25D

DIST_MULTIPLIER=float(get("Bomb Distance Multiplier"))**2

class GenericBomb(GenericObject):
        '''
        Bomb definitions
        '''
        def init(self):
                self.set_radius(100)
                self.set_power(100000000)
                self.set_counter(300)
                
        def set_counter(self, counter):
                self.counter = 300
                
        def set_power(self, p):
                self.power = p
                
        def set_radius(self, r):
                self.explode_in = r**2 
                
        def show_damage(self, n):
                pass
             
        def draw(self, to):
                '''
                Since the draw function is called every tick, we are able to use this for our purposes
                - the actual working example of AI in this game
                '''
                self.counter -= 1
                if self.counter == 0:
                        Modules.World.world.add_text ( "Initiated!!!", self, 0.989327770604733, 1.5 )
                if self.counter < 0:
                        self.change_working_engines()
                GenericObject.draw(self,to)
                if self.counter > 0:
                        World.draw_font(to, Modules.World.world.font_info, str(self.counter), (234, 0, 0), self.P )
                
        def explode(self):
                self.damage(self.HP)
               
        def hp_lost(self):
                if self.HP<=self.HP*0.2:
                        Modules.World.world.remove(self)
                        Modules.World.world.bomb_explosion(self.P)
                        Modules.World.world.physics.blast(self.P, self.explode_in, self.power)
                        return False
                return False  
               
        def change_working_engines(self):
                nearest = Vector25D(2000,2000)
                nearestObj = None
                
                for obj in Modules.World.world.objects:
                        if obj != self:
                                diff = obj.P - self.P
                                if diff.length2() < self.explode_in*DIST_MULTIPLIER:
                                        self.explode()
                                        return
                                        
                                if nearest.length2() > diff.length2():
                                        nearest = diff
                                        nearestObj = obj
                if nearestObj == None:
                        return
                        
                Vmove = nearest.rotate(self.P[2])
                        
                self.parts['EngineLeft'].accelerate_stop()
                self.parts['EngineRight'].accelerate_stop()
                self.parts['EngineTop'].accelerate_stop()
                self.parts['EngineBottom'].accelerate_stop()
                        
                if Vmove[0] > 0:
                        self.parts['EngineLeft'].accelerate_start(0.00001)
                else:
                        self.parts['EngineRight'].accelerate_start(0.00001)
                if Vmove[1] > 0:
                        self.parts['EngineTop'].accelerate_start(0.00001)
                else:
                        self.parts['EngineBottom'].accelerate_start(0.00001)
                

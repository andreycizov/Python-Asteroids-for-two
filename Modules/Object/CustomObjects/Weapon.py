import Modules.World
import pygame
from Modules.Vector25D import Vector25D

from Modules.Object.CustomObjects.GenericObject import GenericObjectPart
import math

class Weapon(GenericObjectPart):
        def init(self): 
                self.working = False
        
        def init_custom_info(self, custom):
                self.bullet_velocity = float(custom['Bullet Velocity'])
                self.bullet_mass = float(custom['Bullet Mass'])
                self.bullet_radius = float(custom['Bullet Radius'])
                self.bpf = float(custom['Bullets Per Frame'])
                self.color = (255,0,0)
                
        def init_after_parent(self):
                self.V = Vector25D(math.sin(self.pos[2]/180*math.pi), math.cos(-self.pos[2]/180*math.pi))*self.bullet_velocity
                
        def shoot_start(self, c):
                self.working = True
                V = self.V.rotate(-self.parent.P[2])+self.parent.V
                Modules.World.world.physics.apply_force( self.parent, V*self.bullet_mass*-1, Vector25D())
                Modules.World.world.add_bullet( self.parent.P+V.norm()*25, V, int(self.bullet_radius), self.color, self.bullet_mass )
        
        def shoot_stop(self):
                self.Working = False
                
        def get_controls(self):
                return [Weapon.shoot_start, Weapon.shoot_stop]
                
        def static_redraw(self):
                        self.blit_static(self.images['Stall'])
                        
        def dynamic_redraw(self):
                if self.working == True:
                        self.blit_dynamic(self.images['Running'])

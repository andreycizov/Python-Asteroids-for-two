from Modules.Object.CustomObjects.GenericObject import GenericObject
from Modules.Vector25D import Vector25D

from Modules.Config import get
import random
import Modules.Object.Loader
import Modules.World
import math

MAX_SMALL=int(get("Asteroids Children Max"))
VELOCITY_FACTOR=float(get("Asteroids Velocity Factor"))
COLLISION_DAMAGE=float(get("Asteroids Collision Damage Factor"))


class Asteroid(GenericObject):
        def init(self):
                self.large = self.parts['root'].large

        def create_small(self):
                if self.large:  
                        # asteroid calculation is quadratic. we have more chances to get a larger ammount of children, than small
                        n = random.random()
                        n = n**2
                        n = int(math.ceil((1-n)*MAX_SMALL))
                        
                        for i in range(0, n):
                                asteroid = Modules.Object.Loader.load("SmallAsteroid", Asteroid)
                                asteroid.P.v[0] = self.P[0] - self.rect.w/2 + random.random()*self.rect.w
                                asteroid.P.v[1] = self.P[1] - self.rect.h/2 + random.random()*self.rect.h
                                asteroid.P.v[2] = random.random()*360
                                asteroid.V = self.V+((asteroid.P-self.V).norm()*VELOCITY_FACTOR*random.random())
                                Modules.World.world.add(asteroid)
                                Modules.World.world.fast_add(asteroid, Modules.World.world.physics_bullet_modules)
                                
        def show_damage(self, n):
                pass
                
        def collision(self, obj):
                masses = self.mass*obj.mass
                F = (self.V - obj.V)/self.mass/obj.mass
                P1 = obj.P
                P2 = self.P
                P1.v[2] = 0
                P2.v[2] = 0
                F +=  (P1*self.mass - P2*obj.mass)/(self.mass+obj.mass)**2.7
                
                wh = self.rect.w + self.rect.h
                wh2 = obj.rect.w + obj.rect.h

                Pcoll = (self.P*wh2+obj.P*wh)/(2+wh+wh2)
                
                Va = self.V
                Va.v[2] = 0
                Vb = obj.V
                Vb.v[2] = 0
                
                Rap = Pcoll - self.P
                Rap.v[2] = 0
                Rbp = Pcoll - obj.P
                Rbp.v[2] = 0
                
                N = (Va-Vb).norm()
                N.v[2] = 0
                
                e = 0
                
                wa = self.V[2]/360*math.pi
                wb = obj.V[2]/360*math.pi
                
                Vab = Va + Rap.cross(wa) - Vb - Rbp.cross(wb)
                
                ma = self.mass
                mb = obj.mass
                
                Ia = self.I
                Ib = obj.I
                
                j = ( Vab*N*-(1+e) )/ ( 1/ma+1/mb + Rap.cross(N)*Rap.cross(N)/Ia + Rbp.cross(N)*Rbp.cross(N)/Ib )
                print (Rap.cross(N), Rap.cross(N)*Rap.cross(N))
                
                Va.v[2] = 0
                Vb.v[2] = 0
                
                Va = Va + N*j/ma
                Vb = Vb - N*j/mb
                
                Va.v[2] = (wa + (((Rap).cross(N*j)[2])/Ia))/math.pi*360
                Vb.v[2] = (wb - (((Rbp).cross(N*j))[2]/Ib))/math.pi*360
                
                self.V = Va
                obj.V = Vb
                obj.A += (obj.P-self.P)*(1/(obj.P-self.P).length())*50
                
                Da = (Va-self.V).length()
                Db = (Vb-obj.V).length()
                
                Modules.World.world.physics.apply_force(obj, F*masses*obj.mass, (self.P-obj.P).norm())
                '''
                Add force application!!
                '''
                
                if not isinstance(obj, Asteroid):
                        Modules.World.world.ship_explosion((self.P*wh2+obj.P*wh)/(2+wh+wh2))
                        if isinstance(obj, GenericObject):
                                self.destroy()
                        mult = 1
                        if not self.large:
                                mult=0.2
                        obj.damage( COLLISION_DAMAGE*mult )
                        self.damage( COLLISION_DAMAGE*mult )
                
        def destroy(self):
                Modules.World.world.ship_explosion(self.P)
                Modules.World.world.remove(self)
                Modules.World.world.fast_remove(self, Modules.World.world.physics_bullet_modules)
      
        def hp_lost(self):
                if self.HP<=0:
                        if self.large:
                                self.create_small()
                        return True
                return False

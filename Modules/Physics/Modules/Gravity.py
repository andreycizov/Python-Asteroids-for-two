'''
03.12.2010
Gravity module
'''
from Modules.Register import Register
import Modules.World

G = 6.6726e-9

class Gravity(Register):
        def __init__(self,world):
                Register.__init__(self)
                print ("iii Modules.Physics.Modules.Gravity loaded")
                
        def tick(self):
                for obj in self.items():
                        a = G*obj.mass
                        for name, obj2 in Modules.World.world.objects.items():
                                if obj2 != obj:
                                        obj2.A += (obj.P-obj2.P)*a*obj2.mass/(obj.P-obj2.P).length()/obj2.mass

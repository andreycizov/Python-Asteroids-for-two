from Modules.Register import Register
import math
class Acceleration(Register):
        def __init__(self,world):
                Register.__init__(self)
                print ("iii Modules.Physics.Modules.Acceleration loaded")
                
        def tick(self):
                for obj in self.items():
                        obj.V += obj.A/self.parent.pps
                        if obj.V.length2()+obj.V[2]**2 > 1000000:
                                obj.V = obj.V/math.sqrt(obj.V.length2()+obj.V[2]**2)*1000
                

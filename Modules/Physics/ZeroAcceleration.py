from Modules.Register import Register
from Modules.Vector25D import Vector25D
class ZeroAcceleration(Register):
        def __init__(self,world):
                Register.__init__(self)
                print ("iii Modules.Physics.Modules.ZeroAcceleration loaded")
                
        def tick(self):
                for obj in self.items():
                        obj.A = Vector25D()
                

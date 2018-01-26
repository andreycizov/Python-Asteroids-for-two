from __future__ import absolute_import
from Modules.Register import Register
class Moving(Register):
        def __init__(self,world):
                Register.__init__(self)
                print ("iii Modules.Physics.Modules.Moving loaded")
                
        def tick(self):
                for obj in self.items():
                        obj.P += obj.V/self.parent.pps # + (obj.center_of_mass-obj.get_center())/self.parent.pps

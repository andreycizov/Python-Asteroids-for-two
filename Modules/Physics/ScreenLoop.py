from __future__ import absolute_import
from Modules.Register import Register
from Modules.Vector25D import Vector25D
from Modules.Config import get
class ScreenLoop(Register):
        def __init__(self,world):
                Register.__init__(self)
                self.max = Vector25D ( float(get("Window Width")), float(get("Window Height")) )
                print ("iii Modules.Physics.Modules.ScreenLoop loaded")
                
        def tick(self):
                for obj in self.items():
                        if obj.P[0] > obj.rect.w/2+self.max[0]:
                                obj.P.v[0] = -obj.rect.w/2
                        if obj.P[1] > obj.rect.h/2+self.max[1]:
                                obj.P.v[1] = -obj.rect.h/2
                        if obj.P[0] < -obj.rect.w/2:
                                obj.P.v[0] = self.max[0]+obj.rect.w/2
                        if obj.P[1] < -obj.rect.h/2:
                                obj.P.v[1] = self.max[1] +obj.rect.h/2  
                             
                

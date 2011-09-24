'''
02.12.2010 Andrej Cizov

Vector 2.5D - x,y,w coordinate vector as x,y - point on the screen, w - rotation
'''

import math

class Vector25D:
        def __init__(self, x=0,y=0,w=0):
                '''
                initializes a vector with default positions at 0
                '''
                self.v = [x, y, w]
                
        def __add__(self, v):
                return Vector25D( self.v[0]+v.v[0], self.v[1]+v.v[1], self.v[2]+v.v[2] )
                
        def __sub__(self, v):
                return Vector25D( self.v[0]-v.v[0], self.v[1]-v.v[1], self.v[2]-v.v[2] )
                
        def __mul__(self, v):
                if isinstance(v, int) or isinstance(v, float):
                        return Vector25D( self.v[0]*v, self.v[1]*v, self.v[2]*v )
                else:
                        return float( self.v[0]*v.v[0]+self.v[1]*v.v[1]+self.v[2]*v.v[2] )
                        
        def __truediv__(self, i):
                i = 1/i
                return self*i
                
        def __getitem__(self, a):
                return self.v[a]
                
        def rotate(self, degree):
                rads = degree/180*math.pi
                sin = math.sin(rads)
                cos = math.cos(rads)
                return Vector25D( self.v[0]*cos - self.v[1]*sin,
                                  self.v[0]*sin + self.v[1]*cos )
                                  
        def cross(self, v):
                '''
                The cross product in 25D for two vectors.
                '''
                if isinstance(v, int) or isinstance(v, float):
                        return Vector25D(-v*self.v[1], v*self.v[0] ) 
                else:
                        x,y,z = self.v
                        u,v,w = v.v
                        
                        return Vector25D( y*w - z*v, -x*w + z*u, x*v-y*u)
                        # 
                        #return float( self.v[0]*v.v[1]-self.v[1]*v.v[0] )

        def __str__(self):
                return str(self.v)
                
        def __unicode__(self):
                return str(self.v)

        def norm(self):
                l = self.length()
                if l > 0:
                        return self/self.length()
                else:
                        return Vector25D()
                
        def length(self):
                return float(math.sqrt(self.v[0]*self.v[0]+self.v[1]*self.v[1]))
                
        def length2(self):
                return float(self.v[0]*self.v[0]+self.v[1]*self.v[1])
                
def rotate_around_point(point, v):
        '''
        rotate given vector around given point
        
        returns new vector position
        '''
        
        v = v-point
        
        

'''
02.12.2010 Andrej Cizov

Engine class
'''
from Modules.Object.CustomObjects.GenericObject import GenericObjectPart
class User_Ship(GenericObjectPart):
        '''
        
        '''
        def static_redraw(self):
                for name, img in self.images.items():
                        self.blit_static(img)
                        break
               
                
                

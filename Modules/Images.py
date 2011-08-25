'''
02.12.2010 Andrej Cizov

Image manipulation functions
'''

class Image():
        def __init__(self, image, parent):
                self.image = image
                self.parent = parent
                self.initialrect = image.get_rect()
                self.rect = self.initialrect
                
        def rotate(self, degree):
                
        

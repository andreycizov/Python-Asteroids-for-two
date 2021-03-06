import Modules.World
class StaticInterface():
        def __init__(self, parent, sprite):
                self.parent = parent
                self.sprite = sprite
                
        def draw(self, to):
                if not self.parent in Modules.World.world.objects:
                        Modules.World.world.remove_interface(self)
                        return
                self.P = self.parent.P
                r = self.sprite.current().get_rect()
                to.blit(self.sprite.current(), (self.P[0]-r.w/2, self.P[1]-r.h/2))
                self.sprite.next()

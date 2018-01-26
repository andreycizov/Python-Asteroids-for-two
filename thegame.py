'''
The Game by Andrej Cizov sc10a3c
Tanks-in-the-space-like-game
'''
from __future__ import absolute_import

from Modules.Vector25D import Vector25D



import Modules.World

import Modules.Object.Loader
from Modules.Object.CustomObjects.GenericObject import GenericObject
import cProfile
from Modules.Interface.StaticInterface import StaticInterface
from Modules.Sprite.Sprite import Sprite
import random
import math
from Modules.Config import get


def dead(a):
        return a.HP<=0

def set_kbd_bindings(objs):
        a,b=objs
        world = Modules.World.world
        world.input.add_key_to_reaction( 273, [{'part_obj': a.parts['Name0'], 'coefficient': 3 }, 
                                               {'part_obj': a.parts['Name1'], 'coefficient': 3 }  ] )                
        world.input.add_key_to_reaction( 275, [{'part_obj': a.parts['Name1'], 'coefficient': 2 }] )
        world.input.add_key_to_reaction( 276, [{'part_obj': a.parts['Name0'], 'coefficient': 2 }] )
        world.input.add_key_to_reaction( 274, [{'part_obj': a.parts['Name2'], 'coefficient': 2 }] )
        world.input.add_key_to_reaction( 47, [{'part_obj': a.parts['Weapon'], 'coefficient': 2 }] )
        world.input.add_key_to_reaction( 46, [{'part_obj': a.parts['Bomber'], 'coefficient': 2 }] )


        world.input.add_key_to_reaction( 119, [{'part_obj': b.parts['Name0'], 'coefficient': 3 }, 
                                               {'part_obj': b.parts['Name1'], 'coefficient': 3 }  ] )     
        world.input.add_key_to_reaction( 100, [{'part_obj': b.parts['Name1'], 'coefficient': 2 }] )
        world.input.add_key_to_reaction( 97, [{'part_obj': b.parts['Name0'], 'coefficient': 2 }] )
        world.input.add_key_to_reaction( 115, [{'part_obj': b.parts['Name2'], 'coefficient': 2 }] )
        world.input.add_key_to_reaction( 32, [{'part_obj': b.parts['Weapon'], 'coefficient': 2 }] )
        world.input.add_key_to_reaction( 113, [{'part_obj': b.parts['Bomber'], 'coefficient': 2 }] )
        
def rem_kbd_bindings(objs):
        world = Modules.World.world
        print ("Removing keyboard bindings!!!")
        world.input.remove_by_parent(objs)
        
def add_objects():
        world = Modules.World.world
        a = Modules.Object.Loader.load("GenericUserShip2", GenericObject)
        b = Modules.Object.Loader.load("GenericUserShip2", GenericObject)

        #a.P = Vector25D(400,150,-30)
        a.P = Vector25D(500,150,0)
        a.V = Vector25D(0, 0)
        #b.P = Vector25D(500,400,120)
        b.P = Vector25D(500,400,22)
        b.A = Vector25D(0, 0, 0)
        
        world.add(a)
        world.add(b)
        '''for i in range(0,30):
                g = Modules.Object.Loader.load("GenericUserShip2", GenericObject)
                g.P = Vector25D(780+i*10,150,0)
                g.V = Vector25D(20, 0)
                world.add(g)'''
        
        c = StaticInterface(a, Sprite.from_loader("RedPlayerCircle", "First", 0.2, 0 ) )
        d = StaticInterface(b, Sprite.from_loader("BluePlayerCircle", "First", 0.2, 0 ) )
        world.add_interface(c)
        world.add_interface(d)
        world.add
        
        return [a,b]

DECORATION = True

def set_decoration():
        world = Modules.World.world
        
        if DECORATION:
            world.add_decoration(Vector25D(900, 300), Vector25D(-1, 0), "./planets/planet_glow.png")
            world.add_decoration(Vector25D(100, 150), Vector25D(-3, 0.0005), "./planets/Saturn_(planet)_large.png")
            world.add_decoration(Vector25D(600, 700), Vector25D(3, 0.06), "./planets/planet_venus_3d_screensaver-4114-scr.png")

def reinit(a,b):
        world = Modules.World.world
        world.flush()
        set_decoration()
        if a != None and b != None:
                rem_kbd_bindings([a,b])
                del a
                del b
        a,b = add_objects()
        set_kbd_bindings([a,b])
        return [a,b]


def main():
        world = Modules.World.world
        a = None
        b = None
        a,b = reinit(a,b)
          
        while (world.loop(int(world.fps*0.5))):
                text = "Player {0} won!"
                if dead(a) and not dead(b):
                        world.add_text(text.format("Blue"), b, 1, 3)
                        world.input.remove_by_parent([a])
                        world.loop(world.fps*3)
                        world.remove(b)
                        a,b=reinit(a,b)
                elif dead(b) and not dead(a):
                        world.add_text(text.format("Red"), a, 1, 3)
                        world.input.remove_by_parent([b])
                        world.loop(world.fps*3)
                        world.remove(a)
                        a,b=reinit(a,b)
                elif dead(a) and dead(b):
                        a.P = Vector25D(world.dimensions[0]/2, world.dimensions[1]/2)
                        world.input.remove_by_parent([a,b])
                        world.add_text("Nobody has won", a, 1, 3)
                        world.loop(world.fps*3)
                        a,b=reinit(a,b)
PROFILE = False

if not PROFILE:                
    main()      
else:
    cProfile.run('main()', 'fooprof')



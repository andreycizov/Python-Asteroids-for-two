'''
02.12.2010 Andrej Cizov

MOdule that loads the objects from the configuration directory
'''
from Modules.Config import get
from Modules.Config.LoaderConfigReader import read_loader_config
from Modules.Object.CustomObjects.GenericObject import GenericObject, GenericObjectPart
import sys
from Modules.Vector25D import Vector25D
import pygame.image



def load(objname, t):
        '''
        loads an object of Modules.Object.GenericObject type
        
        The object loaded actually depends on the settings in the config file for object
        '''
        #read the root object:
        print ( "iii Loading object named '{0}'".format(objname) )
        root = load_part(objname)
        
        root_object = load_object_class(root[0]['class'])
        
        parts = {'root':root_object(
                             root[0]['name'],
                             root[0]['HP'], 
                             root[0]['mass'],
                             root[0]['pos'],
                             root[0]['redraw'],
                             load_images ( root[0]['images'] ),
                             list_to_dict(root[3])
                             )}
        for child in root[1]:#
                child_part = load_part ( child['type'] )
                child_object = load_object_class(child_part[0]['class'])
                parts[child['name']] = child_object(child['name'],
                             child_part[0]['HP'], 
                             child_part[0]['mass'],
                             child['pos'],
                             child_part[0]['redraw'],
                             load_images ( child_part[0]['images'] ),
                             list_to_dict(child_part[3])
                             )
                
        rootObject = t(parts)
        return rootObject

def list_to_dict(l):
        d = dict()
        for item in l:
                d[item[0]] = item[1]
        return d

def load_object_class(name):
        print ( "iii Modules.Object.Loader.load_object_class importing clas: '{0}'".format("Modules.Object.CustomObjects."+name))
        m = __import__("Modules.Object.CustomObjects."+name, {}, {}, [name])
        return getattr( m, name )

def load_images(imglist):
        r = dict()
        for image in imglist:
                p = "/Users/apple/Projects/Personal/Asteroids/{0}/{1}/{2}".format(get("Objects"),get ( "Objects Images" ), image[1]  )
                print ( "Loading image {0}".format(p))
                img = pygame.image.load(p).convert_alpha()
                
                r[image[0]] = img
        return r
        
def load_part(objname):
        
        #firstly try to read the root file for the object
        print ( "iii Loading object part '{0}'".format(objname) )
        cfg = read_loader_config ( objname )
        
        root = {'name':'',
                'class':'', 
                'mass':0., 
                'images':[],
                'resize':0.,
                'redraw':False,
                'HP':0
                }
        children = []
        controls = []
        customs = []
        for cfgline in cfg:
                name = cfgline[0]
                params = cfgline[1]
                
                if name == "Name":
                        root['name']=params
                if name == "Class":
                        root['class']=params
                elif name == "Mass":
                        root['mass']=float(params)
                elif name == "AddImage":
                        image = params.split(' ')
                        root['images']+=[[image[0], image[1]]]
                elif name == "Position":
                        image = params.split(' ')
                        root['pos']=Vector25D(float(image[0]), float(image[1]), float(image[2]))
                elif name == "Redrawn":
                        if params == "True":
                                root['redraw'] = True
                        else:
                                root['redraw'] = False
                elif name == "Resize":
                        root['resize'] = float(params)
                elif name == "HP":
                        root['HP'] = int(params)
                elif name == "Add":
                        child = params.split(' ')
                        children.append({ 'name': child[0], 
                                      'type':child[1], 
                                      'pos':Vector25D(float(child[2]), float(child[3]), float(child[4]))})
                elif name == "AddControl":
                        control = params.split(' ')
                        controls.append({ 'name': control[0] ,
                                     'objname': control[1],
                                     'coefficient': float(control[2]),
                                   })
                else: #this is a custom per-class control
                        customs.append ( [ name, params ] ) 
        if root['class']=='':
                 sys.exit ( "!!! Modules.Object.Loader load_part type not set up!" )        
        return [root, children, controls, customs]

'''class Loader():
        
        This is a class to load the objects from files.
        
        
        
        def __init__(objname):
                print (
                Creates an instance of loader class
                Argument:
                - objname: name of the Object to be loaded
                )
                
                obj = dict()
                
        def load_object(objname):
                '''
                

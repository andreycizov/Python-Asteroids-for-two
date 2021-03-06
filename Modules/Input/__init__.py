'''
03.12.2010 Andrej Cizov

Input module for the game
'''

'''

TODO: MUST DO THIS TOMORRROW

'''


import pygame

# For mapping of the mouse moves and clicks over the objects
MOUSE_OVER=1000
MOUSE_DOWN=1001
MOUSE_UP=1002

class Input():
        def __init__(self):
                self.init_mappings()
        
        
        def init_mappings(self):
                '''
                
                '''
                self.key_to_reaction = dict()
                self.key_states = dict()
                
        def add_key_to_reaction ( self, key, to ):
                for k in to:
                        controls = k['part_obj'].get_controls()
                        k['function'] = controls[0]
                        k['function_end'] = controls[1]
                self.add_mapping( self.key_to_reaction, key, to )
                self.key_states[key] = False

        def add_mapping(self, dictionary, key, to):
                try:
                        dictionary[key] += to
                except:
                        dictionary[key] = to
                        
        def remove_by_parent(self, parents):
                for parent in parents:
                        for key, reactions in self.key_to_reaction.items():
                                for reaction in reactions:
                                        if reaction['part_obj'].parent == parent:
                                                self.key_to_reaction[key].remove(reaction)
                        
        def tick (self):
                for e in pygame.event.get():
                        if e.type == pygame.KEYUP:
                                key = e.dict['key']
                                try:
                                        reactions = self.key_to_reaction[key]
                                except KeyError:
                                        continue
                                self.key_states[key] = False
                                for r in reactions:
                                        r['function_end'](r['part_obj'])
                        if e.type == pygame.KEYDOWN:
                                key = e.dict['key']
                                self.key_states[key] = True
                                
                                print (key)
                
                for key, reactions in self.key_to_reaction.items():
                        if self.key_states[key]:
                                for r in reactions:    
                                        r['function'](r['part_obj'], r['coefficient'])
                                        '''if r['part_obj'].parent.HP > 0:
                                               
                                        else:
                                                reactions.remove(r)'''
                        
        

'''
Created by Andrej Cizov on 02.12.2010

defines config file reader class

this is usually a singleton
'''

import io
import sys
import os

class ConfigReader ( ):
        '''
        Reads a config file to a dictionary and holds it for the application lifetime
        '''
        def __init__(self, filename):
                '''
                filename to open on class creation
                '''
                self.settings = dict()
                
                cfgfile = io.open ( filename )
                
                lines = cfgfile.readlines ( )
                
                for line in lines:
                        line_parts = line.split('=')
                        try:
                                self.settings[line_parts[0]] = line_parts[1].rstrip(" "+os.linesep)
                        except:
                                pass

        def get(self, name):
                '''
                Gets a setting from a dictionary
                '''
                return self.settings[name]
                
class ConfigReader2 ( ):
        '''
        Reads a config file to a dictionary and holds it for the application lifetime
        '''
        def __init__(self, filename):
                '''
                filename to open on class creation
                '''
                self.settings = []
                
                cfgfile = io.open ( filename )
                
                lines = cfgfile.readlines ( )
                
                for line in lines:
                        line_parts = line.split('=')
                        try:
                                self.settings += [[line_parts[0], line_parts[1].rstrip(" "+os.linesep)]]
                        except:
                                pass


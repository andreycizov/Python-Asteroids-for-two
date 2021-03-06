'''
Created by Andrej Cizov on 02.12.2010

Config file reader
Reads config file on module import
'''
import Modules.Config.Config
import sys

DEFAULTCONFIG="./config.txt"

print ("iii Config module loaded")
print ("iii Default config file is {0}".format(DEFAULTCONFIG))

'''
Configuration singleton instance creation
'''
try:
        ApplicationConfig = Config.ConfigReader(DEFAULTCONFIG)
except:
        sys.exit( "!!! Config could not open configuration file '{0}'".format(DEFAULTCONFIG) )

print ( "iii Configuration file loaded" )

def get(name):
        '''
        Gets the configuration setting from a config singleton
        '''
        global ApplicationConfig
        try:
                return ApplicationConfig.get(name)
        except:
                sys.exit( "!!! Config::get() Could not get the configuration setting for '{0}'".format(name) )

                

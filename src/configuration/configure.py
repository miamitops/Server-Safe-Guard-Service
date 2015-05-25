# ********************************************************************
#                                                                    *
# FOR: http://unhcr-nairobi-hub.org                                  *
# FILE: "config.ini"                                                 *
# VERSION: 0.2-dev                                                 *
# UPDATE: Thu, 23 Apr 2015                                           *
# AUTHOR: Miami, (miami@unhcr.org, vokestops@gmail.com)              *
# PURPOSE: This is the primary configuration loader for              *
#     the remote system backup and maintenance system                *
#                                                                    *
#                                                                    *
# ********************************************************************

#### BEGIN PROGRAM LOGIC ####
'''
Created on Apr 23, 2015

@author: Miami
'''
import ConfigParser, os
import string
configFolder = os.getcwd()
cFile = os.path.abspath('configuration/config.ini')
class Configure(object):
    '''
    classdocs
    '''
    def LoadConfig(self, lFile = cFile, config={}):
        """
        returns a dictionary with keys of the form
        <section>.<option> and the corresponding values
        """
        print(cFile)  
        config = config.copy( )
        cp = ConfigParser.ConfigParser( )
        cp.read(lFile)
        for sec in cp.sections( ):
            name = string.lower(sec)
            for opt in cp.options(sec):
                config[name + "." + string.lower(opt)] = string.strip(cp.get(sec, opt))
        return config


    def __init__(self):
        '''
        Constructor
        '''  
            
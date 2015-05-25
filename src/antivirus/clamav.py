'''
Created on Apr 24, 2015

@author: miami
'''
import os
import subprocess

class clamavAv(object):
    '''
    classdocs
    '''
    def update(self):
        '''
        update antivirus
        '''
        os.system('freshclam')
        
    def avScan(self, scanDir = '/var/www/html/'):
        '''
        Scan a directory
        '''
        scanDir = str(scanDir)
        print('performing scan' '''+str(scanDir)''')
        scan = os.system("clamscan " + "-r " + scanDir)
        if scan == 0:
            print('scan was successful')
    def genReport(self, scanDir):
        '''
        generate a report for scan
        '''
        genReport = {}
        return genReport
    def removeFile(self, rFile):
        '''
        remove an infected file
        '''

    def __init__(self):
        '''
        Constructor
        '''
        
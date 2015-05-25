#!/usr/local/bin/python2.7
'''
Created on Apr 23, 2015

@author: Miami
'''
import os
import client as clientele
import server as servlet

def main():
    from sys import argv
    myargs = getopts(argv)
    if '-i' in myargs:
        print(myargs['-i'])
    #skipping directories and files
    if '-s' in myargs:
        system = myargs['-s']
        clamavScan(system, '/var/www/html/ray/')
    #skipping directories and files
    if '--skip' in myargs:
        '''
        skip a directory
        '''
        print(myargs['--skip'])
        
    #Skipping antivirus scan
    if '--no-scan' in myargs:
        ''' do not scan for viruses
        '''
        
    #print(myargs)
    #print(os.environ.keys())
    #print(os.environ['USERNAME'])
    #user = os.system('echo $UID')
    #if user == 0 :
    #    print( "not allowed" + str(user) )
    #else:
    #    print("allowed " + user)
def clamavScan(system, directory = '/var/www/html/'):
    '''
    scan files on the server
    '''
    if system == 'client':
        os.system('clamscan -r {}', (directory))
    elif system == 'server':
        #perform scan on server
        clientele.doScanserver('clamav', '/var/www/html/ray/')
#update antivirus
#scan for viruses return report
#count files
#remove infected files
#count files
#scan for virus again
#if no virus is found. rsync files

#@local machine
# -update antivirus
# -scan for viruses
# -remove infected files
#@Restore
# -Scan for viruses
# -Get difference btwn backup and live
#@Maintenance 
# - start and stop services
# - Check server loads
# - Check services are healthy
# - 
def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
            argv = argv[2:]
        else:
            argv = argv[1:]
    return opts
def runmail():
    print('mail chimp')
    print(os.system('ls -la ../ >> new.txt'))
if __name__ == '__main__':
    main()
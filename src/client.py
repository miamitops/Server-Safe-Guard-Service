#!/usr/local/bin/python2.7
'''
Created on Apr 24, 2015

@author: Miami
'''
import sys, os
from socket import *  
from configuration import configure

##Configuration
clientConfig = configure.Configure()                   # portable socket interface plus constants
loadedConf = clientConfig.LoadConfig()
sHost = loadedConf['settings.server']                                    # server name, or: 'starship.python.net'
sPort = int(loadedConf['settings.serverport'])                           # non-reserved port used by the server

#Begin Logic
def action(activity):
    if activity == 'check-connection':
        print('checking connection')
    elif activity == 'scan':
        print('do aV scan')
    else:
        print('default action')
def main():
    '''
    the main function definition
    '''
    doScanserver('clamav', '/var/')
def doScanserver(method, directory):
    conStatus = checkConnection()
    if conStatus['success'] == 0:
        print(conStatus['respon'])
    elif conStatus['success'] == 1:
        scanServer(method, directory)
    elif conStatus['success'] == 2 :
        print(conStatus['respon'])    
def checkConnection():
    mts = 'connect' 
    message = [b'{}', (mts) ]        # default text to send to server
                                                            # requires bytes: b'' or str,encode()
    try:
        sockobj = socket(AF_INET, SOCK_STREAM)          # make a TCP/IP socket object
        sockobj.connect((sHost, sPort))                 # connect to server machine + port
        for line in message:                            # send line to server over socket
            sockobj.send(line)                                  # receive line from server: up to 1k
            data = sockobj.recv(1024)
        if str(data) == 'Echo=>Success':
            respon = 'Connection was successful, proceed to next command'
            success = 1            
        else:
            respon = 'Connection was successful but client did not receive the correct response from server, the server says ' + str(data)
            success = 2
            #print('Client received:', respon) 
            # bytes are quoted, was `x`, repr(x)
    except:
        respon = ('Could not connect to server at ' + sHost + ' on port ' + str(sPort))
        success = 0
        
    sockobj.close()
    tRet = {}
    tRet['success'] = success
    tRet['respon'] = respon
    return tRet
def createConnection():
    try:
        sockobj = socket(AF_INET, SOCK_STREAM)          # make a TCP/IP socket object
        sockobj.connect((sHost, sPort))                 # connect to server machine + port
        return sockobj
    except:
        return
def scanServer(sockobj, directory): 
    mts = 'scan' 
    message = [b'{}', (mts) ]  
    sockobj = createConnection()
    for line in message:                            # send line to server over socket
        sockobj.send(line)                                  # receive line from server: up to 1k
        data = sockobj.recv(1024)
    if str(data) == 'please provide a directory':
        #print('the server is requesting a directory to scan')
        supDirect = [b'' +directory ]
        for line in supDirect: 
            sockobj.send(line)                                  # receive line from server: up to 1k
            datab = sockobj.recv(1024) 
        print(datab)
        respon = 'server is requesting a directory'
        success = 1
    else:
        respon = 'Connection was successful but client did not receive the correct response from server, the server says ' + str(data)
        success = 0
            #print('Client received:', respon) 
            # bytes are quoted, was `x`, repr(x)                                                                              # close socket to send eof to server
    
if __name__ == '__main__':
    main()
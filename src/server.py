#!/usr/local/bin/python2.7
from socket import *
serverHost = ''
serverPort = 22000
def main():
    initServer()
def initServer():
    sockobj = socket(AF_INET, SOCK_STREAM) # make a TCP socket object
    sockobj.bind((serverHost, serverPort)) # bind it to server port number
    sockobj.listen(5) # listen, allow 5 pending connects
    while True: 
        connection, address = sockobj.accept()      # listen until process killed
        print('Server connected by', address)       # wait for next client connect
        logFile = open('serverLog.txt', 'a')
        logFile.write('\n Server connected by ' + str(address) +'\n');
        logFile.close() 
        
        while True:                                 # connection is a new socket
            data = connection.recv(1024)
            
            if str(data) == 'connect':              # read next line on client socket
                '''perform
                '''
                respon = 'Success'                  
                #Respond with Success if connection ws successful
            elif str(data) == 'exec':
                '''
                execute something
                '''
                import os
                os.system('ls -la >> serverLog.txt')
                respon = 'exec'
            elif str(data) == 'scan':
                connection.send(b'please provide a directory')
                sDirectory = connection.recv(1024)
                doScan(sDirectory)
                #print(sDirectory)
                connection.send('directory was scanned')
                
                #doScan('/var/www/html/ray/')
                respon = 'scan complete'
            elif not data: break
            else:
                dcop = str(data)
                respon = 'The command : ' + '{}' + ' was not found on server :' , (str(dcop)) 
                # send a reply line to the client
            connection.send(b'Echo=>' + str(respon))       # until eof when socket closed 
        connection.close()
def doScan(sDirectory): 
    #perform a scan on this server
    from antivirus import clamav
    clamAD = clamav.clamavAv()          #New class of antivirus
    clamAD.avScan(sDirectory)

if __name__ == '__main__':
    main()   
import socket
import sys
 
## Keep host empty, switch to localhost when it doesn't work.
HOST = '' 
PORT = 80
 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
try:
    # s.setsockopt(SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))    ## Binding socket
    
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
	
print('Socket bind complete')

## Accept a max of 10 connections
s.listen(10)
conn, addr = s.accept()

## Print connection details
print('Connected with ' + addr[0] + ':' + str(addr[1]))

import socket, sys, logging
from _thread import *


logging.basicConfig(filename='proxy.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

try:
    listening_port = int(input("#-------------------\n\t Enter a port number to listen on: "))
except KeyboardInterrupt:
    print("\n#-------------------\nProxy shutdown command received...")
    print("Shutting down proxy server...Goodbye!")
    sys.exit()

max_connections = 10
buffer_size = 8192

## This is the listener socket code
def start():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("--- Initializing socket")
        s.bind(('', listening_port))
        print("--- Binding socket to port :"+str(listening_port))
        s.listen(max_connections)
        print("--- Proxy server started")
    except Exception as e:
        print("--- ERROR ---\nSocket Initialization failed. Server could not be started")
        logging.error("--- ERROR ---\nSocket Initialization failed. Server could not be started")
        logging.error(e)
        sys.exit(2)

    while True:
        try:
            conn, addr = s.accept()
            data = conn.recv(buffer_size)
            ## Start new thread for the connection, and send con
            start_new_thread(conn_string, (conn, data, addr))
            
        except KeyboardInterrupt:
            s.close()
            print("\nKeyboard Interrupt received.\nShutting down proxy server...Goodbye!")
            sys.exit(1)
    s.close()

## conn_string would decide where the packet should be sent.
def conn_string(conn, data, addr):
    try:
        print(data)
            # # Extracting first line
            # first_line = data.split('\n')[0]
            
            # url = first_line.split(' ')[1]
            
            # http_pos = url.find("://")
            # if(http_pos == -1):
            #     temp = url
            # else:
            #     temp = url[(http_pos+3):]
            
            # port_pos = temp.find(':')

            # webserver_pos = temp.find("/")
            # if(webserver_pos == -1):
            #     webserver_pos = len(temp)
            # webserver = ''
            # port = -1
            # if(port_pos == -1 or webserver_pos < port_pos):
            #     port = 80
            #     webserver = temp[:webserver_pos]
            # else:
            #     port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
            #     webserver = temp[:port_pos]
        
        ## Add switch logic here ---------------
        proxy_server('172.18.0.2', 443, conn, addr, data)
    except Exception as e:
        pass


## Function to proxy the connection to correct docker container.
def proxy_server(webserver, port, conn, addr, data):
    try:
        print('here3')
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('here1')
        try:
            s1.connect((webserver, port))
        except Exception as e:
            print(e)
        print('here2')
        s1.send(data)

        while True:
            print('here')
            reply = s1.recv(buffer_size)
            print(reply)
            if(len(reply) > 0):
                conn.send(reply)

                dar = float(float(len(reply))/1024)
                dar = "%.3s" % (str(dar))
                dar = "%s KB" % (dar)

                print("--- Request done: %s => %s <=" % (str(addr[0]), str(dar)))
            else:
                break
        s1.close()
        conn.close()
    except socket.error:
        s1.close()
        conn.close()
        sys.exit()
                

## Replace this with if main code snippet. This is the entry point of code.
start()
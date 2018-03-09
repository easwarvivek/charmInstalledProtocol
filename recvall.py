
import time,socket

def recvall(the_socket,timeout=''):
    #nullified now - #setup to use non-blocking sockets
    #if no data arrives it assumes transaction is done
    #recv() returns a string
    #the_socket.setblocking(0)
    total_data=[]
    data=''
    begin=time.time()
    if not timeout:
        timeout=0.1
    while True:
        #if you got some data, then break after wait sec
        if total_data and time.time()-begin>timeout:
            break
        #if you got no data at all, wait a little longer
        elif time.time()-begin>timeout*2:
            break
        try:
            data=the_socket.recv(4096)
            if data:
                total_data.append(data)
                begin=time.time()
                data=''
            else:
                time.sleep(0.01)
        except:
            pass
        #When a recv returns 0 bytes, other side has closed
    result=b''.join(total_data)
    return result

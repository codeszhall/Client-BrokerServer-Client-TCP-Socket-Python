import socket
import threading

s = socket
IPv4 = s.AF_INET
TCP = s.SOCK_STREAM
ss = s.socket(IPv4, TCP)

HOST = ""
PORT = 12345
ss.bind((HOST, PORT))

elgib_host = 1000
ss.listen(elgib_host)

buffer_size = 1024

endecode_data0 = "ascii"
endecode_data1 = "UTF-8"

clients_list = []

err_kbrd_intrpt = KeyboardInterrupt

def on_new_client_thread(conn):
    global s
    global clients_list
    global err_kbrd_intrpt

    try:
        status_success_response = "200 OK"
        while 1 :    
            message = conn.recv(buffer_size)
            message = message.decode(endecode_data0)
            message = status_success_response + message
            message = message.encode(endecode_data0)

            for utas_in_thread in clients_list :
                if conn != utas_in_thread :
                    utas_in_thread.send(message)
                        
    except (s.error, err_kbrd_intrpt):
                conn.close()
                clients_list.remove(conn)
                print ("Client", client_addr, "out of connection")
try:
    while True :
        conn, addr = ss.accept()
        client_addr = str(addr[0])
        port_bound = str(addr[1])
        clients_list.append(conn)
        print ("Succesfully connected to ("+client_addr+":"+port_bound+")")
        new_thread = threading.Thread(target=on_new_client_thread, args=(conn,))
        new_thread.start()
except KeyboardInterrupt:
        print ("...Server is going to be hibernate...","\n","Thank You")
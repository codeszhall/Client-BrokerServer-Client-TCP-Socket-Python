import socket

s = socket
IPv4 = s.AF_INET
TCP = s.SOCK_STREAM
ss = s.socket(IPv4, TCP)

HOST = "127.0.0.1"
PORT = 12345
ss.connect((HOST, PORT))

buffer_size = 1024

endecode_data0 = "ascii"

while 1 :
    message = ss.recv(buffer_size).decode(endecode_data0)
    print("Status:", message[:6], " Pesan:",message[6:])

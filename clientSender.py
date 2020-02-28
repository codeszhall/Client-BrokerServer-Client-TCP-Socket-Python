import socket

s = socket
IPv4 = s.AF_INET
TCP = s.SOCK_STREAM
ss = s.socket(IPv4, TCP)

HOST = "127.0.0.1"
PORT = 12345
ss.connect((HOST, PORT))

endecode_data0 = "ascii"

while 1 :
    message = input("Send message >> ")
    message = message.encode(endecode_data0)
    ss.send(message)

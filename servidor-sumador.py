#!/usr/bin/python3

import socket
import calculadora

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

ok_html = ("HTTP/1.1 200 OK\r\n\r\n" +
        "<html><head><meta charset='utf-8'><h1>X-Serv-14.5-Sumador-Simple" +
        "</h1></head><body><p>CALC</p></body></html>\r\n")

favicon_html = ("HTTP/1.1 404 Not Found\r\n\r\n" +
                "<html><body><p>404 Not Found</p></body></html>\r\n")

usage = "Usage: localhost:1234/operand1/function/operand2"

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        Request = recvSocket.recv(2048).decode('utf-8')
        print(Request)
        # ---------
        
        input = Request.split()[1].split('/')[1:]
        print(input)

        if 'favicon.ico' in input:
            print("404")
            recvSocket.send(favicon_html.encode('utf-8'))
            recvSocket.close()
            continue

        if '' in input:
            output = usage
        else:
            try:
                output = calculadora.calculator(input[1], input[0], input[2])
            except IndexError:
                output = usage
        print(output)

        print('Answering back...')
        response = ok_html.replace('CALC', output)
        print(response)
        recvSocket.send(response.encode('utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()

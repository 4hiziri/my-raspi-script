import socket
from pyzbar.pyzbar import decode
from PIL import Image
import time


if __name__ == '__main__':
    host = '192.168.11.5'
    port = 9191

    i = 0
    while True:
        print(i)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        i += 1
        sock.send(b'take')

        recvlen = 100
        buffer = b''
        while recvlen > 0:
            receivedstr = sock.recv(1024 * 8)
            recvlen = len(receivedstr)
            buffer += receivedstr
        sock.close()

        with open('test.jpg', 'wb') as f:
            f.write(buffer)

        data = decode(Image.open('test.jpg'))

        if len(data) != 0:
            print('success')

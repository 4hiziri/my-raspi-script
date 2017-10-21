import socketserver
import picamera
import time

tmpfile = 'tmp.jpg'

# {'washedout': 18, 'negative': 1, 'blur': 15, 'hatch': 10, 'colorbalance': 21, 'deinterlace1': 23, 'solarize': 2, 'gpen': 11, 'oilpaint': 9, 'emboss': 8, 'saturation': 16, 'denoise': 7, 'cartoon': 22, 'none': 0, 'colorswap': 17, 'posterise': 19, 'pastel': 12, 'deinterlace2': 24, 'colorpoint': 20, 'film': 14, 'watercolor': 13, 'sketch': 6}


def unsharp_masking():
    pass


def take_pic():
    with picamera.PiCamera() as camera:
        camera.resolution = (2592, 1944)
        camera.sharpness = 100

        camera.start_preview()
        time.sleep(1)  # カメラ初期化
        camera.capture(tmpfile)


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()

        if data == b'take':
            take_pic()

            with open(tmpfile, 'rb') as f:
                payload = f.read()
            self.request.send(payload)


if __name__ == '__main__':
    host = '192.168.11.5'
    port = 9191

    server = socketserver.TCPServer((host, port), TCPHandler)
    server.serve_forever()

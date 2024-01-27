from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

class MyRequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Simpan data ke dalam file (gantilah sesuai kebutuhan)
        with open('downloaded_image.jpg', 'wb') as f:
            f.write(post_data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Image successfully uploaded')

if __name__ == "__main__":
    PORT = 8000  # Port yang akan digunakan oleh server
    handler = MyRequestHandler

    with TCPServer(("", PORT), handler) as httpd:
        print(f"Sedang mendengarkan di port {PORT}")
        httpd.serve_forever()

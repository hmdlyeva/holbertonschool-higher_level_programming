import http.server
import json
import socketserver


class NewHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write('404 Not Found'.encode())


with socketserver.TCPServer(("", 8000), NewHandler) as httpd:
    print(f"Serving at port {8000}")
    httpd.serve_forever()

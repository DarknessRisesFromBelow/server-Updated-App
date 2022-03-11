import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer


def some_function():
    return '1.09'

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/update' in self.path:

            b = self.path.replace("/update", "")
            a = some_function()
            if(float(a) > float(b)):
                self.send_response(200) 
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("you need to update to version {}!".format(a).encode("utf-8")))
                 
            else:
                self.send_response(200) 
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("you dont need to update!".encode("utf-8")))

httpd = socketserver.TCPServer(("", 8080), MyHandler)
httpd.serve_forever()

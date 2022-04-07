import socketserver
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


version = 0
versionIncrementation = 1
strings = []
os.chdir("Your projects files path here.")

def GetLatestVersion():
    global strings
    global version
    if(GetAllFiles() != strings or strings == null):
        strings = GetAllFiles()
        version = version + versionIncrementation
        return version

def GetAllFiles():
    return os.listdir(".")

def GetFile(name):
    if(name.startswith('.') == False and "." in name):
        f = open("{}".format(name), "r")
        return (f.read())
    else:
        return ("1")
    

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/update' in self.path:
            b = self.path.replace("/update", "")
            a = GetLatestVersion()
            if(float(a) > float(b)):
                a = GetAllFiles()
                self.send_response(200, message = None) 
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("{}".format(a).encode("utf-8")))
            else:
                self.send_response(200, message = None) 
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes("you dont need to update!".encode("utf-8")))
        else:
            self.send_response(200, message = None) 
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("{}".format(GetFile(self.path.replace("%20", " ").replace("/", ""))).encode("utf-8")))

httpd = socketserver.TCPServer(("", 8080), MyHandler)
httpd.serve_forever()

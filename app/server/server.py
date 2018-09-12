#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from os import curdir, sep

#https://gist.github.com/bradmontgomery/2219997

class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    #https://www.acmesystems.it/python_http
    def do_GET(self):
        if self.path == "/":
            self.path="/index.html"

        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                sendReply = True
            elif self.path.endswith(".jpg"):
    			mimetype='image/jpg'
    			sendReply = True
            elif self.path.endswith(".gif"):
                mimetype='image/gif'
                sendReply = True
            elif self.path.endswith(".js"):
                mimetype='application/javascript'
                sendReply = True
            elif self.path.endswith(".css"):
                mimetype='text/css'
                sendReply = True
            elif self.path.endswith(".json"):
                mimetype='application/json'
                sendReply = True
            elif self.path.endswith(".ico"):
                mimetype='application/image/x-icon'
                sendReply = True

            if sendReply:
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)


    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

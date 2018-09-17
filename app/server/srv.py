from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
from os import curdir, sep
import json
from main import getJsonGraph

#https://gist.github.com/bradmontgomery/2219997
class S(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    #https://www.acmesystems.it/python_http
    def do_GET(self):
        if self.path == "/":
            self.path="index.html"
        enc = ""
        try:
            sendReply = False
            if self.path.endswith(".html"):
                mimetype='text/html'
                enc = "utf8"
                sendReply = True
            elif self.path.endswith(".jpg"):
                mimetype='image/jpg'
                enc = "jpg"
                sendReply = True
            elif self.path.endswith(".gif"):
                mimetype='image/gif'
                enc = "gif"
                sendReply = True
            elif self.path.endswith(".js"):
                mimetype='application/javascript'
                enc = "utf8"
                sendReply = True
            elif self.path.endswith(".css"):
                mimetype='text/css'
                enc = "utf8"
                sendReply = True
            elif self.path.endswith(".json"):
                mimetype='application/json'
                enc = "utf8"
                sendReply = True
            else:
                return;
            """
            elif self.path.endswith(".ico"):
                mimetype='application/image/x-icon'
                enc = "ico"
                sendReply = True
            """

            if sendReply and enc != "":
                f = open(curdir + sep + "../client/" + self.path)
                self.send_response(200)
                self.send_header('Content-type',mimetype)
                self.end_headers()
                self.wfile.write(bytes(f.read(), enc))
                f.close()

        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        d = getJsonGraph(post_body);
        with open('output.json', 'w') as outfile:
            json.dump(d, outfile)
        f = open(curdir + sep + "output.json")
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(bytes(f.read(), "utf8"))

def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

#!/usr/bin/python
import time
import mimetypes
import os
import BaseHTTPServer


HOST_NAME = 'localhost' 
PORT_NUMBER = 8000 
BASE_RESOURCE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/resources/'


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        """Respond to a GET request."""
        if s.path == '/':
            path = 'index.html'
        else:
            path = s.path

        if os.path.isfile(BASE_RESOURCE_DIR + path):
            serve_file(s, path)
        else:
            response_404(s)
        

def serve_file(s, path):
    """ Send an serve a file, if it exists response """
    mimetype,a = mimetypes.guess_type(path)
    s.send_response(200)
    s.send_header("Content-type", mimetype)
    s.end_headers()
    f = open (BASE_RESOURCE_DIR + path)
    s.wfile.write(f.read())
    

def response_404(s):
    """ Send  a 404 response """
    s.send_response(404)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write("<html><head><title>Title goes here.</title></head>")
    s.wfile.write("<body><p>The path you entered could not be found.</p>")
    s.wfile.write("</body></html>")

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)


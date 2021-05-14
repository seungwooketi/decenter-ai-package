from io import StringIO
from  http.server import BaseHTTPRequestHandler

class AIReqHandler(BaseHTTPRequestHandler):

    def __init__(self, inText, outFile):
        self.rfile = StringIO.StringIO(inText)
        self.wfile = outFile
        BaseHTTPRequestHandler.__init__(self, "", "", "")

    def setup(self):
        pass

    def handle(self):
        BaseHTTPRequestHandler.handle(self)

    def finish(self):
        BaseHTTPRequestHandler.finish(self)

    def address_string(self):
        return "dummy_server"

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>WoW</title></head>")
        self.wfile.write("<body><p>This is a Total Wowness</p>")
        self.wfile.write("</body></html>")

    def do_POST(self):
        """ """

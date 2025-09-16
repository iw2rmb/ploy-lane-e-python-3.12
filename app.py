from http.server import BaseHTTPRequestHandler, HTTPServer
import os
class H(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/healthz': self.send_response(200); self.end_headers(); self.wfile.write(b'ok'); return
    self.send_response(200); self.end_headers(); self.wfile.write(b'hello')
port = int(os.environ.get('PORT','8080'))
HTTPServer(('',port), H).serve_forever()

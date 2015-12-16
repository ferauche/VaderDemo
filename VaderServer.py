import cgi
import sys
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import vader

class MainHandler(BaseHTTPRequestHandler):

   def do_GET(self):
	p = self.path.split("?")
	path = p[0][1:].split("/")
	params = {}
	if len(p) > 1:
		params = cgi.parse_qs(p[1],True,True)
	print params
	print params['vader'][0]
	if params['vader'][0]=='0':
		vader.power_darkside()
	if params['vader'][0]=='1':
		vader.breathing()
	if params['vader'][0]=='2':
		vader.dont_make_destroy()
	if params['vader'][0]=='3':
		vader.dont_fail()
	if params['vader'][0]=='4':
		vader.dont_comeback()	

def main(port):
	try:
		server = HTTPServer(('',int(port)),MainHandler)
		print "Servidor Iniciado na porta ", port
		server.serve_forever()
	except KeyboardInterrupt:
		print '^C recebido, servidor desligado!'
		server.socket.close()

if __name__ == '__main__':
	main(sys.argv[1])


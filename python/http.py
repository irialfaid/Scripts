#!/usr/bin/env python
#Just copied from python.org with an easy way to change the port added. Currently broken
from __future__ import print_function
import SimpleHTTPServer
import SocketServer

port = int(raw_input("Enter port number: ")

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print ("serving at port", PORT)
httpd.server_forever()

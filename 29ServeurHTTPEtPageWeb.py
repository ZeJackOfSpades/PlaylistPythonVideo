#coding:utf-8
"""
TODO	:	FINIR LA VIDEO !
"""
import http.server
import socketserver

port 	=	8080
adress	=	("", port) # "" pour l'adresse en local

handler	=	http.server.SimpleHTTPRequestHandler
httpd 	=	socketserver.TCPServer(adress, handler)

print("Serveur démarré sur le PORT {}".format(port))

httpd.serve_forever()



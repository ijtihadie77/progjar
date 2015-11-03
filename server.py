import threading
import socket
import time
import sys

def handle_get(client_socket, uri):
	client_socket.send('Hai Apa Kabar ')
	return

def handle_post(client_socket,uri):
	client_socket.send('Hai Apa Kabar POST')
	return


class MemprosesClient(threading.Thread):
	def __init__(self,client_socket,client_address,nama):
		self.client_socket = client_socket
		self.client_address = client_address
		self.nama = nama
		threading.Thread.__init__(self)
	
	def run(self):
		message = ''
		while True:
        		data = self.client_socket.recv(32)
            		if data:
				message = message + data #collect seluruh data yang diterima
                                if (message.endswith("\r\n\r\n")):  #pada webserver, request diakhiri dengan CRLF CRLF
                                        all_request = message.split("\r\n") #memisahkan header satu dengan yang lain
					# reply ke client dengan sesuatu
					request_pertama = all_request[0].split(' ')
					tipe_request = request_pertama[0]
					uri = request_pertama[1]
					versi_http = request_pertama[2]
					if (tipe_request=='GET'):
						handle_get(self.client_socket, uri)
					if (tipe_request=='POST'):
						handle_post(self.client_socket, uri)
					break

            		else:
               			break
		self.client_socket.close()
		


class Server(threading.Thread):
	def __init__(self):
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_address = ('localhost',9999)
		self.my_socket.bind(self.server_address)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.listen(1)
		nomor=0
		while (True):
			self.client_socket, self.client_address = self.my_socket.accept()
    			nomor=nomor+1
			#---- menghandle message cari client (Memproses client)
			my_client = MemprosesClient(self.client_socket, self.client_address, 'PROSES NOMOR '+str(nomor))
			my_client.start()
			#----


serverku = Server()
serverku.start()



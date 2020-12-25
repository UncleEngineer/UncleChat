# chat-server.py

import socket
import datetime
import threading
import random

PORT = 8500
BUFSIZE = 4096
#SERVERIP = 'localhost' # YOUR IP
SERVERIP = '159.65.135.242'
clist = [] # Client List
cdict = {}
pvroom = {}
pvdict = {}

allroomnumber = []
allroomnumber.append(10001) # create default room
pvdict[10001] = [] # create default room
def client_handler(client,addr):
	while True:
		try:
			data = client.recv(BUFSIZE)
			check = data.decode('utf-8').split('|')
			# check = ['NAME','UNCLE']
			# check = ['ROOM','NEW']
			# check = ['JOIN','19999','UNCLE']
			# check = ['MSG','19999','HELLO WORLD']
			if check[0] == 'NAME':
				cdict[str(addr)] = check[1]
			elif check[0] == 'ROOM':
				rn = random.randint(10010,99999)
				while rn in allroomnumber:
					rn = random.randint(10010,99999)
				allroomnumber.append(rn)
				if rn not in pvdict:
					pvdict[rn] = []
				newroom = 'newroom|{}'.format(rn)
				client.sendall(newroom.encode('utf-8'))
				print('PVDICT:',pvdict)
			elif check[0] == 'JOIN':
				rnumber = int(check[1])
				pvdict[rnumber].append(client)
				cdict[str(addr)] = check[2]
				pvroom[str(addr)] = rnumber
				username = cdict[str(addr)]
				for c in pvdict[rnumber]:
					c.sendall('เพิ่ม {} เข้ากลุ่มแล้ว'.format(username).encode('utf-8'))

		except Exception as e:
			
			try:
				client.sendall('q'.encode('utf-8'))
				print(e)
				rnum = pvroom[str(addr)]
				pvdict[rnum].remove(client)
				username = cdict[str(addr)]
				for c in pvdict[rnum]:
						c.sendall('{} ได้ออกจากกลุ่มแล้ว'.format(username).encode('utf-8'))
				print('REMAIN: ',len(pvdict[rnum]))
				break
			except Exception as e:
				print(e)
				break

		
		cnlist = ['NAME','ROOM']
		if check[0] not in cnlist:
			
			if check[0] == 'MSG':
				# check = ['MSG','170144','HELLO']
				roomnumber = int(check[1])

				try:
					username = cdict[str(addr)]
					msg = username + '>>> ' + check[2]
				except:
					msg = str(addr) + '>>> ' + check[2]

				for c in pvdict[roomnumber]:
					c.sendall(msg.encode('utf-8'))

	client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.bind((SERVERIP,PORT))
server.listen(5)

while True:
	client, addr = server.accept()
	print(addr)
	print('ALL CLIENT: ', len(pvroom))

	task = threading.Thread(target=client_handler, args=(client, addr))
	task.start()
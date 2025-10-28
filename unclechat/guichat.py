# GUI-Chat.py
from tkinter import *
from tkinter import ttk, messagebox
import tkinter.scrolledtext as st
from tkinter import simpledialog

####################NETWORK##########################
import socket
import threading
import sys

PORT = 8500
BUFSIZE = 4096
SERVERIP = '159.223.46.145' # SERVER IP
#SERVERIP = '192.168.1.150'

status = False

global client

def server_checkroom(client):

	global data
		
	try:
		data = client.recv(BUFSIZE) # Data from server
		data = data.decode('utf-8')
		ldata = data.split('|')
		#print('LIST DATA',ldata)
	except:
		print('ERROR')
		

	if ldata[0] == 'newroom':
		v_roomnumber.set(ldata[1])
	elif ldata[0] == 'noroom':
		v_roomnumber.set(ldata[2])
		messagebox.showinfo('ห้องรวม 1','ลุงให้เข้าไปแชทในห้องรวมนะจ๊ะ')

	client.close()
	

def server_handler(client):
	global status
	while True:
		try:
			data = client.recv(BUFSIZE) # Data from server
		except:
			print('ERROR')
			break
		if (not data) or (data.decode('utf-8') == 'q'):
			print('OUT!')
			break

		allmsg.set(allmsg.get() + data.decode('utf-8') + '\n')
		chatbox.delete(1.0,END) # clear old msg
		chatbox.insert(INSERT,allmsg.get()) # insert new
		chatbox.yview(END)
		#print('USER: ', data.decode('utf-8'))


	client.close()
	#messagebox.showerror('Connection Failed','ตัดการเชื่อมต่อ')
	alert = 'ไม่สามารถเชื่อมต่อระบบได้ ต้องการเริ่มใหม่หรือไม่?\n\n-ตรวจสอบเลขห้องว่าถูกต้องหรือไม่\n-กด New Room เพื่อสร้างห้องใหม่ หรือใช้ห้องหลัก "10001"'
	checkenter = messagebox.askyesno('Connection Failed',alert)
	#print('CHECK: ',checkenter)
	if checkenter == True:
		status = False
		GUI2.deiconify()
		v_roomnumber.set('10001')
	else:
		GUI.destroy()

##############################################
GUI = Tk()
#GUI.geometry('650x750+1000+100')

w = 650
h = 700

ws = GUI.winfo_screenwidth() #screen width
hs = GUI.winfo_screenheight() #screen height


x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')


GUI.title('Uncle Chat by Uncle Engineer')

FONT1 = ('Angsana New',35) 
FONT2 = ('Angsana New',20) 
#############chatbox###############
F0 = Frame(GUI)
F0.place(x=5,y=5)

L = ttk.Label(F0,text='Room Number: ',font=FONT2)
roomnumber = StringVar()
roomnumber.set('10001')
LL = ttk.Label(F0,textvariable=roomnumber,font=FONT2)

L.grid(row=0,column=0)
LL.grid(row=0,column=1)


F1 = Frame(GUI)
F1.place(x=5,y=70)

allmsg = StringVar()

chatbox = st.ScrolledText(F1,width=38,heigh=8,font=FONT1)
chatbox.pack(expand=True, fill='x')
#############message form###############
v_msg = StringVar()

F2 = Frame(GUI)
F2.place(x=20,y=600)

E1 = ttk.Entry(F2,textvariable=v_msg,font=FONT2,width=50)
E1.pack(ipady=20)

#############button###############
def SendMessage(event=None):
	msg = v_msg.get()
	#allmsg.set(allmsg.get() + msg + '\n---\n')
	msgsend = 'MSG|{}|{}'.format(roomnumber.get(),msg)
	client.sendall(msgsend.encode('utf-8')) ######SEND to SERVER######
	chatbox.delete(1.0,END) # clear old msg
	chatbox.insert(INSERT,allmsg.get()) # insert new
	chatbox.yview(END)
	v_msg.set('') # clear msg
	E1.focus()

F3 = Frame(GUI)
F3.place(x=500,y=600)
B1 = ttk.Button(F3,text='Send',command=SendMessage)
B1.pack(ipadx=25,ipady=30)

E1.bind('<Return>',SendMessage)

username = StringVar()

global getname
getname = ''


################CUSTOM DIALOG##################

def GUI2Dialog():
	global v_roomnumber
	global GUI2
	GUI2 = Toplevel()
	GUI2.attributes('-topmost',True)
	w = 320
	h = 350

	ws = GUI2.winfo_screenwidth() #screen width
	hs = GUI2.winfo_screenheight() #screen height
	

	x = (ws/2) - (w/2)
	y = (hs/2) - (h/2)

	GUI2.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')

	v_getname = StringVar()
	L = ttk.Label(GUI2, text='Name',font=FONT2).pack()
	EN1 = ttk.Entry(GUI2,textvariable=v_getname,font=('Angsana New',25),width=40)
	EN1.pack(padx=30,pady=00)

	v_roomnumber = StringVar()
	L = ttk.Label(GUI2, text='Room Number',font=FONT2).pack()
	EN2 = ttk.Entry(GUI2,textvariable=v_roomnumber,font=('Angsana New',25),width=40)
	EN2.pack(padx=30,pady=00)

	v_roomnumber.set('10001')

	def EnterName(event=None):
		global getname
		getname = v_getname.get()
		roomnumber.set(v_roomnumber.get())
		GUI2.withdraw()
		GUI.attributes('-topmost',True)
		E1.focus()
		GUI.attributes('-topmost',False)

		import random

		print('GETNAME',getname)
		if getname == '' or getname == None:
			num = random.randint(10000,99999)
			getname = str(num)

		username.set(getname)
		chatbox.insert(INSERT,'สวัสดี ' + getname)


		###########RUN SERVER#############
		global client
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

		try:
			client.connect((SERVERIP,PORT))
			firsttext = 'JOIN|{}|{}'.format(roomnumber.get(),username.get()) # + username.get()
			client.send(firsttext.encode('utf-8'))
			task = threading.Thread(target=server_handler, args=(client,))
			task.start()
		except:
			print('ERROR!')
			messagebox.showerror('Connection Failed','ไม่สามารถเชื่อมต่อกับ server ได้')

	BLINE = Frame(GUI2)
	BLINE.pack()

	BB2 = ttk.Button(BLINE,text='Enter Chatroom',command=EnterName)
	BB2.grid(row=0,column=0,ipady=10,ipadx=20,pady=20,padx=10)
	EN1.bind('<Return>',lambda x: EN2.focus())
	EN2.bind('<Return>',EnterName)


	def NewRoom():

		global client
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

		try:
			client.connect((SERVERIP,PORT))
			firsttext = 'ROOM|NEW'
			client.send(firsttext.encode('utf-8'))
			task = threading.Thread(target=server_checkroom, args=(client,))
			task.start()
		except:
			print('ERROR!')
			messagebox.showerror('Connection Failed','ไม่สามารถเชื่อมต่อกับ server ได้')



	BB3 = ttk.Button(BLINE,text='New Room',command=NewRoom)
	BB3.grid(row=0,column=1,ipady=10,ipadx=20,pady=20,padx=10)

	


	def CheckClose():
		GUI2.attributes('-topmost',False)
		checkenter = messagebox.askyesno('ยกเลิกการใช้งานโปรแกรม','หากไม่กรอกชื่อจะไม่สามารถใช้งานโปรแกรมได้\nคุณต้องการยกเลิกใช่หรือไม่?')
		print('CHECK: ',checkenter)
		if checkenter == True:
			GUI2.destroy()
		else:
			GUI2.attributes('-topmost',True)

	EN1.focus()
	GUI2.protocol('WM_DELETE_WINDOW', CheckClose)  # root is your root window
	GUI2.mainloop()



def CheckCloseMain():
	GUI.attributes('-topmost',False)
	checkenter = messagebox.askyesno('ยืนยันการปิดโปรแกรม','คุณต้องการออกจากโปรแกรมใช่หรือไม่?')
	#print('CHECK: ',checkenter)
	if checkenter == True:
		GUI.destroy()
	else:
		GUI.attributes('-topmost',True)

GUI.protocol('WM_DELETE_WINDOW', CheckCloseMain)
GUI2Dialog()

print('Uncle Chat (V.0.0.1) Starting...')

GUI.mainloop()


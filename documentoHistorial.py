from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class DocumentoAccion(object):

	def __init__(self,oficina,usuario):
		self.oficina=oficina
		self.usuario=usuario
	def Top_Menu(self,frame,width,height):
		letra=('Comic Sans MS',24,'bold')
		frame_left=Frame(frame,width=int(width*0.15),height=int(height*0.93),bg='#181F50')		
		frame_left.pack(side='left')
		Lista_Menu=Listbox(frame_left,width=int(width*0.1),height=int(height*0.059))
		items=('MENU1','MENU2','MENU3')
		Lista_Menu.insert(0,*items)
		Lista_Menu.place(x=0,y=0)
		

		frame_main=Frame(frame,width=int(width*0.83),height=int(height*0.93),bg='#C2C2C1')
		frame_main.pack(side='right',padx=int(width*0.009))
		label=Label(frame_main,text='EN DESARROLLO...')
		label.place(x=5,y=200)

	
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class DocumentoAccion(object):

	def __init__(self,oficina,usuario):
		self.oficina=oficina
		self.usuario=usuario
	def Top_Menu(self,frame,width,height):
		frame_left=Frame(frame,width=int(width*0.15),height=int(height*0.93),bg='#181F50')
		frame_left.pack(side='left')

		frame_main=Frame(frame,width=int(width*0.83),height=int(height*0.93),bg='#C2C2C1')
		frame_main.pack(side='right',padx=int(width*0.009))

	
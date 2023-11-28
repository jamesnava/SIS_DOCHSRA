import ttkbootstrap as ttk
from tkinter import *
class Usuario():
	def __init__(self):
		pass
	def Top_Perfiles(self):
		self.TopPerfil=Toplevel()
		self.TopPerfil.geometry('400x500')
		self.TopPerfil.title("Crear Perfil")
		self.TopPerfil.grab_set()
		self.TopPerfil.resizable(0,0)
		self.table_Documentos=ttk.Treeview(self.TopPerfil,height=5,columns=('#1','#2','3'),show='headings',style='info.Treeview')
		self.table_Documentos.heading("#1",text="DNI")
		self.table_Documentos.column("#1",width=50,anchor="w",stretch='NO')
		self.table_Documentos.heading("#2",text="USUARIO")
		self.table_Documentos.column("#2",width=100,anchor="w",stretch='NO')
		self.table_Documentos.heading("#3",text="ESTADO")
		self.table_Documentos.column("#3",width=100,anchor="w",stretch='NO')		
		self.table_Documentos.grid(row=1,column=0,columnspan=4,padx=10,sticky='e')



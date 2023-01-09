from tkinter import *
import datetime
from tkinter import ttk
from tkinter import messagebox
import GUI_User


class Ventana_Principal(object):
	"""docstring for Ventana_Principal"""
	def __init__(self,usuario):
	
		self.letra_leyenda=('Candara',16,'bold italic')		
	
		self.ventana=Tk()
		self.ventana.title('Sistema de citas de Consultorio Externo')
		 
		self.ventana.iconbitmap('image/doctor.ico')		
		self.height=int(self.ventana.winfo_screenheight()*0.9)
		self.width=int(self.ventana.winfo_screenwidth()*0.9)		
		self.ventana.geometry("%dx%d" % (self.width,self.height)+"+0+0")
		self.ventana.resizable(0,0)
		#frame principal
		self.Frame_Principal=Frame(self.ventana,bg='#828682',width=self.width,height=self.height)
		self.Frame_Principal.pack()
		#agregando menu
		self.Barra_Menu=Menu(self.ventana)
		self.ventana['menu']=self.Barra_Menu
		#creando menu configuracion
		self.M_Configuracion=Menu(self.Barra_Menu,tearoff=False)
		self.M_Configuracion.add_command(label='Minimizar',command=self.ventana.iconify)
		self.M_Configuracion.add_command(label='Cerrar',command=self.ventana.destroy)
		self.M_Configuracion.add_separator()		
		self.Barra_Menu.add_cascade(label='Archivo',menu=self.M_Configuracion)

		# creando menu Acciones
		self.M_Acciones=Menu(self.Barra_Menu,tearoff=False)
		self.M_Acciones.add_command(label='Generar Documento')
		self.M_Acciones.add_command(label='Bandeja de Entrada')
		self.M_Acciones.add_separator()		
		self.Barra_Menu.add_cascade(label='Documentos',menu=self.M_Acciones)

		
	

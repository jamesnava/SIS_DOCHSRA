from tkinter import *
import datetime
from tkinter import ttk
from tkinter import messagebox
import GUI_User
import documentos
import Consulta_doc


class Ventana_Principal(object):
	"""docstring for Ventana_Principal"""
	def __init__(self,usuario):
		self.usuario=usuario
		self.letra_leyenda=('Candara',16,'bold italic')		
	
		self.ventana=Tk()
		self.ventana.title('Seguimiento Documentario')
		 
		self.ventana.iconbitmap('image/doctor.ico')		
		self.height=int(self.ventana.winfo_screenheight()*0.9)
		self.width=int(self.ventana.winfo_screenwidth()*0.9)		
		self.ventana.geometry("%dx%d" % (self.width,self.height)+"+0+0")
		self.ventana.resizable(0,0)
		#frame principal
		self.Frame_Principal=Frame(self.ventana,bg='#647B7B',width=self.width,height=int(self.height*0.96))
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
		self.M_Acciones.add_command(label='Generar Documento',command=self.M_GenerarDocumento)
		self.M_Acciones.add_command(label='Bandeja de Entrada',command=self.bandeja_Entrada)
		self.M_Acciones.add_command(label='Seguimiento')
		self.M_Acciones.add_separator()		
		self.Barra_Menu.add_cascade(label='Documentos',menu=self.M_Acciones)

		#Creando oficinas

		self.M_Oficina=Menu(self.Barra_Menu,tearoff=False)
		self.M_Oficina.add_command(label='Agregar Nueva Oficina')		
		self.M_Oficina.add_separator()		
		self.Barra_Menu.add_cascade(label='Oficina',menu=self.M_Oficina)

		#Pefil de Usuariio
		self.M_Usuario=Menu(self.Barra_Menu,tearoff=False)
		self.M_Usuario.add_command(label='Agregar Nuevo Usuario')		
		self.M_Usuario.add_separator()		
		self.Barra_Menu.add_cascade(label='Perfil de Usuario',menu=self.M_Usuario)
		self.agregar_bottom()

	def Return_Office(self):
		obj_consulta=Consulta_doc.querys()
		rows=obj_consulta.query_OficinaMUser(self.usuario)
		return rows[0].Id_Oficina,rows[0].dni

	def agregar_bottom(self):		
		self.Frame_Bottom=Frame(self.ventana,bg='#647B7B',width=self.width,height=int(self.height*0.03))
		self.Frame_Bottom.pack(side='bottom')
		etiqueta_usuario=Label(self.Frame_Bottom,text='Usuario: ')
		etiqueta_usuario.grid(row=0,column=0)
		etiqueta_UsuarioValor=Label(self.Frame_Bottom,text=self.usuario)
		etiqueta_UsuarioValor.grid(row=0,column=1)

	def M_GenerarDocumento(self):
		#647B7B
		self.Frame_Documentos=Frame(self.ventana,bg='#647B7B',width=int(self.width*0.99),height=int(self.height*0.93),highlightthickness=5)
		self.Frame_Documentos.place(x=10,y=10)
		self.Frame_Documentos.grid_propagate(False)
		obj_Documentos=documentos.Documentos()
		obj_Documentos.Generar_Documentos(self.Frame_Documentos,self.width,self.height,self.usuario)

	def bandeja_Entrada(self):
		oficina,usuario=self.Return_Office()
		self.Frame_Bandeja=Frame(self.ventana,bg='#647B7B',width=int(self.width*0.99),height=int(self.height*0.93),highlightthickness=5)
		self.Frame_Bandeja.place(x=10,y=10)
		self.Frame_Bandeja.grid_propagate(False)
		obj_Documentos=documentos.Bandeja(oficina,usuario)
		obj_Documentos.BandejaEntrada(self.Frame_Bandeja,self.width,self.height)


		
	
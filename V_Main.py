from tkinter import *
import datetime
from tkinter import ttk
from tkinter import messagebox
import GUI_User
import documentos
import Consulta_doc
import documentoHistorial
import datetime
import time


class Ventana_Principal(object):
	"""docstring for Ventana_Principal"""
	def __init__(self,usuario):
		self.hora=datetime.datetime.now()
		self.usuario=usuario
		self.letra_leyenda=('Candara',16,'bold italic')		
	
		self.ventana=Tk()
		self.ventana.title('Seguimiento Documentario')
		 
		self.ventana.iconbitmap('image/libro.ico')		
		self.height=int(self.ventana.winfo_screenheight()*0.92)
		self.width=int(self.ventana.winfo_screenwidth()*0.9)		
		self.ventana.geometry("%dx%d" % (self.width,self.height)+"+0+0")
		self.ventana.resizable(0,0)
		#frame principal
		self.Frame_Principal=Frame(self.ventana,bg='#647B7B',width=self.width,height=int(self.height*0.95))
		self.Frame_Principal.pack()
		#agregando menu
		self.Barra_Menu=Menu(self.ventana)
		self.ventana['menu']=self.Barra_Menu
		#creando menu configuracion
		self.M_Configuracion=Menu(self.Barra_Menu,tearoff=False)
		self.M_Configuracion.add_command(label='Restablecer Contraseña',command=self.Cambiar_Contrasenia)
		self.M_Configuracion.add_command(label='Minimizar',command=self.ventana.iconify)
		self.M_Configuracion.add_command(label='Cerrar',command=self.ventana.destroy)
		self.M_Configuracion.add_separator()		
		self.Barra_Menu.add_cascade(label='Archivo',menu=self.M_Configuracion)

		# creando menu Acciones
		self.M_Acciones=Menu(self.Barra_Menu,tearoff=False)
		self.M_Acciones.add_command(label='Generar Documento',command=self.M_GenerarDocumento)
		self.M_Acciones.add_command(label='Bandeja de Entrada',command=self.bandeja_Entrada)				
		self.M_Acciones.add_command(label='Seguimiento',command=self.Seguimiento_Documentario)
		self.M_Acciones.add_command(label='Historial de Documentos',command=self.Historial_Documentario)
		#self.M_Acciones.add_command(label='Imprimir Hoja de Tramite')
		self.M_Acciones.add_separator()		
		self.Barra_Menu.add_cascade(label='Documentos',menu=self.M_Acciones)
				
		#Ayuda...
		self.M_Ayuda=Menu(self.Barra_Menu,tearoff=False)
		self.M_Ayuda.add_command(label='Acerca de...',command=self.acercade)
		self.M_Ayuda.add_command(label='Desarrollado por...', command=self.autor)		
		self.M_Ayuda.add_separator()		
		self.Barra_Menu.add_cascade(label='Ayuda',menu=self.M_Ayuda)
		self.agregar_bottom()

	def Return_Office(self):
		obj_consulta=Consulta_doc.querys()
		rows=obj_consulta.query_OficinaMUser(self.usuario)
		return rows[0].Id_Oficina,rows[0].dni

	def agregar_bottom(self):		
		self.Frame_Bottom=Frame(self.ventana,bg='#647B7B',width=self.width,height=int(self.height*0.05))
		self.Frame_Bottom.pack(side='bottom')
		etiqueta_usuario=Label(self.Frame_Bottom,text='Usuario: ',font=('Candara',11,'bold italic')	)
		etiqueta_usuario.grid(row=0,column=0)
		etiqueta_UsuarioValor=Label(self.Frame_Bottom,text=self.usuario,font=('Candara',11,'bold italic'))
		etiqueta_UsuarioValor.grid(row=0,column=1)		

	def M_GenerarDocumento(self):
		oficina,usuario=self.Return_Office()
		#647B7B
		self.Frame_Documentos=Frame(self.ventana,bg='#647B7B',width=int(self.width*0.99),height=int(self.height*0.93),highlightthickness=5)
		self.Frame_Documentos.place(x=10,y=10)
		self.Frame_Documentos.grid_propagate(False)
		obj_Documentos=documentos.Documentos(oficina,usuario)
		obj_Documentos.Generar_Documentos(self.Frame_Documentos,self.width,self.height,self.usuario)

	def bandeja_Entrada(self):
		oficina,usuario=self.Return_Office()
		self.Frame_Bandeja=Frame(self.ventana,bg='#647B7B',width=int(self.width*0.99),height=int(self.height*0.93),highlightthickness=5)
		self.Frame_Bandeja.place(x=10,y=10)
		self.Frame_Bandeja.grid_propagate(False)
		obj_Documentos=documentos.Bandeja(oficina,usuario,self.ventana)
		obj_Documentos.BandejaEntrada(self.Frame_Bandeja,self.width,self.height)

	def Seguimiento_Documentario(self):
		oficina,usuario=self.Return_Office()
		self.Frame_Bandeja=Frame(self.ventana,bg='#647B7B',width=int(self.width*0.99),height=int(self.height*0.93),highlightthickness=5)
		self.Frame_Bandeja.place(x=10,y=10)
		self.Frame_Bandeja.grid_propagate(False)
		obj_Documentos=documentos.Seguimiento(oficina,usuario)
		obj_Documentos.Seguimiento(self.Frame_Bandeja,self.width,self.height)

	def Historial_Documentario(self):
		oficina,usuario=self.Return_Office()
		self.Frame_Historial=Frame(self.ventana,bg='#647B7B',width=int(self.width*0.99),height=int(self.height*0.93),highlightthickness=0)
		self.Frame_Historial.place(x=10,y=10)
		self.Frame_Historial.grid_propagate(False)
		obj_HistorialDoc=documentoHistorial.DocumentoAccion(oficina,usuario)
		obj_HistorialDoc.Top_Menu(self.Frame_Historial,self.width,self.height)

	def Cambiar_Contrasenia(self):

		Top_Contrasenia=Toplevel(self.ventana)
		Top_Contrasenia.iconbitmap('image/pass.ico')	
		Top_Contrasenia.geometry('400x200')
		Top_Contrasenia.resizable(0,0)
		Top_Contrasenia.grab_set()
		Top_Contrasenia.title("Cambiar Contraseña")
		etiqueta=Label(Top_Contrasenia,text='Contraseña Actual')
		etiqueta.grid(row=1,column=1,pady=10,padx=10)
		text_contraActual=Entry(Top_Contrasenia,show='*')
		text_contraActual.grid(row=1,column=2,pady=10,padx=10)
		etiqueta=Label(Top_Contrasenia,text='Contraseña Nueva')
		etiqueta.grid(row=2,column=1,pady=10,padx=10)
		text_contraNueva=Entry(Top_Contrasenia,show='*')
		text_contraNueva.grid(row=2,column=2,pady=10,padx=10)

		btn_AceptarC=Button(Top_Contrasenia,text='Aceptar')
		btn_AceptarC['command']=lambda :self.UpdatePass(self.usuario,text_contraActual.get(),text_contraNueva.get(),Top_Contrasenia)
		btn_AceptarC.grid(row=3,column=1,pady=10,padx=10)

		btn_CancelarC=Button(Top_Contrasenia,text='Cancelar')
		btn_CancelarC['command']=Top_Contrasenia.destroy
		btn_CancelarC.grid(row=3,column=2,pady=10,padx=10)
	def UpdatePass(self,usuario,contraA,contraN,Top_Contrasenia):
		obj_querys=Consulta_doc.querys()

		try:			
			rows=obj_querys.query_RetornaCodigo('USUARIO',contraA,'Contrasenia','Contrasenia')
			if len(rows)!=0:
				obj_querys.Update_Pass(usuario,contraA,contraN)
				messagebox.showinfo('Alerta','Se cambio correctamente!')
				Top_Contrasenia.destroy()
				self.ventana.destroy()
			else:
				messagebox.showinfo('Alerta','La contraseña Actual no Corresponde')
		except Exception as e:
			messagebox.showerror('Error',e)

	def acercade(self):
		messagebox.showinfo('informacion del software',"""Sistema de seguimiento documentario, version 1.1""")
	def autor(sel):
		messagebox.showinfo('Desarrollado por',"""El sistema de seguimiento documentario fue desarrollado por la\nUNIDAD DE ESTADISTICA E INFORMATICA a través de la oficina de\nDESARROLLO DE SOFTWARE del Hospital Sub Regional de Andahuaylas\nTodos los derechos reservado ®2023\nby JAIME NAVARRO CRUZ- navarrocruzjaime@gmail.com""")






		
	
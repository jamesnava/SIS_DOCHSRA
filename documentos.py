from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import generales
import Consulta_doc
from datetime import datetime
class Documentos():
	def __init__(self):
		self.fecha_Actual=datetime.now()
		self.obj_consultas=Consulta_doc.querys()	
	def Generar_Documentos(self,frame,width,height):
		letra=('Comic Sans MS',12,'bold')

		etiqueta=Label(frame,text='Codigo: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=0,column=1,pady=8,padx=5,sticky='e')
		self.Entry_Codigo=Entry(frame,width=40)
		self.Entry_Codigo.insert('end',self.Generar_CodigoValido('PEDIDO','cod_Pedido'))
		self.Entry_Codigo['state']='readonly'
		self.Entry_Codigo.grid(row=0,column=2,ipady=3)

		etiqueta=Label(frame,text='Nro Pedido: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=0,column=3,pady=8,padx=5,sticky='e')
		self.Entry_NroPedido=Entry(frame,width=40)
		self.Entry_NroPedido.grid(row=0,column=4,ipady=3)

		etiqueta=Label(frame,text='Descripcion: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=2,column=1,pady=8,padx=5,sticky='e')
		self.Text_Descripcion=Text(frame,width=50,height=6)
		self.Text_Descripcion.grid(row=2,column=2,columnspan=4,sticky='w')

		etiqueta=Label(frame,text='Tipo: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=3,column=1,pady=8,padx=5,sticky='e')
		self.listTipo=ttk.Combobox(frame,values=['SERVICIO','BIEN'],width=35)
		self.listTipo.current(1)
		self.listTipo.grid(row=3,column=2,ipady=3)

		etiqueta=Label(frame,text='Fecha: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=3,column=3,pady=8,padx=5,sticky='e')
		self.Entry_Fecha=Entry(frame,width=40)
		self.Entry_Fecha.insert('end',self.fecha_Actual.strftime("%d-%m-%Y"))
		self.Entry_Fecha.config(state='readonly')
		self.Entry_Fecha.grid(row=3,column=4,ipady=3)

		etiqueta=Label(frame,text='Derivar: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=5,column=1,pady=8,padx=5,sticky='e')
		self.Lista_Oficinas=ttk.Combobox(frame,width=35)
		self.Lista_Oficinas.grid(row=5,column=2,ipady=3)
		self.llenar_Listaoficina()
	
		etiqueta=Label(frame,text='Generado Por: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=5,column=3,pady=8,padx=5,sticky='e')
		self.Entry_Usuario=Entry(frame,width=40)
		self.Entry_Usuario.grid(row=5,column=4,ipady=3)

		btn_Aceptar=Button(frame,text='Aceptar',width=20)
		btn_Aceptar.grid(row=6,column=1,columnspan=2,padx=10,pady=10,sticky='e')

		btn_Aceptar=Button(frame,text='Cancelar',width=20)
		btn_Aceptar.grid(row=6,column=3,columnspan=2,pady=10,padx=10,sticky='e')

	def Generar_CodigoValido(self,tabla,columna):
					
		while True:
			codigo=generales.Generar_Codigo()
			rows=self.obj_consultas.query_ExistenciaCodigo(tabla,codigo,columna)			
			if len(rows)==0:
				break

		return codigo
	def llenar_Listaoficina(self):
		rows=self.obj_consultas.query_tablas('OFICINA')
		ofcinas=[]
		if len(rows)!=0:
			oficinas=[valor.Oficina for valor in rows]
		self.Lista_Oficinas.config(values=oficinas)
		self.Lista_Oficinas.current(0)


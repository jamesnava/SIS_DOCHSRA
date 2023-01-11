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
	def Generar_Documentos(self,frame,width,height,Usuario):
		letra=('Comic Sans MS',12,'bold')
		self.width=width
		self.height=height
		self.Frame_Docs=Frame(frame,bg='#647B7B',width=int(width*0.6),height=int(height*0.6))
		self.Frame_Docs.place(x=int(self.width*0.5)-int((self.width*0.6)/2),y=int(self.height*0.08))
		self.Frame_Docs.grid_propagate(False)

		etiqueta=Label(self.Frame_Docs,text='Codigo: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=0,column=1,pady=8,padx=5,sticky='e')
		self.Entry_Codigo=Entry(self.Frame_Docs,width=40)
		self.Entry_Codigo.insert('end',self.Generar_CodigoValido('PEDIDO','cod_Pedido'))
		self.Entry_Codigo['state']='readonly'
		self.Entry_Codigo.grid(row=0,column=2,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Nro Doc: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=0,column=3,pady=8,padx=5,sticky='e')
		self.Entry_NroPedido=Entry(self.Frame_Docs,width=40)
		self.Entry_NroPedido.bind("<KeyRelease>",lambda event,campo=self.Entry_NroPedido:generales.validar_numero(event,campo))
		self.Entry_NroPedido.grid(row=0,column=4,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Descripcion: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=2,column=1,pady=8,padx=5,sticky='e')
		self.Text_Descripcion=Text(self.Frame_Docs,width=50,height=6)
		self.Text_Descripcion.grid(row=2,column=2,columnspan=4,sticky='w')

		etiqueta=Label(self.Frame_Docs,text='Tipo: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=3,column=1,pady=8,padx=5,sticky='e')
		self.listTipo=ttk.Combobox(self.Frame_Docs,values=['SERVICIO','BIEN','DOCUMENTO'],width=35)
		self.listTipo.current(1)
		self.listTipo.grid(row=3,column=2,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Fecha: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=3,column=3,pady=8,padx=5,sticky='e')
		self.Entry_Fecha=Entry(self.Frame_Docs,width=40)
		self.Entry_Fecha.insert('end',self.fecha_Actual.strftime("%d-%m-%Y"))
		self.Entry_Fecha.config(state='readonly')
		self.Entry_Fecha.grid(row=3,column=4,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Derivar: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=5,column=1,pady=8,padx=5,sticky='e')
		self.Lista_Oficinas=ttk.Combobox(self.Frame_Docs,width=35)
		self.Lista_Oficinas.grid(row=5,column=2,ipady=3)
		self.llenar_Listaoficina()
	
		etiqueta=Label(self.Frame_Docs,text='Generado Por: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=5,column=3,pady=8,padx=5,sticky='e')
		self.Entry_Usuario=Entry(self.Frame_Docs,width=40)
		self.Entry_Usuario.insert('end',Usuario)
		self.Entry_Usuario['state']='readonly'
		self.Entry_Usuario.grid(row=5,column=4,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Año: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=6,column=1,pady=8,padx=5,sticky='e')
		self.Entry_Anio=Entry(self.Frame_Docs,width=40)
		self.Entry_Anio.insert('end',self.fecha_Actual.strftime("%Y"))
		self.Entry_Anio['state']='readonly'
		self.Entry_Anio.grid(row=6,column=2,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Oficina: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=6,column=3,pady=8,padx=5,sticky='e')
		self.Entry_OficinaG=Entry(self.Frame_Docs,width=40)
		self.Entry_OficinaG.insert('end',self.Recuperar_OficinaGeneradora(Usuario))

		self.Entry_OficinaG['state']='readonly'
		self.Entry_OficinaG.grid(row=6,column=4,ipady=3)

		btn_Aceptar=Button(self.Frame_Docs,text='Aceptar',width=20)
		btn_Aceptar['command']=self.Insertar_Pedido
		btn_Aceptar.grid(row=7,column=1,columnspan=2,padx=10,pady=10,sticky='e')

		btn_Cancelar=Button(self.Frame_Docs,text='Cancelar',width=20)
		btn_Cancelar['command']=self.Capa
		btn_Cancelar.grid(row=7,column=3,columnspan=2,pady=10,padx=10,sticky='e')

	def Recuperar_OficinaGeneradora(self,usuario):
		row=self.obj_consultas.query_OficinaMUser(usuario)
		return row[0].Id_Oficina+':'+row[0].Oficina

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

	def Insertar_Pedido(self):
		
		#generando la lista
		datos=[]

		self.Entry_Codigo['state']='normal'
		codigo_Pedido=self.Entry_Codigo.get()
		datos.append(codigo_Pedido)

		nroPedido=self.Entry_NroPedido.get()		
		datos.append(nroPedido)

		descripcion=self.Text_Descripcion.get('1.0','end-1c')
		datos.append(descripcion)

		tipo=self.listTipo.get()
		datos.append(tipo)

		fecha=self.fecha_Actual.strftime("%d-%m-%Y")
		datos.append(fecha)

		#oficina
		oficina_Derivar=self.Lista_Oficinas.get()		
		rows=self.obj_consultas.query_RetornaCodigo('OFICINA',oficina_Derivar,'Oficina','Id_Oficina')
		codigo_Oficina_Derivar=rows[0].Id_Oficina	
		#datos.append(codigo_Oficina)
		
		#Oficina generadora
		self.Entry_OficinaG['state']='normal'
		oficina_Generadora=self.Entry_OficinaG.get()[:5]
		datos.append(oficina_Generadora)
		# usuario creador
		self.Entry_Usuario['state']='normal'
		usuario=self.Entry_Usuario.get()
		rows_user=self.obj_consultas.query_RetornaCodigo('USUARIO',usuario,'Usuario','dni')
		codigo_Usuario=rows_user[0].dni
		datos.append(codigo_Usuario)

		#año del pedido
		self.Entry_Anio['state']='normal'
		anio=self.Entry_Anio.get()
		datos.append(anio)
		
		#reestriccion de pedido
		datosAccion=[codigo_Pedido,fecha,codigo_Usuario,'ninguna',2,codigo_Oficina_Derivar,0,anio]
		if tipo=='BIEN':
			condicion=[tipo,nroPedido,anio]
			columnasC=['Tipo','Nro_Pedido','anio']			
			rows_nroPedido=self.obj_consultas.consulta_2Condiciones('PEDIDO',condicion,columnasC)			
			if len(rows_nroPedido)==0:
				self.obj_consultas.query_InsertarPedido(datos)
				self.obj_consultas.Insert_Accion(datosAccion)
				messagebox.showinfo('Notificación','se registró correctamiento!!')
				self.Capa()					
			else:
				messagebox.showerror('Notificación','el numero de pedido ya fué registrada')
				self.Capa()			


		elif tipo=='SERVICIO':
			condicion=[tipo,nroPedido,anio]
			columnasC=['Tipo','Nro_Pedido','anio']
			rows_nroServicio=self.obj_consultas.consulta_2Condiciones('PEDIDO',condicion,columnasC)
			if len(rows_nroServicio)==0:				
				self.obj_consultas.query_InsertarPedido(datos)
				self.obj_consultas.Insert_Accion(datosAccion)
				messagebox.showinfo('Notificación','se registró correctamiento!!')
				self.Capa()
			else:
				messagebox.showerror('Notificación','el numero de Servicio ya fué registrada')
				self.Capa()

		else:
			condicion=[tipo,nroPedido,anio,codigo_Oficina_Derivar]
			columnasC=['Tipo','Nro_Pedido','anio','Oficina']
			rows_nroDocumento=self.obj_consultas.consulta_3Condiciones('PEDIDO',condicion,columnasC)
			if len(rows_nroDocumento)==0:
				self.obj_consultas.query_InsertarPedido(datos)
				self.obj_consultas.Insert_Accion(datosAccion)
				messagebox.showinfo('Notificación','se registró correctamiento!!')
				self.Capa()
			else:
				messagebox.showerror('Notificación','el numero de Documento ya fué registrada')
				self.Capa()

	def Capa(self):
		self.Frame_Capa=Frame(self.Frame_Docs,bg='#647B7B',width=int(self.width*0.6),height=int(self.height*0.6))
		self.Frame_Capa.place(x=0,y=0)
		self.Frame_Capa.grid_propagate(False)



class Bandeja():
	def __init__(self,oficina,dniUser):
		self.oficina=oficina
		self.dniUser=dniUser
		self.obj_consulta=Consulta_doc.querys()
	def BandejaEntrada(self,frame,width,height):
		letra=('Segoe Script',12,'bold')
		self.Frame_Docs=Frame(frame,bg='#647B7B',width=int(width*0.98),height=int(height*0.92))
		self.Frame_Docs.place(x=0,y=0)
		self.Frame_Docs.grid_propagate(False)
		etiqueta=Label(self.Frame_Docs,text='DOCUMENTOS POR RECEPCIONAR',width=int(width*0.1),font=letra)
		etiqueta.place(x=0,y=10)
		self.table_Recepcionar=ttk.Treeview(self.Frame_Docs,columns=('#1','#2','#3','#4','#5'),show='headings')				
		self.table_Recepcionar.heading("#1",text="CODIGO")
		self.table_Recepcionar.column("#1",width=60,anchor="w")
		self.table_Recepcionar.heading("#2",text="NRO DOC")
		self.table_Recepcionar.column("#2",width=50,anchor="w")
		self.table_Recepcionar.heading("#3",text="DESCRIPCION")
		self.table_Recepcionar.column("#3",width=400,anchor="w")
		self.table_Recepcionar.heading("#4",text="TIPO")
		self.table_Recepcionar.column("#4",width=100,anchor="w")
		self.table_Recepcionar.heading("#5",text="REMITENTE")
		self.table_Recepcionar.column("#5",width=200,anchor="w")
		self.table_Recepcionar.place(x=int(width*0.03),y=60,width=int(width*0.7),height=220)
		self.llenar_TablaRecepcionar()
		btn_AccionR=Button(self.Frame_Docs,text="Accion")
		btn_AccionR['command']=self.Top_Accion
		btn_AccionR.place(x=int(width*0.3),y=300)



		etiqueta=Label(self.Frame_Docs,text='DOCUMENTOS POR ATENDER',width=int(width*0.1),font=letra)
		etiqueta.place(x=0,y=int(height*0.5))

		self.table_Derivar=ttk.Treeview(self.Frame_Docs,columns=('#1','#2','#3','#4'),show='headings')				
		self.table_Derivar.heading("#1",text="NRO DOC")
		self.table_Derivar.column("#1",width=60,anchor="w")
		self.table_Derivar.heading("#2",text="DESCRIPCION")
		self.table_Derivar.column("#2",width=320,anchor="w")
		self.table_Derivar.heading("#3",text="TIPO")
		self.table_Derivar.column("#3",width=100,anchor="w")
		self.table_Derivar.heading("#4",text="REMITENTE")
		self.table_Derivar.column("#4",width=320,anchor="w")
		self.table_Derivar.place(x=int(width*0.03),y=int(height*0.55),width=int(width*0.6),height=220)

		btn_AccionD=Button(self.Frame_Docs,text="Accion")
		btn_AccionD.place(x=int(width*0.3),y=int(height*0.8))

	def llenar_TablaRecepcionar(self):
		rows=self.obj_consulta.query_Recepcionar(self.oficina)		
		for valor in rows:
			self.table_Recepcionar.insert('','end',values=(valor.Cod_Pedido,valor.Nro_Pedido,valor.Descripcion,valor.Tipo,valor.Oficina))

	def Top_Accion(self):
		self.TopAccion=Toplevel()
		self.TopAccion.geometry('400x400')
		self.TopAccion.title('Realizar Accion')
		self.TopAccion.grab_set()




		






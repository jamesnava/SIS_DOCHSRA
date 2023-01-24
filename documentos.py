from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import generales
import Consulta_doc
from datetime import datetime
from PIL import Image
import pdf
import os
class Documentos():
	def __init__(self,oficina,usuario):
		self.oficinaG=oficina
		self.usuarioG=usuario
		self.fecha_Actual=datetime.now()
		self.obj_consultas=Consulta_doc.querys()	
	def Generar_Documentos(self,frame,width,height,Usuario):
		letra=('Comic Sans MS',12,'bold')
		self.width=width
		self.height=height
		#647B7B
		self.Frame_Docs=Frame(frame,bg='#647B7B',width=int(width*0.6),height=int(height*0.71))
		self.Frame_Docs.place(x=int(self.width*0.5)-int((self.width*0.6)/2),y=int(self.height*0.08))
		self.Frame_Docs.grid_propagate(False)

		etiqueta=Label(self.Frame_Docs,text='Codigo: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=0,column=1,pady=8,padx=5,sticky='e')
		self.Entry_Codigo=Entry(self.Frame_Docs,width=40)
		self.Entry_Codigo.insert('end',self.Generar_CodigoValido('PEDIDO','cod_Pedido'))
		self.Entry_Codigo['state']='readonly'
		self.Entry_Codigo.grid(row=0,column=2,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Numeracion: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=0,column=3,pady=8,padx=5,sticky='e')
		self.Entry_NroPedido=Entry(self.Frame_Docs,width=40)
		#self.Entry_NroPedido.bind("<KeyRelease>",lambda event,campo=self.Entry_NroPedido:generales.validar_numero(event,campo))
		self.Entry_NroPedido.grid(row=0,column=4,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Razon Social: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=1,column=1,pady=8,padx=5,sticky='e')
		self.Entry_Razon=Entry(self.Frame_Docs,width=40)		
		self.Entry_Razon.grid(row=1,column=2,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Asunto: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=1,column=3,pady=8,padx=5,sticky='e')
		self.Entry_Asunto=Entry(self.Frame_Docs,width=40)
		self.Entry_Asunto.grid(row=1,column=4,ipady=3)


		etiqueta=Label(self.Frame_Docs,text='Descripcion: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=2,column=1,pady=8,padx=5,sticky='e')
		self.Text_Descripcion=Text(self.Frame_Docs,width=60,height=6)
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

		btn_Aceptar=ttk.Button(self.Frame_Docs,text='Aceptar',width=20,cursor="hand2")
		btn_Aceptar['command']=self.Insertar_Pedido
		btn_Aceptar.grid(row=7,column=1,columnspan=2,padx=10,pady=10,sticky='e')

		btn_Cancelar=ttk.Button(self.Frame_Docs,text='Cancelar',width=20,cursor='hand2')
		btn_Cancelar['command']=self.Capa
		btn_Cancelar.grid(row=7,column=3,columnspan=2,pady=10,padx=10,sticky='e')

		################## AGREGANDO  LISTA DE PEDIDOS #######################
		s=ttk.Style()
		s.configure("model.Treeview",background="#1099B5")

		etiqueta=Label(self.Frame_Docs,text="LISTA DE DOCUMENTOS",bg='#647B7B',fg="#1B3A71",font=('Comic Sans MS',18,'bold'))
		etiqueta.grid(row=8,column=1,pady=5,columnspan=4)

		self.table_Documentos=ttk.Treeview(self.Frame_Docs,columns=('#1','#2','#3','#4','#5'),show='headings',style="model.Treeview")
		self.table_Documentos.heading("#1",text="Nro")
		self.table_Documentos.column("#1",width=20,anchor="w")
		self.table_Documentos.heading("#2",text="CODIGO")
		self.table_Documentos.column("#2",width=80,anchor="w")
		self.table_Documentos.heading("#3",text="NRO DOC")
		self.table_Documentos.column("#3",width=200,anchor="w")
		self.table_Documentos.heading("#4",text="Descripcion")
		self.table_Documentos.column("#4",width=350,anchor="w")
		self.table_Documentos.heading("#5",text="Derivado a")
		self.table_Documentos.column("#5",width=200,anchor="w")	
		self.table_Documentos.grid(row=9,column=1,columnspan=4,rowspan=2,pady=5)
		self.llenar_tableDocumentos()

		

		btn_UpDoc=ttk.Button(self.Frame_Docs,text='Eliminar',width=20,cursor="hand2")
		btn_UpDoc['command']=self.eliminar_Documento
		btn_UpDoc.grid(row=11,column=2,padx=10,pady=5,sticky='e')

		image=PhotoImage(file='image/impre.png')
		#image= image.resize(40,40)
		self.etiqueta_print=ttk.Button(self.Frame_Docs,text='Imprimir Exp.',width=20,cursor='hand2')		
		self.etiqueta_print.bind("<Button-1>",self.print_expediente)
		self.etiqueta_print.grid(row=11,column=3)
		
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
	def llenar_tableDocumentos(self):
		self.delete_table(self.table_Documentos)
		rows=self.obj_consultas.documentos_EmitidosUpdate(2,0,self.oficinaG)
		for valor in rows:
			self.table_Documentos.insert('','end',values=(valor.Id_Accion,valor.Cod_Pedido,valor.Nro_Pedido,valor.Descripcion,valor.Oficina))
	def eliminar_Documento(self):
		if self.table_Documentos.selection():
			codigo_Accion=self.table_Documentos.item(self.table_Documentos.selection()[0])['values'][0]
			codigo_pedido=self.table_Documentos.item(self.table_Documentos.selection()[0])['values'][1]
			try:
				self.obj_consultas.delete_itemINT('ACCION','Id_Accion',codigo_Accion)
				self.obj_consultas.delete_itemSTR('PEDIDO','cod_Pedido',codigo_pedido)
				self.llenar_tableDocumentos()
			except Exception as e:
				messagebox.showerror('Notificación',e)			

		else:
			messagebox.showinfo('Alerta','Seleccione un Item')
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

		fecha=self.fecha_Actual.strftime("%d-%m-%Y %H:%M")
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

		#falta numero de tramite
		num=0
		nroRow=self.obj_consultas.query_Max()		
		if nroRow[0].nro!=None:
			num=nroRow[0].nro+1
		else:
			num=1

		datos.append(num)
		#asunto
		razon=self.Entry_Razon.get()
		datos.append(razon)

		#Asunto
		asunto=self.Entry_Asunto.get()
		datos.append(asunto)

		#hora
		Hora=self.fecha_Actual.strftime("%H:%M")
		datos.append(Hora)
		
		#reestriccion de pedido
		datosAccion=[codigo_Pedido,fecha,codigo_Usuario,'ninguna',2,codigo_Oficina_Derivar,0,anio,oficina_Generadora]
		if codigo_Oficina_Derivar!=oficina_Generadora:
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
			self.llenar_tableDocumentos()
		else:
			messagebox.showerror('Error','No se puede derivar a la misma oficina')

	def Capa(self):
		self.Frame_Capa=Frame(self.Frame_Docs,bg='#647B7B',width=int(self.width*0.6),height=int(self.height*0.71))
		self.Frame_Capa.place(x=0,y=0)
		self.Frame_Capa.grid_propagate(False)

	def delete_table(self,table):
		for item in table.get_children():
			table.delete(item)

	def print_expediente(self,event):
		if self.table_Documentos.selection():			
			codigo=self.table_Documentos.item(self.table_Documentos.selection()[0])['values'][1]
			rows=self.obj_consultas.query_RetornaCodigo('PEDIDO',codigo,'cod_Pedido','Nro_Tramite')
			obj_pdf=pdf.PDF(rows[0].Nro_Tramite)
			if messagebox.askquestion('Atencion','Desea Imprimir el expediente'):
				os.startfile('Expediente.pdf','print')
				
		else:
			messagebox.showinfo('Atencion','Seleccione un ITEM!!')


class Bandeja():
	def __init__(self,oficina,dniUser,ventana):
		self.ventana=ventana
		self.fecha_Actual=datetime.now()
		self.oficina=oficina
		self.dniUser=dniUser
		self.obj_consulta=Consulta_doc.querys()
		self.letra1=('Comic Sans MS',12,'bold')
	def BandejaEntrada(self,frame,width,height):
		letra=('Segoe Script',12,'bold')
		self.Frame_Docs=Frame(frame,bg='#647B7B',width=int(width*0.98),height=int(height*0.92))
		self.Frame_Docs.place(x=0,y=0)
		self.Frame_Docs.grid_propagate(False)
		etiqueta=Label(self.Frame_Docs,text='DOCUMENTOS POR RECEPCIONAR',width=int(width*0.1),font=letra)
		etiqueta.place(x=0,y=10)
		self.table_Recepcionar=ttk.Treeview(self.Frame_Docs,columns=('#1','#2','#3','#4','#5'),show='headings')				
		self.table_Recepcionar.heading("#1",text="Nro")
		self.table_Recepcionar.column("#1",width=1,anchor="w")
		self.table_Recepcionar.heading("#2",text="CODIGO")
		self.table_Recepcionar.column("#2",width=60,anchor="w")
		self.table_Recepcionar.heading("#3",text="NRO DOC")
		self.table_Recepcionar.column("#3",width=50,anchor="w")
		self.table_Recepcionar.heading("#4",text="DESCRIPCION")
		self.table_Recepcionar.column("#4",width=400,anchor="w")
		self.table_Recepcionar.heading("#5",text="TIPO")
		self.table_Recepcionar.column("#5",width=100,anchor="w")
		
		self.table_Recepcionar.place(x=int(width*0.03),y=60,width=int(width*0.7),height=220)
		self.llenar_TablaRecepcionar()
		btn_AccionR=ttk.Button(self.Frame_Docs,text="Recepcionar",width=20,cursor='hand2')
		btn_AccionR['command']=self.Recepcionar
		btn_AccionR.place(x=int(width*0.3),y=300)



		etiqueta=Label(self.Frame_Docs,text='DOCUMENTOS POR ATENDER',width=int(width*0.1),font=letra)
		etiqueta.place(x=0,y=int(height*0.5))

		self.table_Derivar=ttk.Treeview(self.Frame_Docs,columns=('#1','#2','#3','#4','#5'),show='headings')				
		
		self.table_Derivar.heading("#1",text="Nro")
		self.table_Derivar.column("#1",width=10,anchor="w")
		self.table_Derivar.heading("#2",text="CODIGO")
		self.table_Derivar.column("#2",width=60,anchor="w")
		self.table_Derivar.heading("#3",text="NRO DOC")
		self.table_Derivar.column("#3",width=60,anchor="w")
		self.table_Derivar.heading("#4",text="DESCRIPCION")
		self.table_Derivar.column("#4",width=320,anchor="w")
		self.table_Derivar.heading("#5",text="TIPO")
		self.table_Derivar.column("#5",width=100,anchor="w")		
		self.table_Derivar.place(x=int(width*0.03),y=int(height*0.55),width=int(width*0.7),height=220)
		self.llenar_TablaDerivar()

		btn_AccionD=ttk.Button(self.Frame_Docs,text="Atender",width=20,cursor='hand2')
		btn_AccionD['command']=self.Top_Atencion
		btn_AccionD.place(x=int(width*0.3),y=int(height*0.8))

		image=PhotoImage(file='image/impre.png')
		self.etiqueta_print=Label(self.Frame_Docs,image=image,bg='#647B7B',cursor='hand2')
		self.etiqueta_print.image=image
		self.etiqueta_print.bind("<Button-1>",self.print_expediente)
		self.etiqueta_print.place(x=int(width*0.94),y=int(height*0.54))

	def llenar_TablaRecepcionar(self):
		rows=self.obj_consulta.query_DocXEstado(self.oficina,2)		
		for valor in rows:			
			self.table_Recepcionar.insert('','end',values=(valor.Id_Accion,valor.Cod_Pedido,valor.Nro_Pedido,valor.Descripcion,valor.Tipo))


	def llenar_TablaDerivar(self):
		self.delete_table(self.table_Derivar)
		rows=self.obj_consulta.query_DocXEstado(self.oficina,1)		
		for valor in rows:
			rows_Oficina=self.obj_consulta.query_RetornaCodigo('OFICINA',valor.Oficina,'Id_Oficina','Oficina')
			self.table_Derivar.insert('','end',values=(valor.Id_Accion,valor.Cod_Pedido,valor.Nro_Pedido,valor.Descripcion,valor.Tipo,rows_Oficina[0].Oficina))


	def delete_table(self,table):
		for item in table.get_children():
			table.delete(item)
	def Recepcionar(self):
		if self.table_Recepcionar.selection():
			codigo=self.table_Recepcionar.item(self.table_Recepcionar.selection()[0])['values'][0]
			self.obj_consulta.Update_TableEstadoAccion(codigo,1)			
			messagebox.showinfo('Notificación','El documento se recepcionó!!')
			self.delete_table(self.table_Recepcionar)
			self.llenar_TablaRecepcionar()
			self.llenar_TablaDerivar()

		else:
			messagebox.showinfo('Alerta','Seleccione un Item')

	def Top_Atencion(self):

		if self.table_Derivar.selection():
			codigo_A,codigo_pedido=self.table_Derivar.item(self.table_Derivar.selection()[0])['values'][0],self.table_Derivar.item(self.table_Derivar.selection()[0])['values'][1]
			
			rows=self.obj_consulta.query_PedidoAccion(codigo_pedido,codigo_A)			

			self.TopAccion=Toplevel(self.ventana)
			self.TopAccion.iconbitmap('image/paciente.ico')
			self.TopAccion.geometry('500x450')
			self.TopAccion.title('Realizar Atencion')
			self.TopAccion.grab_set()
			self.TopAccion.resizable(0,0)

			etiqueta=Label(self.TopAccion,text='Nro: ',font=self.letra1)
			etiqueta.grid(row=1,column=1,pady=8,padx=5,sticky='e')
			self.Entry_nro=Entry(self.TopAccion,width=40)
			self.Entry_nro.insert('end',rows[0].Id_Accion)
			self.Entry_nro['state']='readonly'
			self.Entry_nro.grid(row=1,column=2,columnspan=2,ipady=3)

			etiqueta=Label(self.TopAccion,text='Codigo: ',font=self.letra1)
			etiqueta.grid(row=2,column=1,pady=8,padx=5,sticky='e')
			self.Entry_RCodigo=Entry(self.TopAccion,width=40)
			self.Entry_RCodigo.insert('end',rows[0].Cod_Pedido)
			self.Entry_RCodigo['state']='readonly'
			self.Entry_RCodigo.grid(row=2,column=2,columnspan=2,ipady=3)

			etiqueta=Label(self.TopAccion,text='Nro Doc: ',font=self.letra1)
			etiqueta.grid(row=3,column=1,pady=8,padx=5,sticky='e')
			self.Entry_RNorDoc=Entry(self.TopAccion,width=40)
			self.Entry_RNorDoc.insert('end',rows[0].Nro_Pedido)
			self.Entry_RNorDoc['state']='readonly'
			self.Entry_RNorDoc.grid(row=3,column=2,columnspan=2,ipady=3)

			etiqueta=Label(self.TopAccion,text='Documento: ',font=self.letra1)
			etiqueta.grid(row=4,column=1,pady=8,padx=5,sticky='e')
			self.Entry_RPedido=Entry(self.TopAccion,width=40)
			self.Entry_RPedido.insert('end',rows[0].Descripcion)
			self.Entry_RPedido['state']='readonly'
			self.Entry_RPedido.grid(row=4,column=2,columnspan=2,ipady=3)

			etiqueta=Label(self.TopAccion,text='Actividad: ',font=self.letra1)
			etiqueta.grid(row=5,column=1,pady=8,padx=5,sticky='e')
			self.Lista_Actividad=ttk.Combobox(self.TopAccion,width=35)
			EstadoRows=self.obj_consulta.query_tabla('ESTADO')
			self.llenarLista(self.Lista_Actividad,EstadoRows)
			self.Lista_Actividad.current(1)
			self.Lista_Actividad.bind("<<ComboboxSelected>>",self.evento_listaA)
			self.Lista_Actividad.grid(row=5,column=2,columnspan=2,ipady=3)

			etiqueta=Label(self.TopAccion,text='Motivo: ',font=self.letra1)
			etiqueta.grid(row=6,column=1,pady=8,padx=5,sticky='e')
			self.Entry_RDescripcionPedido=Text(self.TopAccion,width=37,height=6)
			self.Entry_RDescripcionPedido.grid(row=6,column=2,columnspan=2)			

			etiqueta=Label(self.TopAccion,text='Remitir A: ',font=self.letra1)
			etiqueta.grid(row=7,column=1,pady=8,padx=5,sticky='e')
			self.Lista_ROficina=ttk.Combobox(self.TopAccion,width=35)
			self.Lista_ROficina.grid(row=7,column=2,ipady=3,columnspan=2)

			btn_AccionR=Button(self.TopAccion,text="Aceptar",width=20,cursor='hand2')
			btn_AccionR['command']=self.Derivar_Doc
			btn_AccionR.grid(row=8,column=2,padx=10,pady=10,sticky='w')

			btn_AccionCancelar=ttk.Button(self.TopAccion,text="Cancelar",width=20,cursor='hand2')
			btn_AccionCancelar['command']=self.TopAccion.destroy
			btn_AccionCancelar.grid(row=8,column=3,columnspan=2,padx=10,pady=10)
			
		else:
			messagebox.showerror('Alerta','Seleccione un item')

	def llenarLista(self,lista,rows):
		listado=[]
		for valor in rows:
			listado.append(valor.Estado)
		lista['values']=listado

	def evento_listaA(self,event):
		actividad=self.Lista_Actividad.get()
		if actividad=='ATENDIDO' or actividad=='RECIBIDO':
			self.Lista_ROficina['state']='disabled'
		else:
			self.Lista_ROficina['state']='normal'
			rowsO=self.obj_consulta.query_tabla('OFICINA')
			ListOficina=[]
			for valor in rowsO:
				ListOficina.append(valor.Oficina)
			self.Lista_ROficina['values']=ListOficina
	
	def Derivar_Doc(self):
		
		valores=[]
		self.Entry_RCodigo['state']='normal'
		codigo_pedido=self.Entry_RCodigo.get()
		valores.append(codigo_pedido)		

		fecha=self.fecha_Actual.strftime("%d-%m-%Y %H:%M")
		valores.append(fecha)
		valores.append(self.dniUser)

		Descripcion=self.Entry_RDescripcionPedido.get('1.0','end-1c')
		valores.append(Descripcion)

		#obteniendo el estado.
		Estado=self.Lista_Actividad.get()
		idEstado=self.obj_consulta.query_Tabla1Condicion('ESTADO','Estado',Estado)[0].Id_Estado
		
		if idEstado!=1:
			valores.append(idEstado)
			id_oficina='X'
			try:
				if Estado=='ATENDIDO' or Estado=='RECIBIDO':
					id_oficina=self.oficina
				else:			
					id_oficina=self.obj_consulta.query_Tabla1Condicion('OFICINA','Oficina',self.Lista_ROficina.get())[0].Id_Oficina
			
				#consultamos...
			
				row_OfOrigen=self.obj_consulta.query_RetornaCodigo('PEDIDO',codigo_pedido,'cod_Pedido','Oficina')
				
				
				if row_OfOrigen[0].Oficina!=id_oficina:
					valores.append(id_oficina)
					valores.append(0)
					anio=self.fecha_Actual.strftime("%Y")
					valores.append(anio)
					valores.append(self.oficina)
				
					#insertando accion
					self.obj_consulta.Insert_Accion(valores)
					self.Entry_nro['state']='normal'
					id_Accion=self.Entry_nro.get()
					#hereeeeeee....!!
					self.obj_consulta.Update_AccionOtros(id_Accion)
					messagebox.showinfo('Notificación','Exitoso!!')
					self.llenar_TablaDerivar()				


				else:
					messagebox.showerror('Alerta','No se puede derivar')
			except Exception as e:
				 messagebox.showerror('Alerta',f'error: {e}')
			
			

		else:
			messagebox.showerror('Alerta','No se puede Recepcionar el documento en este Modulo!!')
		self.TopAccion.destroy()

	def print_expediente(self,event):
		if self.table_Derivar.selection():			
			codigo=self.table_Derivar.item(self.table_Derivar.selection()[0])['values'][1]
			rows=self.obj_consulta.query_RetornaCodigo('PEDIDO',codigo,'cod_Pedido','Nro_Tramite')
			obj_pdf=pdf.PDF(rows[0].Nro_Tramite)
			if messagebox.askquestion('Atencion','Desea Imprimir el expediente'):
				os.startfile('Expediente.pdf','print')
		else:
			messagebox.showinfo('Atencion','Seleccione un ITEM!!')
			

class Seguimiento():

	def __init__(self,oficina,usuario):		
		self.oficina=oficina
		self.usuario=usuario
		self.obj_consulta=Consulta_doc.querys()
		self.fecha_Actual=datetime.now()
	def Seguimiento(self,frame,width,height):
		letra=('Comic Sans MS',12,'bold')
		self.width=width
		self.height=height
		#647B7B
		self.Frame_Docs=Frame(frame,bg='#647B7B',width=int(width*0.6),height=int(height*0.6))
		self.Frame_Docs.place(x=int(self.width*0.5)-int((self.width*0.6)/2),y=int(self.height*0.05))
		self.Frame_Docs.grid_propagate(False)

		etiqueta=Label(self.Frame_Docs,text='Nro Expediente: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=0,column=1,pady=8,padx=5,sticky='e')
		self.Entry_NroDoc=Entry(self.Frame_Docs,width=40)		
		self.Entry_NroDoc.grid(row=0,column=2,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Tipo: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=0,column=3,pady=8,padx=5,sticky='e')
		self.Entry_anio=Entry(self.Frame_Docs,width=40)
		self.Entry_anio.insert('end',self.fecha_Actual.strftime("%Y"))
		self.Entry_anio['state']='readonly'			
		self.Entry_anio.grid(row=0,column=4,ipady=3)					

		btn_Aceptar=Button(self.Frame_Docs,text='Buscar',width=20)
		btn_Aceptar['command']=self.event_Seguimiento	
		btn_Aceptar.grid(row=7,column=2,columnspan=2,padx=10,pady=10,sticky='e')


		self.table_Seguimiento=ttk.Treeview(self.Frame_Docs,columns=('#1','#2','#3','#4','#5'),show='headings')	
		self.table_Seguimiento.heading("#1",text="Nro Doc")
		self.table_Seguimiento.column("#1",width=100,anchor="w")
		self.table_Seguimiento.heading("#2",text="Descripcion")
		self.table_Seguimiento.column("#2",width=200,anchor="w")		
		self.table_Seguimiento.heading("#3",text="Oficina")
		self.table_Seguimiento.column("#3",width=200,anchor="w")
		self.table_Seguimiento.heading("#4",text="Estado")
		self.table_Seguimiento.column("#4",width=80,anchor="w")
		self.table_Seguimiento.heading("#5",text="Fecha Movimiento")
		self.table_Seguimiento.column("#5",width=60,anchor="w")				
		self.table_Seguimiento.place(x=int(width*0.03),y=int(self.height*0.1),width=int(width*0.55),height=220)

	def event_Seguimiento(self):
		self.delete_table(self.table_Seguimiento)
		Nro_Documento=self.Entry_NroDoc.get()
		self.Entry_anio['state']='normal'
		anio=self.Entry_anio.get()

		rows=self.obj_consulta.query_Seguimiento(Nro_Documento,anio)

		for valor in rows:
			estado=self.obj_consulta.query_RetornaCodigo('ESTADO',valor.Id_Estado,'Id_Estado','Estado')
			ofi=self.obj_consulta.query_RetornaCodigo('OFICINA',valor.Id_Oficina,'Id_Oficina','Oficina')
			self.table_Seguimiento.insert('','end',values=(valor.Nro_Pedido,valor.Asunto,ofi[0].Oficina,estado[0].Estado,valor.Presentado))

	def delete_table(self,table):
		for item in table.get_children():
			table.delete(item)





		




	
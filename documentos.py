from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import generales
import Consulta_doc
from datetime import datetime
from PIL import Image
import pdf
import os
import requests
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
		self.Frame_Docs=Frame(frame,bg='#647B7B',width=int(width*0.95),height=int(height*0.88))
		self.Frame_Docs.place(x=int(width*0.02),y=int(self.height*0.03))
		self.Frame_Docs.grid_propagate(False)

		#CONSULTA
		row_tipo=self.obj_consultas.query_tablas('Tipo')
		lista_Tipo=[valor.tipo for valor in row_tipo]
		etiqueta=Label(self.Frame_Docs,text='Tipo Doc.: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=0,column=0,sticky='w')
		self.Tipo_Documento=ttk.Combobox(self.Frame_Docs,values=lista_Tipo)
		self.Tipo_Documento.current(0)
		self.Tipo_Documento.grid(row=0,column=1)

		etiqueta=Label(self.Frame_Docs,text='Multiple: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=1,column=0,sticky='w')
		self.T_Doc=ttk.Combobox(self.Frame_Docs,values=['NO','SI'])
		self.T_Doc.current(0)
		self.T_Doc.bind("<<ComboboxSelected>>",self.event_combo)
		self.T_Doc.grid(row=1,column=1)
		
		self.Entry_Codigo=Entry(self.Frame_Docs,width=40)
		self.Entry_Codigo.insert('end',self.Generar_CodigoValido('PEDIDO','cod_Pedido'))
		self.Entry_Codigo['state']='readonly'
		self.Entry_Codigo.grid(row=0,column=3,ipady=3)
		self.Entry_Codigo.grid_forget()

		etiqueta=Label(self.Frame_Docs,text='Encabezado : ',bg='#647B7B',font=letra)
		etiqueta.grid(row=0,column=4,pady=5)
		self.Entry_NroPedido=Entry(self.Frame_Docs,width=40)	
		self.Entry_NroPedido.grid(row=0,column=5,ipady=3,pady=5)

		etiqueta=Label(self.Frame_Docs,text='Razon Social: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=0,column=2,sticky='e')
		self.Entry_Razon=Entry(self.Frame_Docs,width=40)
		#EVENTO
		self.Entry_Razon.bind("<Return>",self.event_razon)
		self.Entry_Razon.bind("<Button-1>",self.event_razonDelete)
		self.Entry_Razon.grid(row=0,column=3,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Asunto: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=1,column=2,sticky='e')
		self.Entry_Asunto=Entry(self.Frame_Docs,width=40)
		self.Entry_Asunto.grid(row=1,column=3,ipady=3)


		etiqueta=Label(self.Frame_Docs,text='Descripcion: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=2,column=2,pady=8,padx=5,sticky='e')
		self.Text_Descripcion=Text(self.Frame_Docs,width=60,height=2)
		self.Text_Descripcion.grid(row=2,column=3,columnspan=10,sticky='w')

		#llenando el tipo
		etiqueta=Label(self.Frame_Docs,text='Tipo: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=3,column=2,pady=8,padx=5,sticky='e')
		self.listTipo=ttk.Combobox(self.Frame_Docs,values=['SERVICIO','BIEN','DOCUMENTO'],width=35)
		self.listTipo.current(1)
		self.listTipo.grid(row=3,column=3,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Fecha: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=3,column=4,pady=8,padx=5,sticky='e')
		self.Entry_Fecha=Entry(self.Frame_Docs,width=40)
		self.Entry_Fecha.insert('end',self.fecha_Actual.strftime("%d-%m-%Y"))
		self.Entry_Fecha.config(state='readonly')
		self.Entry_Fecha.grid(row=3,column=5,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Derivar: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=4,column=2,pady=8,padx=5,sticky='e')
		self.Lista_Oficinas=Listbox(self.Frame_Docs,width=35,height=6,selectforeground='#ffffff',selectbackground="#00aa00",selectborderwidth=2,cursor='hand2')
		self.Lista_Oficinas.grid(row=4,column=3,ipady=3,rowspan=2)
		self.llenar_Listaoficina()
	
		etiqueta=Label(self.Frame_Docs,text='Generado Por: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=5,column=4,pady=8,padx=5,sticky='e')
		self.Entry_Usuario=Entry(self.Frame_Docs,width=40)
		self.Entry_Usuario.insert('end',Usuario)
		self.Entry_Usuario['state']='readonly'
		self.Entry_Usuario.grid(row=5,column=5,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Año: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=6,column=2,pady=8,padx=5,sticky='e')
		self.Entry_Anio=Entry(self.Frame_Docs,width=40)
		self.Entry_Anio.insert('end',self.fecha_Actual.strftime("%Y"))
		self.Entry_Anio['state']='readonly'
		self.Entry_Anio.grid(row=6,column=3,ipady=3)

		etiqueta=Label(self.Frame_Docs,text='Oficina: ',font=letra,bg='#647B7B')
		etiqueta.grid(row=6,column=4,pady=8,padx=5,sticky='e')
		self.Entry_OficinaG=Entry(self.Frame_Docs,width=40)
		self.Entry_OficinaG.insert('end',self.Recuperar_OficinaGeneradora(Usuario))
		self.Entry_OficinaG['state']='readonly'
		self.Entry_OficinaG.grid(row=6,column=5,ipady=3)		

		btn_Aceptar=ttk.Button(self.Frame_Docs,text='Aceptar',width=20,cursor="hand2")
		btn_Aceptar['command']=self.Insertar_Pedido
		btn_Aceptar.grid(row=7,column=2,columnspan=2,padx=10,sticky='e')

		btn_Cancelar=ttk.Button(self.Frame_Docs,text='Cancelar',width=20,cursor='hand2')
		btn_Cancelar['command']=self.Capa
		btn_Cancelar.grid(row=7,column=4,columnspan=2,padx=10,sticky='w')

		################## AGREGANDO  LISTA DE PEDIDOS #######################
		s=ttk.Style()
		s.configure("model.Treeview",background="#1099B5")

		etiqueta=Label(self.Frame_Docs,text="LISTA DE DOCUMENTOS",bg='#647B7B',fg="#1B3A71",font=('Comic Sans MS',18,'bold'))
		etiqueta.grid(row=8,column=1,pady=5,columnspan=20)

		self.table_Documentos=ttk.Treeview(self.Frame_Docs,columns=('#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11'),show='headings',style="model.Treeview")
		self.table_Documentos.heading("#1",text="Nro")
		self.table_Documentos.column("#1",width=0,anchor="w",stretch='NO')
		self.table_Documentos.heading("#2",text="CODIGO")
		self.table_Documentos.column("#2",width=0,anchor="w",stretch='NO')
		self.table_Documentos.heading("#3",text="Encabezado")
		self.table_Documentos.column("#3",width=200,anchor="w",stretch='NO')
		self.table_Documentos.heading("#4",text="Razon Social")
		self.table_Documentos.column("#4",width=250,anchor="w",stretch='NO')
		self.table_Documentos.heading("#5",text="Asunto")
		self.table_Documentos.column("#5",width=150,anchor="w",stretch='NO')
		self.table_Documentos.heading("#6",text="Descripcion")
		self.table_Documentos.column("#6",width=300,anchor="w",stretch='NO')
		self.table_Documentos.heading("#7",text="Derivado a")
		self.table_Documentos.column("#7",width=200,anchor="w",stretch='NO')
		self.table_Documentos.heading("#8",text="Nro Exp.")
		self.table_Documentos.column("#8",width=70,anchor="w",stretch='NO')
		self.table_Documentos.heading("#9",text="Fecha")
		self.table_Documentos.column("#9",width=50,anchor="w",stretch='NO')
		self.table_Documentos.heading("#10",text="Tipo")
		self.table_Documentos.column("#10",width=50,anchor="w")
		self.table_Documentos.heading("#11",text="Correlativo")
		self.table_Documentos.column("#11",width=50,anchor="w")
		self.table_Documentos.grid(row=9,column=0,columnspan=20,rowspan=2,pady=5)
		self.llenar_tableDocumentos()		

		btn_UpDoc=ttk.Button(self.Frame_Docs,text='Eliminar',width=20,cursor="hand2")
		btn_UpDoc['command']=self.eliminar_Documento
		btn_UpDoc.grid(row=11,column=5)

		btn_EditDoc=ttk.Button(self.Frame_Docs,text='Editar',width=20,cursor="hand2")
		btn_EditDoc['command']=self.Top_Editar
		btn_EditDoc.grid(row=11,column=3)
		
		self.etiqueta_print=ttk.Button(self.Frame_Docs,text='Imprimir Exp.',width=20,cursor='hand2')		
		self.etiqueta_print.bind("<Button-1>",self.print_expediente)
		self.etiqueta_print.grid(row=11,column=4)
	def event_razon(self,event):
		dni=self.Entry_Razon.get()
		url=f'https://dniruc.apisperu.com/api/v1/dni/{dni}?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Im5vZG9oc3JhQGdtYWlsLmNvbSJ9.WkIBBcgkPKa--f49K61ReAErp0JbrPu9wULMOaqR9_E'
		response=requests.get(url)
		if response.status_code==requests.codes.ok:
			datos=response.json()
			data_razon=datos.get('nombres')+" "+datos.get('apellidoPaterno')+" "+datos.get("apellidoMaterno")
			self.Entry_Razon.delete(0,'end')
			self.Entry_Razon.insert('end',data_razon)
	def event_razonDelete(self,event):
		self.Entry_Razon.delete(0,'end')

	def event_combo(self,event):
		if self.T_Doc.get()=='SI':
			self.Lista_Oficinas.config(selectmode='multiple')
		else:
			self.Lista_Oficinas.config(selectmode='single')
		
		
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
		try:
			self.Lista_Oficinas.delete(0,'end')
			rows=self.obj_consultas.query_tablas('OFICINA')
			for val in rows:
				self.Lista_Oficinas.insert(0,val.Oficina)
			self.Lista_Oficinas.selection_set(0)
		except Exceptions as e:
			messagebox.showinfo('Alerta',f'Error {e}')
	
	def llenar_tableDocumentos(self):

		self.delete_table(self.table_Documentos)
		rows=self.obj_consultas.documentos_EmitidosUpdate(2,0,self.oficinaG)
		for valor in rows:
			self.table_Documentos.insert('','end',values=(valor.Id_Accion,valor.Cod_Pedido,valor.Nro_Pedido,valor.Razon,valor.Asunto,valor.Descripcion,valor.Oficina,valor.Nro_Expediente,valor.Fecha,valor.tipo,valor.nro_correlativo))

	def eliminar_Documento(self):

		if self.table_Documentos.selection():
			codigo_Accion=self.table_Documentos.item(self.table_Documentos.selection()[0])['values'][0]
			codigo_pedido=self.table_Documentos.item(self.table_Documentos.selection()[0])['values'][1]
			rows=self.obj_consultas.query_RetornaCodigo('PEDIDO',codigo_pedido,'cod_Pedido','Id_Expediente')
			id_expediente=rows[0].Id_Expediente

			#nro_expediente=self.table_Documentos.item(self.table_Documentos.selection()[0]['values'][7])

			try:
								
				rows_corr=self.obj_consultas.query_RetornaCodigo('ACCION',codigo_pedido,'Cod_Pedido','Id_Accion')
				for eli in rows_corr:
					self.obj_consultas.delete_itemINT('ACCION','Id_Accion',eli.Id_Accion)
					self.obj_consultas.delete_itemINT('CORRELATIVO','AccionId',eli.Id_Accion)

				self.obj_consultas.delete_itemSTR('PEDIDO','cod_Pedido',codigo_pedido)
				self.obj_consultas.delete_itemINT('EXPEDIENTE','Id_Expediente',id_expediente)
				self.llenar_tableDocumentos()
			except Exception as e:
				messagebox.showerror('Notificación',e)			

		else:
			messagebox.showinfo('Alerta','Seleccione un Item')
	def Insertar_Pedido(self):		
		#generando la lista
		datos=[]
		expendiente_data=[]
		rows_idExpediente=self.obj_consultas.query_MaxTable('EXPEDIENTE','Id_Expediente')
		Id_expediente=1
		if rows_idExpediente[0].nro==None:
			Id_expediente=1
		else:
			Id_expediente=rows_idExpediente[0].nro+1

		expendiente_data.append(Id_expediente)
		
		codigo_Pedido=self.Generar_CodigoValido('PEDIDO','cod_Pedido')
		datos.append(codigo_Pedido)

		nroPedido=self.Entry_NroPedido.get()		
		datos.append(nroPedido)

		descripcion=self.Text_Descripcion.get('1.0','end-1c')
		datos.append(descripcion)

		Clase_Doc=self.listTipo.get()
		datos.append(Clase_Doc)		

		fecha=self.fecha_Actual.strftime("%d-%m-%Y %H:%M")
		datos.append(fecha)

		#oficina
		oficinasList=[self.Lista_Oficinas.get(idx) for idx in self.Lista_Oficinas.curselection()]
		
		#oficina_Derivar=self.Lista_Oficinas.selection_get()
		codiOficina=[]	
		for ofi in oficinasList:
			rows=self.obj_consultas.query_RetornaCodigo('OFICINA',ofi,'Oficina','Id_Oficina')
			codiOficina.append(rows[0].Id_Oficina)	
		#datos.append(codigo_Oficina)

		#Oficina generadora
		self.Entry_OficinaG['state']='normal'
		oficina_Generadora=self.Entry_OficinaG.get()[:5]
		expendiente_data.append(oficina_Generadora)
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

		#tipo de documento
		tipoDoc=self.Tipo_Documento.get()
		nro_expediente=0
		if tipoDoc=='EXTERNO':
			rows=self.obj_consultas.consulta_MaxExpedienteExterno(oficina_Generadora)
			if rows[0].nro==None:
				nro_expediente=1
			else:
				nro_expediente= rows[0].nro+1
		else:
			rows_interno=self.obj_consultas.consulta_MaxExpedienteInterno(oficina_Generadora)		
						
			if rows_interno[0].nro==None:			
				nro_expediente=1
			else:
				nro_expediente=rows_interno[0].nro+1

	
		expendiente_data.append(nro_expediente)
		expendiente_data.append(anio)
		tipo=self.Tipo_Documento.get()
		Id_tipo=self.obj_consultas.query_RetornaCodigo('Tipo',tipo,'tipo','Id_Tipo')[0].Id_Tipo		
		expendiente_data.append(Id_tipo)

		datos.append(Id_expediente)
		#asunto
		razon=self.Entry_Razon.get()
		datos.append(razon)

		#Asunto
		asunto=self.Entry_Asunto.get()
		datos.append(asunto)

		#hora
		Hora=self.fecha_Actual.strftime("%H:%M")
		datos.append(Hora)


		datosAccionGeneradora=[]
		datosAccion=[]
		datosCorrelativo=[]
		nro_Accion=0
		rows_accion=self.obj_consultas.query_MaxTable('ACCION','Id_Accion')			
		if rows_accion[0].nro==None:
			nro_Accion=1
		else:
			nro_Accion=rows_accion[0].nro+1
		nro_Accion1=nro_Accion
		datosAccionGeneradora=[nro_Accion1,codigo_Pedido,fecha,codigo_Usuario,'ninguna',1,oficina_Generadora,1,anio,oficina_Generadora,1]
		rows_=self.obj_consultas.consulta_MaxCorrelativo(oficina_Generadora)
		nro_corre1=0
		if rows_[0].nro==None:
			nro_corre1=1
		else:
			nro_corre1=rows_[0].nro+1

		datosCorrelativoGeneradora=[nro_corre1,anio,oficina_Generadora,nro_Accion1]



		nro_Accion2=nro_Accion1

		

		for v in codiOficina:				
			#reestriccion de pedido		
			nro_Accion2=nro_Accion2+1			
			datosAccion.append([nro_Accion2,codigo_Pedido,fecha,codigo_Usuario,'ninguna',2,v,0,anio,oficina_Generadora,1])
			nro_corre=0
			rows=self.obj_consultas.consulta_MaxCorrelativo(v)			
			if rows[0].nro==None:
				nro_corre=1
			else:
				nro_corre=rows[0].nro+1
				
			datosCorrelativo.append([nro_corre,anio,v,nro_Accion2])		

	
		if not (oficina_Generadora in codiOficina):
			if tipo=='INTERNO':				

				self.obj_consultas.Insert_Expediente(expendiente_data)
				self.obj_consultas.query_InsertarPedido(datos)
				self.obj_consultas.Insert_Accion(datosAccionGeneradora)
				self.obj_consultas.Insert_Correlativo(datosCorrelativoGeneradora)
				for valores in datosAccion:					
					self.obj_consultas.Insert_Accion(valores)
				for valores1 in datosCorrelativo:				
					self.obj_consultas.Insert_Correlativo(valores1)
				messagebox.showinfo('Notificación','se registró correctamente!!')
				#print(datosCorrelativo)
				self.Capa()		

			elif tipo=='EXTERNO' and oficina_Generadora=='AAAAA':	
				self.obj_consultas.Insert_Expediente(expendiente_data)
				self.obj_consultas.query_InsertarPedido(datos)
				self.obj_consultas.Insert_Accion(datosAccionGeneradora)				
				self.obj_consultas.Insert_Correlativo(datosCorrelativoGeneradora)
				for valores in datosAccion:
					self.obj_consultas.Insert_Accion(valores)
				for valores1 in datosCorrelativo:
					self.obj_consultas.Insert_Correlativo(valores1)

				messagebox.showinfo('Notificación','se registró correctamente!!')
				self.Capa()
			else:
				messagebox.showerror('error!!','Verifique el tipo de documento, recuerde que documentos \n externos solo puede generara MESA DE PARTES')			
			
			self.llenar_tableDocumentos()
		else:
			messagebox.showerror('Error','No se puede derivar a la misma oficina')

	def Capa(self):
		self.Frame_Capa=Frame(self.Frame_Docs,bg='#647B7B',width=int(self.width*0.7),height=int(self.height*0.88))
		self.Frame_Capa.place(x=0,y=0)
		self.Frame_Capa.grid_propagate(False)

	def delete_table(self,table):
		for item in table.get_children():
			table.delete(item)

	def print_expediente(self,event):
		if self.table_Documentos.selection():			
			codigo=self.table_Documentos.item(self.table_Documentos.selection()[0])['values'][1]
			rows=self.obj_consultas.consulta_PedidoPdf(codigo)			
			obj_pdf=pdf.PDF(rows[0].Nro_Expediente,rows[0].Razon,rows[0].Asunto,rows[0].tipo)
			if messagebox.askquestion('Atencion','Desea Imprimir el expediente'):				
				os.startfile('Expediente.pdf','print')
				
		else:
			messagebox.showinfo('Atencion','Seleccione un ITEM!!')
	def Top_Editar(self):
		letra1=('Comic Sans MS',12,'bold')
		if self.table_Documentos.selection():
			codigo_A,codigo_pedido=self.table_Documentos.item(self.table_Documentos.selection()[0])['values'][0],self.table_Documentos.item(self.table_Documentos.selection()[0])['values'][1]			
			rows_Oficina=self.obj_consultas.query_tablas('OFICINA')
			rows_contenido=self.obj_consultas.query_Tabla1Condicion('PEDIDO','cod_Pedido',codigo_pedido)

			self.TopEditar=Toplevel()
			self.TopEditar.iconbitmap('image/paciente.ico')
			self.TopEditar.geometry('500x450')
			self.TopEditar.title('Editar el Documento')
			self.TopEditar.grab_set()
			self.TopEditar.resizable(0,0)


			etiqueta=Label(self.TopEditar,text='Encabezado: ',font=letra1)
			etiqueta.grid(row=1,column=1,pady=8,padx=5,sticky='e')
			self.Entry_nroE=Entry(self.TopEditar,width=40)		
			self.Entry_nroE.insert('end',rows_contenido[0].Nro_Pedido)
			self.Entry_nroE.grid(row=1,column=2,columnspan=2,ipady=3)		

			etiqueta=Label(self.TopEditar,text='Asunto: ',font=letra1)
			etiqueta.grid(row=3,column=1,pady=8,padx=5,sticky='e')
			self.Entry_AsuntoE=Entry(self.TopEditar,width=40)
			self.Entry_AsuntoE.insert('end',rows_contenido[0].Asunto)
			#self.Entry_RNorDoc['state']='readonly'
			self.Entry_AsuntoE.grid(row=3,column=2,columnspan=2,ipady=3)

			etiqueta=Label(self.TopEditar,text='Razon Social: ',font=letra1)
			etiqueta.grid(row=4,column=1,pady=8,padx=5,sticky='e')
			self.Entry_RazonE=Entry(self.TopEditar,width=40)
			self.Entry_RazonE.insert('end',rows_contenido[0].Razon)
			#self.Entry_RPedido['state']='readonly'
			self.Entry_RazonE.grid(row=4,column=2,columnspan=2,ipady=3)

		
			etiqueta=Label(self.TopEditar,text='Derivar: ',font=letra1)
			etiqueta.grid(row=5,column=1,pady=8,padx=5,sticky='e')
			self.Lista_DerivarE=ttk.Combobox(self.TopEditar,width=35,height=10)			
			self.llenarLista(self.Lista_DerivarE,rows_Oficina)
			self.Lista_DerivarE.current(1)			
			self.Lista_DerivarE.grid(row=5,column=2,columnspan=2,ipady=3)

			etiqueta=Label(self.TopEditar,text='Motivo: ',font=letra1)
			etiqueta.grid(row=6,column=1,pady=8,padx=5,sticky='e')
			self.Entry_DescripcionE=Text(self.TopEditar,width=37,height=6)
			self.Entry_DescripcionE.grid(row=6,column=2,columnspan=2)		

			btn_AccionR=ttk.Button(self.TopEditar,text="Aceptar",width=20,cursor='hand2')
			btn_AccionR['command']=lambda: self.Event_Editar(codigo_pedido,codigo_A)
			btn_AccionR.grid(row=8,column=2,padx=10,pady=10,sticky='w')

			btn_AccionCancelar=ttk.Button(self.TopEditar,text="Cancelar",width=20,cursor='hand2')
			btn_AccionCancelar['command']=self.TopEditar.destroy
			btn_AccionCancelar.grid(row=8,column=3,columnspan=2,padx=10,pady=10)
		else:
			messagebox.showerror('Alerta','Seleccione un ITEM')

	def llenarLista(self,lista,rows):
		listado=[]
		for valor in rows:
			listado.append(valor.Oficina)
		lista['values']=listado
	def Event_Editar(self,codigoPedido,codigoAccion):
		numeracion=self.Entry_nroE.get()
		asunto=self.Entry_AsuntoE.get()
		razon_social=self.Entry_RazonE.get()
		oficina_Derivar=self.Lista_DerivarE.get()
		Descripcion=self.Entry_DescripcionE.get('1.0','end-1c')
		# recuperando el codigo de la oficina
		rows_oficina=self.obj_consultas.query_RetornaCodigo('OFICINA',oficina_Derivar,'Oficina','Id_Oficina')
		id_oficina=rows_oficina[0].Id_Oficina

		#actualizar...
		self.obj_consultas.update_Pedido(codigoPedido,numeracion,asunto,razon_social,Descripcion)
		self.obj_consultas.Update_Accion(codigoAccion,id_oficina)
		messagebox.showinfo('Notificación','Exitoso!!')	
		self.TopEditar.destroy()
		self.Capa()


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
		#647B7B
		self.Frame_Docs=Frame(frame,bg='#647B7B',width=int(width*0.98),height=int(height*0.92))
		self.Frame_Docs.place(x=0,y=0)
		self.Frame_Docs.grid_propagate(False)
		etiqueta=Label(self.Frame_Docs,text='DOCUMENTOS POR RECEPCIONAR',width=int(width*0.1),font=letra,bg="#34A2DE")
		etiqueta.place(x=0,y=10)
		self.table_Recepcionar=ttk.Treeview(self.Frame_Docs,columns=('#1','#2','#3','#4','#5','#6','#7','#8','#9','#10'),show='headings')				
		#self.table_Recepcionar.column("#0",width=600)
		self.table_Recepcionar.heading("#1",text="Nro")
		self.table_Recepcionar.column("#1",width=0,anchor="w",stretch='NO')
		self.table_Recepcionar.heading("#2",text="CODIGO")
		self.table_Recepcionar.column("#2",width=0,anchor="w",stretch='NO')
		self.table_Recepcionar.heading("#3",text="Razon Social")
		self.table_Recepcionar.column("#3",width=150,anchor="w")
		self.table_Recepcionar.heading("#4",text="Asunto")
		self.table_Recepcionar.column("#4",width=150,anchor="w")		
		self.table_Recepcionar.heading("#5",text="Emitido Desde")
		self.table_Recepcionar.column("#5",width=150,anchor="w",stretch='NO')
		self.table_Recepcionar.heading("#6",text="Observaciones")
		self.table_Recepcionar.column("#6",width=300,anchor="w",stretch='NO')
		self.table_Recepcionar.heading("#7",text="Fecha")
		self.table_Recepcionar.column("#7",width=50,anchor="w")
		self.table_Recepcionar.heading("#8",text="Nro Expediente")
		self.table_Recepcionar.column("#8",width=150,anchor="w")
		self.table_Recepcionar.heading("#9",text="Correlativo")
		self.table_Recepcionar.column("#9",width=50,anchor="w")	
		self.table_Recepcionar.heading("#10",text="Tipo")
		self.table_Recepcionar.column("#10",width=50,anchor="w")	
		self.table_Recepcionar.place(x=int(width*0.03),y=60,width=int(width*0.85),height=220)		
		self.llenar_TablaRecepcionar()
		btn_AccionR=ttk.Button(self.Frame_Docs,text="Recepcionar",width=20,cursor='hand2')
		btn_AccionR['command']=self.Recepcionar
		btn_AccionR.place(x=int(width*0.3),y=300)



		etiqueta=Label(self.Frame_Docs,text='DOCUMENTOS POR ATENDER',bg='#34A2DE',width=int(width*0.1),font=letra)
		etiqueta.place(x=0,y=int(height*0.5))

		self.table_Derivar=ttk.Treeview(self.Frame_Docs,columns=('#1','#2','#3','#4','#5','#6','#7','#8','#9','#10'),show='headings')				
		
		self.table_Derivar.heading("#1",text="Nro")
		self.table_Derivar.column("#1",width=0,anchor="w",stretch='NO')
		self.table_Derivar.heading("#2",text="CODIGO")
		self.table_Derivar.column("#2",width=0,anchor="w",stretch='NO')
		self.table_Derivar.heading("#3",text="Razon Social")
		self.table_Derivar.column("#3",width=150,anchor="w")
		self.table_Derivar.heading("#4",text="Asunto")
		self.table_Derivar.column("#4",width=150,anchor="w")
		self.table_Derivar.heading("#5",text="Emitido Desde")
		self.table_Derivar.column("#5",width=100,anchor="w")
		self.table_Derivar.heading("#6",text="Observaciones")
		self.table_Derivar.column("#6",width=300,anchor="w",stretch='NO')
		self.table_Derivar.heading("#7",text="Fecha")
		self.table_Derivar.column("#7",width=50,anchor="w")
		self.table_Derivar.heading("#8",text="Nro Expediente")
		self.table_Derivar.column("#8",width=150,anchor="w")
		self.table_Derivar.heading("#9",text="Correlativo")
		self.table_Derivar.column("#9",width=50,anchor="w")
		self.table_Derivar.heading("#10",text="Tipo")
		self.table_Derivar.column("#10",width=50,anchor="w")

		self.table_Derivar.place(x=int(width*0.03),y=int(height*0.55),width=int(width*0.85),height=220)
		self.llenar_TablaDerivar()

		btn_AccionD=ttk.Button(self.Frame_Docs,text="Atender",width=20,cursor='hand2')
		btn_AccionD['command']=self.Top_Atencion
		btn_AccionD.place(x=int(width*0.3),y=int(height*0.85))

		image=PhotoImage(file='image/impre.png')
		self.etiqueta_print=Label(self.Frame_Docs,image=image,bg='#647B7B',cursor='hand2')
		self.etiqueta_print.image=image
		self.etiqueta_print.bind("<Button-1>",self.print_expediente)
		self.etiqueta_print.place(x=int(width*0.92),y=int(height*0.58))

	def llenar_TablaRecepcionar(self):
		rows=self.obj_consulta.query_DocXEstado(self.oficina,2)		
		for valor in rows:
			rows_Oficina=self.obj_consulta.query_RetornaCodigo('OFICINA',valor.Oficina,'Id_Oficina','Oficina')
			self.table_Recepcionar.insert('','end',values=(valor.Id_Accion,valor.Cod_Pedido,valor.Razon,valor.Asunto,rows_Oficina[0].Oficina,valor.Observacion,valor.Fecha,valor.Nro_Expediente,valor.nro_correlativo,valor.tipo))


	def llenar_TablaDerivar(self):
		self.delete_table(self.table_Derivar)
		rows=self.obj_consulta.query_DocXEstado(self.oficina,1)		
		for valor in rows:
			rows_Oficina=self.obj_consulta.query_RetornaCodigo('OFICINA',valor.Oficina,'Id_Oficina','Oficina')
			self.table_Derivar.insert('','end',values=(valor.Id_Accion,valor.Cod_Pedido,valor.Razon,valor.Asunto,rows_Oficina[0].Oficina,valor.Observacion,str(valor.Fecha)[:16],valor.Nro_Expediente,valor.nro_correlativo,valor.tipo))


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
			etiqueta.grid_forget()
			self.Entry_nro=Entry(self.TopAccion,width=40)			
			self.Entry_nro.insert('end',rows[0].Id_Accion)			
			self.Entry_nro['state']='readonly'
			self.Entry_nro.grid(row=1,column=2,columnspan=2,ipady=3)
			self.Entry_nro.grid_forget()

			#NRO EXPEDIENTE
			etiqueta=Label(self.TopAccion,text='Nro Expediente: ',font=self.letra1)
			etiqueta.grid(row=1,column=1,pady=8,padx=5,sticky='e')
			
			self.Entry_Expediente=Entry(self.TopAccion,width=40)
			self.Entry_Expediente.insert('end',rows[0].Nro_Expediente)						
			self.Entry_Expediente['state']='readonly'
			self.Entry_Expediente.grid(row=1,column=2,columnspan=2,ipady=3)
			#FIN EXPEDIENTE

			etiqueta=Label(self.TopAccion,text='Codigo: ',font=self.letra1)
			etiqueta.grid(row=2,column=1,pady=8,padx=5,sticky='e')
			etiqueta.grid_forget()
			self.Entry_RCodigo=Entry(self.TopAccion,width=40)
			self.Entry_RCodigo.insert('end',rows[0].Cod_Pedido)
			self.Entry_RCodigo['state']='readonly'
			self.Entry_RCodigo.grid(row=2,column=2,columnspan=2,ipady=3)
			self.Entry_RCodigo.grid_forget()

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

			btn_AccionR=ttk.Button(self.TopAccion,text="Aceptar",width=20,cursor='hand2')
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

		rows_accion=self.obj_consulta.query_MaxTable('ACCION','Id_Accion')
		nro_Accion=0
		if rows_accion[0].nro==None:
			nro_Accion=1
		else:
			nro_Accion=rows_accion[0].nro+1

		valores.append(nro_Accion)

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
				#row_OfOrigen=self.obj_consulta.query_RetornaCodigo('PEDIDO',codigo_pedido,'cod_Pedido','Oficina')
									
				valores.append(id_oficina)
				valores.append(0)
				anio=self.fecha_Actual.strftime("%Y")
				valores.append(anio)
				valores.append(self.oficina)
				valores.append(0)				
				#insertando accion
				self.obj_consulta.Insert_Accion(valores)
				#insertando correlativo
				rows=self.obj_consulta.consulta_MaxCorrelativo(id_oficina)
				nro_corre=0
				if rows[0].nro==None:
					nro_corre=1
				else:
					nro_corre=rows[0].nro+1

				datosCorrelativo=[nro_corre,anio,id_oficina,nro_Accion]
				self.obj_consulta.Insert_Correlativo(datosCorrelativo)

				#fin de insertar correlativo
				self.Entry_nro['state']='normal'
				id_Accion=self.Entry_nro.get()
				#hereeeeeee....!!
				self.obj_consulta.Update_AccionOtros(id_Accion)
				messagebox.showinfo('Notificación','Exitoso!!')
				self.llenar_TablaDerivar()
				
			except Exception as e:
				 messagebox.showerror('Alerta',f'error: {e}')			

		else:
			messagebox.showerror('Alerta','No se puede Recepcionar el documento en este Modulo!!')
		self.TopAccion.destroy()

	def print_expediente(self,event):
		if self.table_Derivar.selection():			
			codigo=self.table_Derivar.item(self.table_Derivar.selection()[0])['values'][1]
			rows=self.obj_consulta.consulta_PedidoPdf(codigo)			
			obj_pdf=pdf.PDF(rows[0].Nro_Expediente,rows[0].Razon,rows[0].Asunto,rows[0].tipo)
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
		self.List_Tipo=ttk.Combobox(self.Frame_Docs,values=['INTERNO','EXTERNO'],width=20)					
		self.List_Tipo.grid(row=0,column=4,ipady=3)	
		self.List_Tipo.current(1)

		etiqueta=Label(self.Frame_Docs,text='Oficina: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=0,column=5,pady=8,padx=5,sticky='e')
		self.List_oficinas=ttk.Combobox(self.Frame_Docs,width=20)					
		self.List_oficinas.grid(row=0,column=6,ipady=3)
		self.llenarOficinas()
		self.List_oficinas.current(1)	

		etiqueta=Label(self.Frame_Docs,text='Año: ',bg='#647B7B',font=letra)
		etiqueta.grid(row=0,column=7,pady=8,padx=5,sticky='e')
		self.Entry_anio=Entry(self.Frame_Docs,width=25)
		self.Entry_anio.insert('end',self.fecha_Actual.strftime("%Y"))
		#self.Entry_anio['state']='readonly'			
		self.Entry_anio.grid(row=0,column=8,ipady=3)
						

		btn_Aceptar=ttk.Button(self.Frame_Docs,text='Buscar',width=20)
		btn_Aceptar['command']=self.event_Seguimiento	
		btn_Aceptar.grid(row=7,column=4,columnspan=2,padx=10,pady=10,sticky='e')

		self.table_Seguimiento=ttk.Treeview(self.Frame_Docs,columns=('#1','#2','#3','#4','#5'),show='headings')	
		self.table_Seguimiento.heading("#1",text="Razon")
		self.table_Seguimiento.column("#1",width=200,anchor="w")
		self.table_Seguimiento.heading("#2",text="Observaciones")
		self.table_Seguimiento.column("#2",width=200,anchor="w",stretch="NO")		
		self.table_Seguimiento.heading("#3",text="Oficina")
		self.table_Seguimiento.column("#3",width=150,anchor="w")
		self.table_Seguimiento.heading("#4",text="Estado")
		self.table_Seguimiento.column("#4",width=80,anchor="w")		
		self.table_Seguimiento.heading("#5",text="Fecha Movimiento")
		self.table_Seguimiento.column("#5",width=60,anchor="w")				
		self.table_Seguimiento.place(x=int(width*0.03),y=int(self.height*0.2),width=int(width*0.55),height=int(height*0.5))

	def event_Seguimiento(self):
		self.delete_table(self.table_Seguimiento)
		Nro_Documento=self.Entry_NroDoc.get()		
		anio=self.Entry_anio.get()
		oficina=self.List_oficinas.get()
		tipo=self.List_Tipo.get()	
		rows=self.obj_consulta.query_Seguimiento(Nro_Documento,anio,oficina,tipo)

		for valor in rows:
			oficina_rows=self.obj_consulta.query_RetornaCodigo('OFICINA',valor.Id_Oficina,'Id_Oficina','Oficina')			
			self.table_Seguimiento.insert('','end',values=(valor.Razon,valor.Observacion,oficina_rows[0].Oficina,valor.Estado,str(valor.Fecha)[:16]))

	def llenarOficinas(self):		
		rowsO=self.obj_consulta.query_tabla('OFICINA')
		ListOficina=[]
		for valor in rowsO:
			ListOficina.append(valor.Oficina)
		self.List_oficinas['values']=ListOficina

	def delete_table(self,table):
		for item in table.get_children():
			table.delete(item)





		




	
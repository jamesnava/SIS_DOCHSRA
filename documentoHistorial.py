from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import Consulta_doc

class DocumentoAccion(object):
	

	def __init__(self,oficina,usuario):
		self.oficina=oficina

		self.usuario=usuario
		self.letra_titulo=('Segoe Script',18,'bold')
		self.obj_consulta=Consulta_doc.querys()
	def Top_Menu(self,frame,width,height):
		self.width=width
		self.height=height
		letra=('Comic Sans MS',24,'bold')
		frame_left=Frame(frame,width=int(width*0.15),height=int(height*0.88),bg='#181F50')		
		frame_left.place(x=0,y=0)
		self.Lista_Menu=Listbox(frame_left,width=int(width*0.1),height=int(height*0.059),cursor='hand2')
		items=('Historial','Rechazados','Atendidos')
		self.Lista_Menu.insert(0,*items)
		self.Lista_Menu.place(x=0,y=0)
		self.Lista_Menu.bind("<<ListboxSelect>>",self.Frame_evento)
		

		self.frame_main=ttk.Frame(frame,width=int(width*0.83),height=int(height*0.88),relief='sunken')
		self.frame_main.place(x=200,y=0)
		
	def frame_Historial(self):
		label=ttk.Label(self.frameH,text='HISTORIAL DE DOCUMENTOS DEL AREA',font=self.letra_titulo,bootstyle='inverse-secondary')
		label.place(x=int(self.width*0.3),y=10)

		label=ttk.Label(self.frameH,text='Search: ',font=('Segoe Script',12,'bold'),bootstyle='inverse-secondary')
		label.place(x=int(self.width*0.03),y=50)

		self.table_Historial=ttk.Treeview(self.frameH,columns=('#1','#2','#3','#4','#5','#6','#7','#8','#9'),show='headings',style='success.Treeview')		
		self.table_Historial.heading("#1",text="Nro")
		self.table_Historial.column("#1",width=0,anchor="w",stretch='NO')
		self.table_Historial.heading("#2",text="CODIGO")
		self.table_Historial.column("#2",width=0,anchor="w",stretch='NO')
		self.table_Historial.heading("#3",text="Razon Social")
		self.table_Historial.column("#3",width=150,anchor="w")
		self.table_Historial.heading("#4",text="Asunto")
		self.table_Historial.column("#4",width=150,anchor="w")		
		self.table_Historial.heading("#5",text="Emitido Desde")
		self.table_Historial.column("#5",width=150,anchor="w",stretch='NO')		
		self.table_Historial.heading("#6",text="Fecha")
		self.table_Historial.column("#6",width=50,anchor="w")		
		self.table_Historial.heading("#7",text="Correlativo")
		self.table_Historial.column("#7",width=50,anchor="w")	
		self.table_Historial.heading("#8",text="Tipo")
		self.table_Historial.column("#8",width=50,anchor="w")
		self.table_Historial.heading("#9",text="Estado")
		self.table_Historial.column("#9",width=50,anchor="w")		
		self.table_Historial.place(x=int(self.width*0.01),y=100,width=int(self.width*0.7),height=400)
		self.llenar_Table()
		entry_search=ttk.Entry(self.frameH,width=50)
		entry_search.place(x=int(self.width*0.08),y=50)

		etiqueta_Exportar=Label(self.frameH,text="Exportar",bg='#647B7B',fg='red',cursor='hand2')
		etiqueta_Exportar.place(x=int(self.width*0.03),y=500)
	def llenar_Table(self):
		area=self.oficina
		rows=self.obj_consulta.query_allDocsArea(area)		
		for valor in rows:
			rows_Oficina=self.obj_consulta.query_RetornaCodigo('OFICINA',valor.ASOC_OFICINA,'Id_Oficina','Oficina')
			self.table_Historial.insert('','end',values=('0','0',valor.Razon,valor.Asunto,rows_Oficina[0].Oficina,valor.Fecha,valor.nro_correlativo,valor.tipo,valor.Estado))


	def Frame_evento(self,event):
		selection_=self.Lista_Menu.curselection()
		selection=self.Lista_Menu.get(selection_)
		if selection=='Historial':
			self.frameH=ttk.Frame(self.frame_main,width=int(self.width*0.83),height=int(self.height*0.90),relief='sunken',style='secondary.TFrame')		
			self.frame_Historial()
			self.frameH.place(x=0,y=0)
		if selection=='Rechazados':
			frameR=Frame(self.frame_main,width=int(self.width*0.83),height=int(self.height*0.90),bg='#647B7B')		
			frameR.place(x=0,y=0)
			

	
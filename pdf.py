from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class PDF():
	def __init__(self,nro_expediente):
		pdfmetrics.registerFont(TTFont('Banana','Heavitas.ttf'))
		self.NroExpediente=nro_expediente
		self.width,self.height=A4
		self.Hoja=canvas.Canvas("Expediente.pdf",pagesize=A4)
		self.Hoja.setFont('Helvetica',10)
		self.Hoja.drawString(int(self.width*0.65),self.height-50,"DIRECCION EJECUTIVA DEL HOSPITAL")
		self.Hoja.drawString(int(self.width*0.7),self.height-60,"TRAMITE DOCUMENTARIO")
		self.set_image(10,self.height-80)
		self.Hoja.setFont('Banana',20)
		self.Hoja.setFillColorRGB(0,0,0.5) 
		self.Hoja.drawString(int(self.width*0.35),self.height-100,"HOJA DE TRAMITE")
		self.Hoja.setFont('Banana',8)
		self.Hoja.setFillColorRGB(0,0,0) 
		self.Hoja.drawString(10,self.height-130,"Nombre y Razon:")
		self.Hoja.drawString(100,self.height-130,".."*90)
		self.Hoja.drawString(int(self.width*0.73),self.height-130,"Nro Reg:")
		#self.Hoja.drawString(int(self.width*0.8),self.height-130,"..."*12)
		self.Hoja.setFont('Banana',10)
		self.Hoja.drawString(int(self.width*0.81),self.height-130,f"{nro_expediente}")
		self.Hoja.setFont('Banana',8)
		self.Hoja.drawString(10,self.height-150,"Asunto:")
		self.Hoja.drawString(100,self.height-150,"......"*40)
		self.Hoja.drawString(100,self.height-170,"......"*40)
		self.set_grilla(20,self.Hoja,self.height-int(self.height*0.75))
		self.cabecera(self.Hoja)
		self.Leyenda(10,200)
		self.observaciones(10,int(self.height*0.20))

		self.Hoja.showPage()
		self.Hoja.save()
	def cabecera(self,Hoja):
		cabecera=['ENTREGAR A','PARA','FECHA','ACCION','FIRMA']
		for i,valor in enumerate(cabecera):
			self.Hoja.drawString(self.x[i]+5,self.height-int(self.height*0.27),valor)
	def set_grilla(self,separacion,Hoja,posicionActual):
		self.x=[10,170,320,380,450,550]
		y=[]
		suma=0
		for i in range(0,14):
			y.append(int(self.height-(posicionActual+suma)))
			suma=suma+separacion
		#print(y)
		Hoja.grid(self.x,y)
	def Leyenda(self,x,y):
		self.Hoja.rect(x, y-10, 560, 170)
		col1=['Accion Necesaria Inmediata','Acompañar Antecedentes','Archivar','Cancelacion','Devolver al Interesado','Firma','Atencion','Transcripcion']
		col2=['Informe','Liquidacion','Por Corresponderle','Preparar respepuesta','Proyeccion de Resolucion','Segun Solicitado','Su Conocimiento','Formular Pedido']
		col3=['','','Visacion','Hacer Saber al Interesado','Para conversar','Ver Observacion','Opinion','otros']
		data=[col1,col2,col3]
		num=0
		acumulacionx=0
		for i in range(len(data)):
			acumulaciony=0	
			num+=8
			v=num
			for k in range(len(data[i])):
				self.Hoja.drawString(x+acumulacionx+5,y+acumulaciony,str(v))			
				self.Hoja.drawString(x+acumulacionx+20,y+acumulaciony,data[i][k])
				
				acumulaciony+=20
				v-=1
			acumulacionx+=200
	def observaciones(self,x,y):
		self.Hoja.setFont('Banana',8)
		self.Hoja.setFillColorRGB(0,0,0) 
		self.Hoja.drawString(x,y,"Observaciones:")
		self.Hoja.drawString(x+35,y-20,"......."*40)
		self.Hoja.drawString(x+35,y-40,"......."*40)
		
	def set_image(self,x,y):
		self.Hoja.drawImage("image/hospital.png",x,y,width=65,height=65)


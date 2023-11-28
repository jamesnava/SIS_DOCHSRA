from tkinter import *
import ttkbootstrap  as ttk
from tkinter import messagebox
import usuario
import V_Main
import time


class Login():
	def __init__(self):
		self.obj_usuario=usuario.usuario()
		font_label=('Candara',16)
		self.root=ttk.Window(themename='yeti')
		#self.root.title('Buscar Establecimiento')
		self.root.config(bg='#707070')
		self.root.resizable(width=False,height=False)
		self.root.overrideredirect(True)
		height=self.root.winfo_screenheight()
		width=self.root.winfo_screenwidth()
		height_login=550
		width_login=500
		self.root.geometry(f'{width_login}x{height_login}+{int(width_login/2)}+{int(width_login/2-200)}')
		#crear mainframe
		self.mainFrame=ttk.Frame(self.root)
		self.mainFrame.config(bootstyle='secondary')	
		self.mainFrame.pack()
		self.mainFrame.config(width=500,height=400)
		#self.mainFrame.config(width=900,height=height)
		titulo=ttk.Label(self.mainFrame,text='INICIAR SESIÓN',font=("Arial-bold",24),bootstyle='inverse-secondary')
		titulo.grid(column=0,row=0,columnspan=2)

		log_image=PhotoImage(file='image/administrativo.png')
		Label_image=Label(self.mainFrame,image=log_image)
		Label_image.grid(row=1,column=0,columnspan=2,pady=10)

		txt_user=ttk.Label(self.mainFrame,text='Usuario: ',font=font_label,bootstyle='inverse-secondary')
		txt_user.grid(row=2,column=0,pady=10)
		self.Entry_User=ttk.Entry(self.mainFrame,width=30)
		self.Entry_User.grid(row=2,column=1,pady=10)
		self.Entry_User.focus()

		txt_contra=ttk.Label(self.mainFrame,text='Contraseña: ', font=font_label,bootstyle='inverse-secondary')
		txt_contra.grid(row=3,column=0,pady=15)
		self.Entry_Contra=ttk.Entry(self.mainFrame,show='◘',width=30)
		self.Entry_Contra.bind('<Return>',lambda event:self.conectar(event))
		self.Entry_Contra.grid(row=3,column=1,pady=15)
		

		#creamos un barra de progreso		
		self.bar=ttk.Progressbar(self.mainFrame,length=100)
		self.bar.grid(row=4,column=0,columnspan=2,sticky='WE')
		self.bar.step(0)
		#Creamoos boton
		self.btn_iniciar=ttk.Button(self.mainFrame,text='Iniciar',cursor='hand2',width=25,bootstyle='SUCCESS')
		self.btn_iniciar.bind('<Button-1>',lambda event:self.conectar(event))
		self.btn_iniciar.grid(row=5,column=0,pady=50)
		
		self.btn_cerrar=ttk.Button(self.mainFrame,text='Cerrar',cursor='hand2',width=25,bootstyle='DANGER')
		self.btn_cerrar.grid(row=5,column=1,pady=50)
		self.btn_cerrar['command']=self.root.quit
		self.root.mainloop()

	def conectar(self,event):
		#obj_usuario=usuario()
		try:
			u=self.Entry_User.get()
			c=self.Entry_Contra.get()			
			identificador,usuario,rol,estado=self.obj_usuario.conectar(u,c)
			if identificador==-1:
				messagebox.showerror('Alerta','Datos Incorrectos o el usuario no Existe')
				self.Entry_User.delete(0,'end')
				self.Entry_Contra.delete(0,'end')
				self.Entry_User.focus()
			elif identificador==1 and estado=="ACTIVO":			
				for i in range(0,100,5):				
					self.bar['value']+=5
					self.root.update()
					time.sleep(0.1)				
					if i==100:
						break
				self.root.withdraw()
				#self.root.destroy()
				V_Main.Ventana_Principal(usuario,rol,self.root)

			elif estado=="INACTIVO":
				messagebox.showerror('Alerta','Usuario Inactivo')
				self.Entry_User.delete(0,'end')
				self.Entry_Contra.delete(0,'end')
				self.Entry_User.focus()

		except Exception as e:
			raise e	

if __name__=="__main__":
	Login()


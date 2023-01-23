from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
from PIL import ImageTk,Image


class Login():
	def __init__(self):		
		self.root=Tk()
		self.root.title('Administrador SIS_DOC')
		#self.root.config(bg='#252F61')
		self.root.resizable(width=False,height=False)
		#self.root.overrideredirect(True)
		self.Frame_Main=Frame(self.root,bg='black')
		self.Frame_Main.place(x=0,y=0)		
		self.Frame_Main.config(width=500,height=550)
		self.Frame_Main.grid_propagate(False)

		height=self.root.winfo_screenheight()
		width=self.root.winfo_screenwidth()
		height_login=550
		width_login=500
		self.root.geometry(f'{width_login}x{height_login}+{int(width_login/2)}+{int(width_login/2-200)}')
		#crear mainframe
		
		self.Frame_Session()
		self.root.mainloop()

	def conectar(self,event):
		#obj_usuario=usuario()
		try:
			u=self.Entry_User.get()
			c=self.Entry_Contra.get()			
			identificador,usuario=self.obj_usuario.conectar(u,c)
			if identificador==-1:
				messagebox.showerror('Alerta','Datos Incorrectos o el usuario no Existe')
				self.Entry_User.delete(0,'end')
				self.Entry_Contra.delete(0,'end')
				self.Entry_User.focus()
			elif identificador==1:			
				for i in range(0,100,5):				
					self.bar['value']+=5
					self.root.update()
					time.sleep(0.1)				
					if i==100:
						break
				#self.root.withdraw()
				self.root.destroy()
				V_Main.Ventana_Principal(usuario)			

		except Exception as e:
			raise e	
	def Frame_Session(self):
		font_label=('Candara',16,'bold italic')
		self.Frame_Session=Frame(self.Frame_Main,bg='#6D9CA6',highlightbackground="black", highlightthickness=2)
		self.Frame_Session.place(x=5,y=5)		
		self.Frame_Session.config(width=490,height=540)
		self.Frame_Session.grid_propagate(False)
		titulo=Label(self.Frame_Session,text='INICIAR SESIÓN',font=('Comic Sans MS',16,'bold'),fg='white',bg='#6D9CA6')
		titulo.grid(column=0,row=0,columnspan=4,pady=10)	
		
		txt_user=Label(self.Frame_Session,text='Usuario: ',font=font_label,fg='white',bg='#6D9CA6')
		txt_user.grid(row=2,column=0,pady=10)
		self.Entry_User=Entry(self.Frame_Session,width=30)
		self.Entry_User.grid(row=2,column=1,pady=10)
		self.Entry_User.focus()

		txt_contra=Label(self.Frame_Session,text='Contraseña: ', font=font_label,fg='white',bg='#6D9CA6')
		txt_contra.grid(row=3,column=0,pady=15)
		self.Entry_Contra=Entry(self.Frame_Session,show='◘',width=30)
		self.Entry_Contra.bind('<Return>',lambda event:self.conectar(event))
		self.Entry_Contra.grid(row=3,column=1,pady=15)
		
		#Creamoos boton
		self.btn_iniciar=ttk.Button(self.Frame_Session,text='Iniciar',width=20,state='normal',cursor='hand2')
		self.btn_iniciar['command']=self.Frame_Acceso
		self.btn_iniciar.grid(row=5,column=1,columnspan=2,pady=50,sticky="w")
		
		self.btn_cerrar=ttk.Button(self.Frame_Session,text='Cerrar',width=20,state='normal',cursor='hand2')
		self.btn_cerrar.grid(row=5,column=2,pady=50)
		self.btn_cerrar['command']=self.root.quit
	def Frame_Acceso(self):
		self.mainFrame=Frame(self.Frame_Main)
		self.mainFrame.config(bg='#252F61')	
		self.mainFrame.place(x=5,y=5)
		self.mainFrame.config(width=490,height=540)

		my_image = ImageTk.PhotoImage(Image.open("oficina.jpg"))
		my_image = PhotoImage(self.mainFrame, image=my_image)
		my_image.grid(x=0,y=0)		

		Frame_Menues=Frame(self.Frame_Main,bg='#D1E0E3',highlightbackground="white", highlightthickness=2)
		Frame_Menues.config(width=464,height=300)
		Frame_Menues.place(x=17,y=220)
	def llenar_Menues(self):
		pass

Login()


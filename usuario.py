import Consulta_doc
import GUI_User

class usuario(object):
	def __init__(self):
		self.obj_queryUser=Consulta_doc.querys()
		self.conectado=False
		self.obj_user=GUI_User.Usuario()
	def conectar(self,usuario,contra):
		#self.obj_user.set_Password(contra)
		#contrasenia=self.obj_user.Contrasenia
		rows=self.obj_queryUser.query_User(usuario,contra)		
		identificador=-1
		user=""
		
		estado="INACTIVO"		
		if len(rows)!=0:
			identificador=1
			for val in rows:
				user=val.Usuario					
		else:
			identificador=-1
		return identificador,user




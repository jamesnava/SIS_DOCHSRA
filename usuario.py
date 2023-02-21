import Consulta_doc
import GUI_User

class usuario(object):
	def __init__(self):
		self.obj_queryUser=Consulta_doc.querys()
		self.conectado=False
		self.obj_user=GUI_User.Usuario()
	def conectar(self,usuario,contra):		
		rows=self.obj_queryUser.query_User(usuario,contra)		
		identificador=-1
		user=""	
		rol=""	
		estado=""	
		if len(rows)!=0:
			identificador=1
			for val in rows:
				user=val.Usuario
				rol=val.Rol
				estado=val.estado					
		else:
			identificador=-1
		return identificador,user,rol,estado




import conect_bd

class querys(object):
	def __init__(self):
		obj_conectar=conect_bd.Conexion()
		obj_conectar.ejecutar_conn()
		self.cursor=obj_conectar.get_cursor()
	
		
	def query_User(self,usuario,contra):
		rows=[]
		sql=f"""SELECT * FROM USUARIO WHERE Usuario='{usuario}' AND Contrasenia='{contra}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def query_ExistenciaCodigo(self,tabla,codigo,columna):
		rows=[]
		sql=f"""SELECT {columna} FROM {tabla} WHERE {columna}='{codigo}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def query_tablas(self,tabla):
		rows=[]
		sql=f"""SELECT * FROM {tabla}"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows




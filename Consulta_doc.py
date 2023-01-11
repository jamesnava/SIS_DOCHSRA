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
	def query_RetornaCodigo(self,tabla,codigo,columna,retorna):
		rows=[]
		sql=f"""SELECT {retorna} FROM {tabla} WHERE {columna}='{codigo}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def query_tablas(self,tabla):
		rows=[]
		sql=f"""SELECT * FROM {tabla}"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def query_InsertarPedido(self,datos):
		sql=f"""INSERT INTO PEDIDO VALUES('{datos[0]}','{datos[1]}','{datos[2]}','{datos[3]}','{datos[4]}','{datos[5]}','{datos[6]}','{datos[7]}')"""
		self.cursor.execute(sql)
		self.cursor.commit()

	def consulta_2Condiciones(self,tabla,condicion,columnasC):		
		rows=[]
		sql=f"""SELECT * FROM {tabla} WHERE  {columnasC[0]}='{condicion[0]}' AND {columnasC[1]}='{condicion[1]}' AND {columnasC[2]}='{condicion[2]}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def consulta_3Condiciones(self,tabla,condicion,columnasC):
		rows=[]
		sql=f"""SELECT * FROM {tabla} WHERE  {columnasC[0]}='{condicion[0]}' AND {columnasC[1]}='{condicion[1]}' AND {columnasC[2]}='{condicion[2]}' AND {columnasC[3]}='{condicion[3]}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def Insert_Accion(self,datos):
		sql=f"""INSERT INTO ACCION VALUES('{datos[0]}','{datos[1]}','{datos[2]}','{datos[3]}','{datos[4]}','{datos[5]}','{datos[6]}','{datos[7]}')"""
		self.cursor.execute(sql)
		self.cursor.commit()
	def query_OficinaMUser(self,usuario):
		rows=[]
		sql=f"""SELECT * FROM USUARIO AS US INNER JOIN OFICINA AS O ON US.Id_Oficina=O.Id_Oficina AND US.Usuario='{usuario}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def query_Recepcionar(self,idoficina):
		rows=[]
		sql=f"""SELECT A.Cod_Pedido,P.Nro_Pedido,P.Descripcion,P.Tipo,P.Oficina FROM ACCION AS A INNER JOIN
		 PEDIDO AS P ON A.Cod_Pedido=P.cod_Pedido AND A.Id_Oficina='{idoficina}' AND A.Id_Estado=2"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows




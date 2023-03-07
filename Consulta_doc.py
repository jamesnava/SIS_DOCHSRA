import conect_bd

class querys(object):
	def __init__(self):
		obj_conectar=conect_bd.Conexion()
		obj_conectar.ejecutar_conn()
		self.cursor=obj_conectar.get_cursor()
	
		
	def query_User(self,usuario,contra):
		rows=[]
		sql=f"""SELECT USUARIO.Usuario,USUARIO.estado,ROL.Rol FROM USUARIO INNER JOIN ROL ON USUARIO.Id_Rol=ROL.Id_Rol AND Usuario='{usuario}' AND Contrasenia='{contra}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def query_ExistenciaCodigo(self,tabla,codigo,columna):
		rows=[]
		sql=f"""SELECT {columna} FROM {tabla} WHERE {columna}='{codigo}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	#max pedido
	def query_Max(self):
		rows=[]
		sql=f"""SELECT MAX(Nro_Tramite) AS nro FROM PEDIDO WHERE anio=(SELECT YEAR(GETDATE()))"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def query_MaxTable(self,table,retornar):
		rows=[]
		sql=f"""SELECT MAX({retornar}) AS nro FROM {table}"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	#para recepcion
	def Update_TableEstadoAccion(self,codigo,estado):
		sql=f"""UPDATE ACCION SET Id_Estado={estado} WHERE Id_Accion='{codigo}'"""
		self.cursor.execute(sql)
		self.cursor.commit()
	#para derivar o atender o rechazar
	def Update_AccionOtros(self,codigo):
		sql=f"""UPDATE ACCION SET Manejador=1 WHERE Id_Accion='{codigo}'"""
		self.cursor.execute(sql)
		self.cursor.commit()

	def query_Tabla1Condicion(self,tabla,columna,codicion):
		rows=[]
		sql=f"""SELECT * FROM {tabla} WHERE {columna}='{codicion}'"""
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
		sql=f"""INSERT INTO PEDIDO VALUES('{datos[0]}','{datos[1]}','{datos[2]}','{datos[3]}','{datos[4]}','{datos[5]}','{datos[6]}','{datos[7]}','{datos[8]}','{datos[9]}','{datos[10]}','{datos[11]}')"""
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
		sql=f"""INSERT INTO ACCION VALUES('{datos[0]}','{datos[1]}','{datos[2]}','{datos[3]}','{datos[4]}','{datos[5]}','{datos[6]}','{datos[7]}','{datos[8]}',{datos[9]})"""
		self.cursor.execute(sql)
		self.cursor.commit()

	def Insert_Expediente(self,datos):
		sql=f"""INSERT INTO EXPEDIENTE VALUES('{datos[0]}','{datos[1]}','{datos[2]}','{datos[3]}','{datos[4]}')"""
		self.cursor.execute(sql)
		self.cursor.commit()
	def query_OficinaMUser(self,usuario):
		rows=[]
		sql=f"""SELECT * FROM USUARIO AS US INNER JOIN OFICINA AS O ON US.Id_Oficina=O.Id_Oficina AND US.Usuario='{usuario}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def query_DocXEstado(self,idoficina,estado):
		rows=[]
		sql=f"""SELECT A.Id_Accion,A.Cod_Pedido,P.Razon,P.Asunto,P.Nro_Pedido,P.Oficina,A.Observacion,A.Fecha,EX.Nro_Expediente,T.tipo FROM ACCION AS A INNER JOIN
		 PEDIDO AS P ON A.Cod_Pedido=P.cod_Pedido INNER JOIN EXPEDIENTE AS EX ON P.Id_Expediente=EX.Id_Expediente 
		 INNER JOIN Tipo AS T ON T.Id_Tipo=EX.Id_Tipo  AND A.Id_Oficina='{idoficina}' AND A.Id_Estado={estado} AND A.Manejador=0"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def query_PedidoAccion(self,codigoPedido,id_Accion):
		rows=[]
		sql=f"""SELECT A.Id_Accion,A.Cod_Pedido,P.Nro_Pedido,P.Descripcion,P.Tipo,P.Oficina,EX.Nro_Expediente FROM ACCION AS A INNER JOIN
		 PEDIDO AS P ON A.Cod_Pedido=P.cod_Pedido INNER JOIN EXPEDIENTE AS EX ON P.Id_Expediente=EX.Id_Expediente AND A.Cod_Pedido='{codigoPedido}' AND A.Id_Accion={id_Accion}"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def query_tabla(self,tabla):
		rows=[]
		sql=f"""SELECT * FROM {tabla}"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def query_Seguimiento(self,nroPedido,anio,oficina,tipo):
		
		rows=[]
		sql=f"""SELECT P.cod_Pedido,P.Razon,A.Observacion,P.Nro_Pedido,A.Fecha,EX.Nro_Expediente,A.Id_Oficina,E.Estado FROM PEDIDO AS P INNER JOIN ACCION AS A ON P.cod_Pedido=A.Cod_Pedido 
		INNER JOIN EXPEDIENTE AS EX ON P.Id_Expediente=EX.Id_Expediente INNER JOIN OFICINA AS F ON EX.Id_Oficina=F.Id_Oficina INNER JOIN Tipo AS T ON 
 		EX.Id_Tipo=T.Id_Tipo INNER JOIN ESTADO AS E ON A.Id_Estado=E.Id_Estado AND T.tipo='{tipo}' AND F.Oficina='{oficina}' AND EX.Anio='{anio}' AND EX.Nro_Expediente={nroPedido}"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def documentos_EmitidosUpdate(self,Id_estado,Manejador,ASOC_OFICINA):
		rows=[]
		sql=f"""SELECT A.Id_Accion,A.Cod_Pedido,P.Nro_Pedido,P.Razon,P.Asunto,P.Descripcion,O.Oficina,EX.Nro_Expediente,P.Fecha FROM PEDIDO AS P INNER JOIN ACCION AS A
		ON P.cod_Pedido=A.Cod_Pedido INNER JOIN EXPEDIENTE AS EX ON P.Id_Expediente=EX.Id_Expediente INNER JOIN OFICINA AS O ON A.Id_Oficina=O.Id_Oficina AND A.Id_Estado={Id_estado} AND
		 A.Manejador={Manejador} AND A.ASOC_OFICINA='{ASOC_OFICINA}' AND A.Ingreso_nuevo={1}"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def delete_itemINT(self,table,columna,condicion):
		sql=f"""DELETE FROM {table} WHERE {columna}={condicion}"""
		self.cursor.execute(sql)
		self.cursor.commit()

	def delete_itemSTR(self,table,columna,condicion):
		sql=f"""DELETE FROM {table} WHERE {columna}='{condicion}'"""
		self.cursor.execute(sql)
		self.cursor.commit()
	def Update_Pass(self,Usuario,contraA,ContraN):
		rows=[]
		sql=f"""UPDATE USUARIO SET Contrasenia='{ContraN}' WHERE Usuario='{Usuario}' AND Contrasenia='{contraA}'"""
		self.cursor.execute(sql)
		self.cursor.commit()

	def update_Pedido(self,codigo,nroPedido,asunto,razon,descripcion):
		sql=f"""UPDATE PEDIDO SET Nro_Pedido='{nroPedido}',Asunto='{asunto}',Razon='{razon}',Descripcion='{descripcion}' WHERE cod_Pedido='{codigo}'"""
		self.cursor.execute(sql)
		self.cursor.commit()
	def Update_Accion(self,id_accion,Id_oficina):
		sql=f"""UPDATE ACCION SET Id_Oficina='{Id_oficina}' WHERE Id_Accion='{id_accion}'"""
		self.cursor.execute(sql)
		self.cursor.commit()
	def consulta_MaxExpedienteInterno(self,Oficina):
		rows=[]
		sql=f"""SELECT MAX(E.Nro_Expediente) AS nro FROM EXPEDIENTE AS E INNER JOIN Tipo AS T ON E.Id_Tipo=T.Id_Tipo AND E.anio=(SELECT YEAR(GETDATE())) AND ( E.Id_Oficina='{Oficina}' AND T.tipo='INTERNO')"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows

	def consulta_MaxExpedienteExterno(self,Oficina):
		rows=[]
		sql=f"""SELECT MAX(E.Nro_Expediente) AS nro FROM EXPEDIENTE AS E INNER JOIN Tipo AS T ON E.Id_Tipo=T.Id_Tipo AND E.anio=(SELECT YEAR(GETDATE())) AND ( E.Id_Oficina='{Oficina}' AND T.tipo='EXTERNO')"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def consulta_PedidoPdf(self,codigo):
		rows=[]
		sql=f"""SELECT P.*,T.tipo,EX.Nro_Expediente FROM PEDIDO AS P INNER JOIN EXPEDIENTE AS EX 
		ON P.Id_Expediente=EX.Id_Expediente INNER JOIN Tipo AS T ON T.Id_Tipo=EX.Id_Tipo AND P.cod_Pedido='{codigo}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
			
		#rows=self.cursor.fetchall()
		#return rows






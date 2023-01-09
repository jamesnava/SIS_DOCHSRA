import conect_bd

class querys(object):
	def __init__(self):
		obj_conectar=conect_bd.Conexion_Triaje()
		obj_conectar.ejecutar_conn()
		self.cursor=obj_conectar.get_cursor()
	
	def query_Paciente(self,dni):
		rows=[]
		sql=f"""SELECT dni,Nombre,Apellido_Paterno,Apellido_Materno,Telefono FROM PACIENTE WHERE dni='{dni}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	
		
	def query_User(self,usuario,contra):
		rows=[]
		sql=f"""SELECT * FROM USUARIO WHERE Usuario='{usuario}' AND Contrasenia='{contra}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def Insert_Cita(self,usuario,dni,fuente,cupo,n_referencia,medico,consultorio,fecha_Atencion,telefono,establecimiento,continuador,FUA,HCL,turno):
		sql=f"""INSERT INTO TRIAJE VALUES({usuario},'{dni}','{fuente}','{cupo}',{n_referencia},'{medico}','{consultorio}','{fecha_Atencion}','{telefono}','{establecimiento}','{continuador}','{FUA}','{HCL}','{turno}')"""
		self.cursor.execute(sql)
		self.cursor.commit()
	def Eliminar_Cita(self, cupo, fecha, consultorio,medico,turno):
		sql=f"""DELETE FROM TRIAJE WHERE (Nro_Cupo={cupo} AND Fecha_Atencion='{fecha}' AND Especialidad='{consultorio}') AND (Medico='{medico}' AND Turno='{turno}')"""
		self.cursor.execute(sql)
		self.cursor.commit()
	def query_Cupo(self,fecha,consultorio,medico,turno):
		rows=[]
		sql=f"""SELECT Nro_Cupo,dni FROM TRIAJE WHERE (Fecha_Atencion='{fecha}' AND Especialidad='{consultorio}') AND (Medico='{medico}' AND Turno='{turno}')"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def query_UserName(self,usuario):
		rows=[]
		sql=f"""SELECT Id_Usuario FROM USUARIO WHERE Usuario='{usuario}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def delete_Cupo(self,cupo,fecha):
		sql=f"""DELETE FROM TRIAJE WHERE Nro_Cupo='{cupo}' AND Fecha_Atencion='{fecha}'"""
		self.cursor.execute(sql)
		self.cursor.commit()

	def query_CupoNumber(self,fecha,consultorio,cupo,turno,medico):
		rows=[]
		sql=f"""SELECT dni FROM TRIAJE WHERE (Fecha_Atencion='{fecha}' AND Especialidad='{consultorio}' AND Nro_Cupo={cupo}) AND (Turno='{turno}' AND Medico='{medico}')"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def query_AgendadoXUsuario(self,fecha,consultorio,dni):
		rows=[]
		sql=f"""SELECT * FROM TRIAJE WHERE Fecha_Atencion='{fecha}' AND Especialidad='{consultorio}' AND dni={dni}"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def Insert_Paciente(self,datos):
		self.cursor.execute(f"""INSERT INTO PACIENTE VALUES('{datos["dni"]}','{datos["nombres"]}','{datos["apellidoP"]}','{datos["apellidoM"]}','{datos["telefono"]}','{datos["procedencia"]}')""")
		self.cursor.commit()
	def Consulta_DatosPaciente(self):
		rows=[]
		self.cursor.execute(f"""SELECT * FROM PACIENTE""")
		rows=self.cursor.fetchall()
		return rows

	def Consulta_DatosPacienteLIKE(self,dni):
		rows=[]
		self.cursor.execute(f"""SELECT * FROM PACIENTE WHERE dni LIKE '%{dni}%'""")
		rows=self.cursor.fetchall()
		return rows
	def Update_Pacientes(self,dni,nombre,apellidop,apellidom,telefono,procedencia):
		self.cursor.execute(f"""UPDATE PACIENTE SET Nombre='{nombre}',Apellido_Paterno='{apellidop}',Apellido_Materno='{apellidom}',Telefono='{telefono}',Procedencia='{procedencia}' WHERE dni='{dni}'""")
		self.cursor.commit()
	def consulta_Triaje(self,fecha,consultorio,Turno):
		rows=[]
		self.cursor.execute(f"""SELECT * FROM TRIAJE WHERE Fecha_Atencion='{fecha}' AND Especialidad='{consultorio}' AND Turno='{Turno}'""")
		rows=self.cursor.fetchall()
		return rows
	def consulta_TriajeConsultorios(self,fecha):
		rows=[]
		self.cursor.execute(f"""SELECT * FROM TRIAJE WHERE Fecha_Atencion='{fecha}' ORDER BY Especialidad ASC""")
		rows=self.cursor.fetchall()
		return rows
	def consulta_DatosPaciente(self,dni):
		rows=[]		
		self.cursor.execute(f"""SELECT * FROM PACIENTE WHERE dni='{dni}'""")
		rows=self.cursor.fetchall()		
		return rows
	def consulta_Fuente(self):
		rows=[]
		self.cursor.execute("SELECT * FROM FINANCIAMIENTO")
		rows=self.cursor.fetchall()
		return rows
	def consulta_FuenteId(self,name):
		rows=[]
		self.cursor.execute(f"""SELECT * FROM FINANCIAMIENTO WHERE fuente='{name}'""")
		rows=self.cursor.fetchall()
		return rows

	def query_DataTriaje(self,fecha,consultorio,cupo,medico,turno):
		rows=[]
		#sql=f"""SELECT * FROM TRIAJE WHERE Fecha_Atencion='{fecha}' AND Especialidad='{consultorio}' AND Nro_Cupo={cupo}"""
		sql=f"""SELECT * FROM TRIAJE INNER JOIN FINANCIAMIENTO ON TRIAJE.idFuente=FINANCIAMIENTO.idFuente AND (Fecha_Atencion='{fecha}' AND Especialidad='{consultorio}' AND Nro_Cupo={cupo}) AND (Medico='{medico}' AND Turno='{turno}')"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def Consulta_ExistUsuario(self,dni):
		rows=[]
		self.cursor.execute(f"""SELECT * FROM USUARIO WHERE dni='{dni}'""")
		rows=self.cursor.fetchall()
		return rows
	def Consulta_UserExists(self,nombre):
		rows=[]
		sql=f"""SELECT * FROM USUARIO WHERE Usuario='{nombre}'"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def Insert_User(self,dni,usuario,passs,nivel):
		sql=f"""INSERT INTO USUARIO VALUES((SELECT MAX(Id_Usuario)+1 FROM USUARIO),'{dni}','{usuario}','{passs}','{nivel}',GETDATE(),'ACTIVO')"""
		self.cursor.execute(sql)
		self.cursor.commit()
	def Consulta_Usuarios(self):
		rows=[]
		sql=f"""SELECT * FROM USUARIO"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows
	def update_State(self,estado,dni):
		sql=f"""UPDATE USUARIO SET estado='{estado}' WHERE dni='{dni}'"""
		self.cursor.execute(sql)
		self.cursor.commit()
	def change_password(self,passs,dni):
		sql=f"""UPDATE USUARIO SET Clave='{passs}' WHERE dni='{dni}'"""
		self.cursor.execute(sql)
		self.cursor.commit()

	def query_Atenciones(self,dni):
		rows=[]		
		sql=f"""SELECT TOP 10 * FROM TRIAJE INNER JOIN FINANCIAMIENTO ON TRIAJE.idFuente=FINANCIAMIENTO.idFuente AND TRIAJE.dni LIKE '%{dni}%' ORDER BY Fecha_Atencion DESC"""
		self.cursor.execute(sql)
		rows=self.cursor.fetchall()
		return rows


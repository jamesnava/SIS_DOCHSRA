import random
from tkinter import messagebox
def Generar_Codigo():
	letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z','1','2','3','4','5','6','7','8','9','0']
	letra=''
	for i in range(0,5):
		letra+=letras[random.randint(0,len(letras)-1)]
	return letra
def validar_numero(event,campo):
	if not campo.get().isnumeric():
		messagebox.showerror('Alerta','Solo se acepta valores numericos')
		campo.delete(0,'end')



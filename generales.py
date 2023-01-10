import random
def Generar_Codigo():
	letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
	letra=''
	for i in range(0,5):
		letra+=letras[random.randint(0,len(letras)-1)]
	return letra
#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
def funcion_contrasena(no_min,no_ma,no_num,contrasena):

	"""
	Esta funcion crea contraseñas con una combinacion de n números de minusculas, mayusculas y numeros.
	"""
		
	from random import choice
	if no_num>0:
		contrasena=contrasena+str((choice([0,1,2,3,4,5,6,7,8,9])))
	if no_min>0:		
		contrasena=contrasena+choice(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
	if no_ma>0:		
		contrasena=contrasena+str((choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])))
	
	no_min=no_min-1
	no_ma=no_ma-1
	no_num=no_num-1
	if no_min>0 or no_ma>0 or no_num>0:
		contrasena=funcion_contrasena(no_min,no_ma,no_num,contrasena)
	#else:
	#	print "La contraseña es : "+contrasena
	return contrasena	
	

minusculas=int(raw_input("Ingrese el número de minusculas: "))
mayusculas=int(raw_input("Ingrese el número de mayusculas: "))
numeros=int(raw_input("Ingrese el número de números: "))
password=funcion_contrasena(minusculas,mayusculas,numeros,'')
print "La contraseña es: "+password 

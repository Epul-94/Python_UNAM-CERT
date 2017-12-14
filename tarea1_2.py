#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def num_primo (no):
	"""
	Funcion que analiza si el argumento recibido es un número primo
	Regresa un Valor Falso en caso de lo ser un primo, de lo contrario 
	regresa un verdadero
	"""
	for i in range (2,no):
		if no%i==0:
			return False
		elif no in [0,1]:
			return False
		
	return True

numero=int(raw_input("Ingrese un numero: \n"))
if num_primo(numero):
	print "el número "+str(numero)+" es primo"
else:
	print "el número "+str(numero)+" no es primo"

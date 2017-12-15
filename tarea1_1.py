#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def palindromo(palabra,iteracion):
	"""
	Funicion que regresa el palndromo masgrande de la cadena
	"""
	i=0
	if iteracion>1:
		while iteracion+i <= len(palabra):
			palabra1=palabra
			palabra1=palabra[i:iteracion+i]
			comparar=palabra1[::-1]
			if comparar==palabra1:
				return True,palabra1
			i+=1
		pali=palindromo(b,iteracion-1)
	else:
		return False,'No palindromo'
	return pali		
	
	
b=raw_input("Ingresa el texto:")
a,e=palindromo(b,len(b))
if a:
	print e
else:
	print "No es palindromo"
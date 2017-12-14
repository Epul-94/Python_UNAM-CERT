#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

def palindromo(palabra):
  
	comparar=palabra[::-1]
	print comparar
	if comparar==palabra:
		return True
	return False

#print "Ingrese el palindromo"
b=raw_input("Ingresa el texto:")
if palindromo(b):
	print "verdadero"
else:
	print "falso"




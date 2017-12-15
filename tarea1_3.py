#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT


lista=[]

def num_primo (no,no_p):
	"""
	Esta funcion agrega a una lista los n numeros impar que se le indique
	"""
	i=2
	var=0
	no_es=0
	while var==0:
		if no_p%i==0:
			#print "Entro a modulos = 0 con " +str(no_p)+" y " + str(i)
			i=2			
			no_p+=1		
		else:
			#print "No entro al modulo = 0"				
			i+=1			
			if i==no_p:
				break	
				
					
		
	lista.append(no_p)
	#return True
	no=no-1
	no_p+=1
	if no>0:
		num_primo(no,no_p)
	#else:
	#	print str(lista)

	return lista

numero=int(raw_input("Ingrese el número de no. primos que desea: \n"))
listi=num_primo(numero,3)
print "La lista de "+str(numero)+" números primos es: \n" + str(listi)

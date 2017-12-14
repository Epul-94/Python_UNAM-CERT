#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

becarios = []
aprobados = []

def aprueba_becario(nombre_completo,b):
    nombre_completo=nombre_completo.upper()
    #print nombre_completo
    nombre_separado = nombre_completo.split()
    for n in nombre_separado:
        if n in ['GERARDO', 'ALAN', 'GUADALUPE', 'RAFAEL', 'KARINA']:
	    print '\n'+ nombre_completo + ' ESTATUS:'
            return False
    aprobados.append(nombre_completo)
    aprobados.sort()
    print '\n' + aprobados[b] + ' ESTATUS:'
    return True 

def borrar(bec):
#    o=becarios.index(bec)
    for i in becarios:
        if i== bec:
            o=becarios.index(bec)
            print bec+str(o)
            becarios.pop(o)
            return True 
    becarios.sort()
    return False 


becarios = ['Becerra Alvarado Hugo Alonso',
            'Cabrera Balderas Carlos Eduardo',
            'Corona Lopez Gerardo',
            'Diez Gutierrez Gonzalez Rafael',
            'Disner Lopez Marco Antonio',
            'Garcia Romo Claudia FernAnda',
            'Gonzalez Ramirez Miguel Angel',
            'Gonzalez Vargas Andrea Itzel',
            'Orozco Avalos Aline KaRiNa',
            'Palacio Nieto Esteban',
            'Reyes Aldeco Jairo Alan',
            'Santiago Mancera Arturo Samuel',
            'Sarmiento Campos Jose',
            'Sarmiento Campos Maria Guadalupe',
            'Valle Juarez Pedro Angel',
            'Viveros Campos Ulises']
i=0
for b in becarios:
    if aprueba_becario(b,i):
        print '\t\t\t\t APROBADOO'
        i=i+1
    else:
        print '\t\t\t\t REPROBADO'

beca=raw_input("Inserta tu becarios ")
if borrar(beca):
    print "Se borro con éxito"+ beca+ "\n"
    print becarios
else:
    print beca+" no se encuentra en la lista"

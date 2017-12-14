#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice
lista1=[]
lista2=[]
conjunto=set()
calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])
def reprobados():
    for alumno in calificacion_alumno:
        if calificacion_alumno[alumno]>=8:
            #aprobados
            lista1.append(alumno)
        else:
            #reprobados
            lista2.append(alumno)
    tupla2=tuple(lista2)
    tupla1=tuple(lista1)
    return tupla1,tupla2
def promedio():
    n=0
    for alumno in calificacion_alumno:
        n=n+calificacion_alumno[alumno]
    promedio=n/(len(calificacion_alumno))
    return promedio        
def conjuntocal():
    for alumno in calificacion_alumno:
        conjunto.add(calificacion_alumno[alumno])
    return conjunto        

asigna_calificaciones()
imprime_calificaciones()
tup,tup2=reprobados()
prom=promedio()
con=conjuntocal()
print "Aprobados "+ str(tup) 
print "Reprobados "+str(tup2)
print "Promedio : " + str(prom)
print con

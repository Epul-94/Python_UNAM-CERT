#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']

print (lambda w,x,y,z: w+x+y+z)(sistemas,op_interna,incidentes,auditorias)
print filter(lambda nombre: 'i' in nombre,(lambda w,x,y,z: w+x+y+z)(sistemas,op_interna,incidentes,auditorias))
print map (lambda nombre: nombre.upper(),filter(lambda nombre: 'i' in nombre,(lambda w,x,y,z: w+x+y+z)(sistemas,op_interna,incidentes,auditorias)))
print 'separacion'
print (lambda x: ','.join(x))(map (lambda nombre: nombre.upper(),filter(lambda nombre: 'i' in nombre,(lambda w,x,y,z: w+x+y+z)(sistemas,op_interna,incidentes,auditorias))))
#print map (lambda nombre: nombre.upper(),(lambda w,x,y,z: w+x+y+z)#(sistemas,op_interna,incidentes,auditorias))

#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
# 2) filtre la lista resultante para obtener todos los nombres que tienen una "i"
# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION

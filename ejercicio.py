#!/usr/bin/python
#-*- coding: utf-8 -*-

fich=open("/etc/passwd","r")

lineas = fich.readlines()
diccionario = {}

for usuarios in lineas:
	lista = usuarios.split(":")
	login = lista[0]
	shell = lista[-1][0:-1]
	diccionario[login] = shell
#print len(diccionario)
try:
	print ("El terminal que usa el usuario root es:" + diccionario['root'])
	print ("El terminal que usa el usuario imaginario es:" + diccionario['imaginario'])
except KeyError:
	print ("Usuario incorrecto, no se puede mostrar el terminal")


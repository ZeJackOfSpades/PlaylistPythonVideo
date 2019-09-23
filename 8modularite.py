#coding:utf-8
import math
import os
import includes.player8 as player #dans le dossier includes appel de player8.py
"""
Importer un module 	: 	import <nom_module>
										from  <nom_module> import <nom_fonction> # plus besoin du nom du module lors de l'appel
										from  <nom_module> import * # tout importer de <nom_module>
""" 
os.system("clear")
resultat = math.sqrt(100)
print(resultat)

sinus = math.sin(42)
print(sinus)

player.parler("Jack", "coucou le monde")


 
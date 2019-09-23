#coding:utf-8
import pygame

"""
pygame.FULLSCREEN
pygame.RESIZABLE
pygame.NOFRAME

pygame.OPENGL
pygame.HWSURFACE
pygame.DOUBLEBUF

"""
pygame.init() #Initialisation de manière générale

pygame.display.set_caption("Première fenêtre PYGAME") #Titre de la fenêtre
screen		=	pygame.display.set_mode((640,480), pygame.RESIZABLE) #| pygame.NOFRAME)


print(pygame.display.Info()) #information par rapport à la fenêtre
print(pygame.get_sdl_version())
launched	=	True

print(type(screen))

while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched	=	False

#pygame.quit() # ne veux PAS dire fermeture du programme c'est juste pour décharger les anciens widgets
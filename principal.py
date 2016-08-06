import juego
cad= raw_input('Dame el nombre del jugador1: ')
cad2= raw_input('Dame el nombre del jugador2: ')
cad3= raw_input('Jugador1 dame la palabra: ')
x=juego.Juego(cad3,3,cad,cad2)
continuar=2
turno=1
#print x.getIncognita()

while continuar>0:
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	print " ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
	print "                                                       "
	print "                                                       "
	print "                         AHORCADO                      "
	print "                                                       "
	print "                                                       "
	print " ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
	print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
	print "                             |                         "
	print "                             |                         "
	print "                             |                         "
	print "                             |                         "
	print "                             |                         "
	print "                             |                         "
	print "                           ______                      "
	print "                          |      |                     "
	print "                          |      |                     "
	print "                          |      |                     "
	print "                           ______                      "
	print "                             |                         "
	print "                    ________ | _______                 "
	print "                             |                         "
	print "                             |                         "
	print "                             |                         "
	print "                             |                         "
	print "                             |                         "
	print "                             |                         "
	print "                             |                         "
	print "                       |           |                   "
	print "                       |           |                   "
	print "                       |           |                   "
	print "                       |           |                   "
	print "                       |           |                   "
	print "                     __|           |__                 "



	while x.getVidas()>0:
		frasa= raw_input('resolver: si, letra: no ')
		if frasa=='si':
			resol= raw_input('Dame la palabra: ')
			if x.Ganar(resol):
				print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
				print " ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
				print "                                                       "
				print "                                                       "
				print "                         FELICIDADES                   "
				print "                                                       "
				print "                                                       "
				print " ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
				print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
				x.setVidas(x.getVidas()-10)
				if turno==1:
					x.j1S()
					turno=2
				else:
					x.j2S()
					turno=1
			else:
				print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
				print " ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
				print "                                                       "
				print "                                                       "
				print "                         MATADO                        "
				print "                                                       "
				print "                                                       "
				print " ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
				print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
			

		else:	
			fras= raw_input('dame la nueva: ')
			x.comprobar(fras)
			print x.getIncognita()
			print x.getVidas()

	print str(x.j1.getNombre())+': ' +str(x.j1.getPuntos())
	print str(x.j2.getNombre())+': ' +str(x.j2.getPuntos())
	continuar= int(raw_input('pon 1 para continuar y -1 para salir: '))
	if continuar==1:
		x.setVidas(3)
		turno=2
		fras= raw_input('dame la frase nueva: ')
		x.setNueva(fras)

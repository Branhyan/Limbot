from Limbo import *
#ACCIONES:
"""presionar_tecla(tecla, duracion) / moverse_derecha(duracion) / moverse_izquierda(duracion) /saltar(duracion) / bajar(duracion)
/ esperar(duracion) / agarrar(tiempo) / agarrar_y_tirar_iz(duracion) / agarrar_y_tirar_dr(duracion) / sinparar_derecha() /
sinparar_izquierda() / correrderecha_y_saltar(tsalto) / correrizquierda_y_saltar(tsalto) / parar_todo()"""



#COMIENZO DEL JUEGO
comenzar()                                               #Cuenta atrás para el comienzo, para poner el juego
saltar(17)                                               #Como demora en levantarse xD
esperar(0.4)                                             #Le doy tiempo a que se despierte para que no atrase con la animación
print("Al fin se levanta")
correrderecha_y_saltar(18)                               #Corre y salta un pozo
esperar(5)                                               #No para de correr hasta la zona de la caja
#CAJA Y BAJADA
moverse_derecha(2)
agarrar_y_tirar_iz(2.5)                                  #Tira de la caja
saltar(1)                                                #Sube a la caja 
moverse_derecha(0.5)
saltar(0.3)                                              #Sube a la plataforma
correrderecha_y_saltar(2)                                #Corre hasta la piola
parar_todo()                                             #Se queda quieto
bajar(8.5)                                                #Deciende por la piola
moverse_izquierda(2)                                     #Baja la plataforma
correrderecha_y_saltar(1.2)                              #Corre y salta el pozo
esperar(11)                                              #Corre 11 segundos luego del salto
parar_todo()                                             #Se detiene en el barco
#BARCO
esperar(25)
moverse_derecha(0.8)
saltar(0.8)
moverse_derecha(1)
moverse_izquierda(1)
agarrar_y_tirar_dr(8)
saltar(0.5)
moverse_derecha(0.1)
correrderecha_y_saltar(0.1)
correrderecha_y_saltar(2)
parar_todo()
saltar(5)
correrizquierda_y_saltar(0.5)
parar_todo()
saltar(7)
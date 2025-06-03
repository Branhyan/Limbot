
import time # Esto sirve para usar funciones de tiempo
from pynput.keyboard import Key, Controller #Esto importa de la librería pynput funciones para presionar teclas

teclado = Controller() #Define que teclado sirve para controlar las teclas

def comenzar():
    print("Comenzando en 5..")
    time.sleep(1)
    print("4...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("YA!!")

def presionar_tecla(tecla, duracion):   #Esto crea una funcion que según la tecla que pongas y la duración se preciona, pero solo con teclas normales
    teclado.press(tecla)       #Esto es lo que hace la acción de que se presione la tecla
    print(f"Se está precionando la tecla {tecla} por {duracion} segundos")
    time.sleep(duracion) #Esto define la duración de la acción en segundos
    teclado.release(tecla) #Esto hace que la tecla deje de presionarse
    print(f"Se soltó la tecla {tecla}")

def moverse_derecha(duracion):  #Esta función así cómo las siguientes sirven para realizar acciones dentro del juego y hay que especificar el tiempo
    teclado.press(Key.right)
    print(f"Se está moviendo a la derecha por {duracion} segundos ")
    time.sleep(duracion)
    teclado.release(Key.right)
    print("Dejó de ir a la derecha")

def moverse_izquierda(duracion):
    teclado.press(Key.left)
    print(f"Se está moviendo a la izquierda por {duracion} segundos")
    time.sleep(duracion)
    teclado.release(Key.left)
    print("Dejó de ir a la izquierda")

def saltar(duracion): #Un salto estando quieto o muchos dependiendo de la duración
    teclado.press(Key.up)
    print(f"Saltado por {duracion} segundos")
    time.sleep(duracion)
    teclado.release(Key.up)

def bajar(duracion): 
    teclado.press(Key.down)
    print(f"Bajando por {duracion} segundos!")
    time.sleep(duracion)
    teclado.release(Key.down)

def esperar(duracion):
    print(f"Esperando {duracion} segundos...")
    time.sleep(duracion)
    

def agarrar(tiempo):                                                  #Agarrar algo estando quieto
    teclado.press(Key.ctrl)
    print(f"Agarrandose por {tiempo} segundos... ")
    time.sleep(tiempo)
    teclado.release(Key.ctrl)
    

def agarrar_y_tirar_iz(duracion):                                   #Agarrar y tirar a la izquierda
    teclado.press(Key.ctrl)
    time.sleep(0.6)
    teclado.press(Key.left)
    print(f"Tirando a la izquierda por {duracion} segundos. ")
    time.sleep(duracion)
    teclado.release(Key.ctrl)
    teclado.release(Key.left)

def agarrar_y_tirar_dr(duracion):
    teclado.press(Key.ctrl)
    time.sleep(0.6)
    teclado.press(Key.right)
    print(f"Tirando a la derecha por {duracion} segundos. ")
    time.sleep(duracion)
    teclado.release(Key.ctrl)
    teclado.release(Key.right)

def sinparar_derecha():           #Corre sin parar hacia la dirección de la función
    teclado.press(Key.right)
    print("Sin parar a la derecha")

def sinparar_izquierda():
    teclado.press(Key.left)
    print("Sin parar a la izquierda")

def correrderecha_y_saltar(tsalto):                    #Corre sin parar a en la dirección de la función y luego del tiempo da un salto
    teclado.press(Key.right)
    print(f"Sin parar a la derecha esperando salto a los {tsalto} segundos...")
    if tsalto < 3:          #Si es menor a 3 solo hace el salto
         print(f"Salto inminente en {tsalto}") 
         time.sleep(tsalto)
    else:                                  #Sino solo hay una pequeña cuenta regresiva
        time.sleep(tsalto - 3)
        print("Salto en 3...")
        time.sleep(1)
        print("2..")
        time.sleep(1)
        print("1..")
        time.sleep(1)
       
    print("Salto!")
    teclado.press(Key.up)
    time.sleep(0.5)
    teclado.release(Key.up)
    
def correrizquierda_y_saltar(tsalto):
    teclado.press(Key.left)
    print(f"Moviendose a la derecha esperando salto {tsalto} segundos...")
    time.sleep(tsalto)
    teclado.press(Key.up)
    time.sleep(0.5)
    print("Salto!")
    teclado.release(Key.up)

def parar_todo():             #Detiene todos los movimientos
    print("Detente!")
    teclado.release(Key.up)
    teclado.release(Key.down)
    teclado.release(Key.right)
    teclado.release(Key.left)
    teclado.release(Key.ctrl)




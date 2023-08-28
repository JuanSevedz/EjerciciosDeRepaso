from cronometro import Cronometro
import msvcrt  # Librería para detectar la pulsación de teclas en Windows

c = Cronometro()

while True:
    print(c.hora.valor, ':', c.minuto.valor, ':', c.segundo.valor)
    c.avanzar()

    if msvcrt.kbhit() and msvcrt.getch() == b'\r':
        break


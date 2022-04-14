from machine import Pin,UART
from DHT22 import DHT22
import time

uart= UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
dht22 = DHT22(Pin(2,Pin.IN,Pin.PULL_UP))
command=''
file=open("file_dati.txt","a")

print('Inizio funzionamento programma:\r')
print('Campionamento dei dati ogni minuto (premere \'Start\' tramite bluetooth per iniziare un campionamento di 3 secondi)')

while True:
    T, H = dht22.read()
    data='Temp: '+ str(T) +' C and Humid: '+ str(H) +' %\r'
    print(str(data))
    uart.write(str(data)+'\n')
    if uart.any():
        command = uart.readline()
        #print(command)
        if 'start' in command:
            print('Inizio campionamento ogni 3 secondi\r\n')
            uart.write('Inizio campionamento ogni 3 secondi\r\n')
        while "start" in command:
            T,H=dht22.read()
            data='Temp: '+ str(T) +' C and Humid: '+ str(H) +' %\r'
            print(str(data))
            uart.write(str(data)+'\n')
            if uart.any():
                command = uart.readline()
                #print(command)
                if "stop" in command:
                    print('Termine campionamento ogni 3 secondi...\r\n')
                    uart.write('Termine campionamento ogni 3 secondi...\r\n')
                    command=''
                    break
            file.write(data)
            file.flush()    
            time.sleep(3)
            
    file.write(data)
    file.flush()
    time.sleep(60)
    

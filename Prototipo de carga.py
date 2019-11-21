import time
import os
carga=1
punto="."
print("hola")
time.sleep(2)
os.system("cls")
for i in range(0,2):
    while carga!=4:
        os.system("cls")
        print("cargando"+(punto*carga))
        time.sleep(1)
        carga=carga+1
    carga=1
os.system("cls")
print("adios")

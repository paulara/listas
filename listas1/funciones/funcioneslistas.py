"Funcion que hace la lista"
from builtins import int
def crearlista(lista):
    x=int(input("Si desea introducir un valor pulse 1."))
    while x==1:
        try:
            elemento=int(input("Introduzca los componentes de la lista"))
            lista.append(elemento)
        except:
            print("Vuelva a introducir dicho elemento")
            elemento=input("Introduzca los componentes de la lista")
            lista.append(elemento)
        
        x=int(input("Si desea introducir un valor pulse 1."))

"Funcion que imprime los elementos de la lista"   
def recorrerlista(lista): 
    for elemento in lista:
        print(elemento)
"Funcion que separa la lista en tres variables:id_paciente,fase_ensayo,serie_temperaturas"
def dividirtres(lista):
    id_paciente=lista[0:1]
    fase_ensayo=lista[1:2]
    serie_temperaturas=lista[2:]
    print("nombre",id_paciente,"fase",fase_ensayo,"temperatura",serie_temperaturas)
    return id_paciente,fase_ensayo,serie_temperaturas
'Funcion que convierte las temperaturas en flotantes'
def convertirfloat(serie_temperaturas):
    for elemento in range(len(serie_temperaturas)):
        serie_temperaturas[elemento]=float(serie_temperaturas[elemento])
'Funcion que incorpora una temperatura mas'
def anadetemp(lista):
    try:
        temp=int(input("introduzca otra temperatura"))
        lista.append(temp)
    except:
        print("Vuelva a introducir temperatura")
        temp=float(input("Introduzca temperatura"))
        lista.append(temp)
"funcion que anade dos temp"
def dostemp(lista):
    try:
        temp1=int(input("introduzca temp1"))
        temp2=int(input("introduzca temp2"))
    except:
        temp1=float(input("introduzca temp1"))
        temp2=float(input("introduzca temp2"))
    lista.append(temp1)
    lista.append(temp2)
"calcula numero de temp"
def numtemp(lista):
    print("El numero de temperaturas es",len(lista[2:]))
"cadena de texto con comas"
def comas(serie_temperaturas):
    for elemento in range(len(serie_temperaturas)):
        serie_temperaturas[elemento]=str(serie_temperaturas[elemento])
    print(serie_temperaturas)       
"funcion que ordena de mayor a menor"  
def ordena(serie_temperaturas):
    for indice1 in range(len(serie_temperaturas)):
        for indice2 in range(indice1+1,len(serie_temperaturas)):
            if serie_temperaturas[indice1]>serie_temperaturas[indice2]:
                serie_temperaturas[indice1],serie_temperaturas[indice2]=serie_temperaturas[indice2],serie_temperaturas[indice1]
    print(serie_temperaturas)
"funcion que hace la media de las temperaturas" 
def media(serie_temperaturas):
    x=0
    y=0
    for elemento in serie_temperaturas:
        x==(serie_temperaturas[elemento]+x)
        y==(y+1)
    media=x/y
    print(media)
if __name__=="__main__":
    lista=[]
    crearlista(lista)
    recorrerlista(lista)
    id_paciente,fase_ensayo,serie_temperaturas=dividirtres(lista)
    convertirfloat(serie_temperaturas)
    anadetemp(lista)
    recorrerlista(lista)
    dostemp(lista)
    recorrerlista(lista)
    id_paciente,fase_ensayo,serie_temperaturas=dividirtres(lista)
    numtemp(lista)
    comas(serie_temperaturas)
    convertirfloat(serie_temperaturas)
    ordena(serie_temperaturas)
    media(serie_temperaturas)

    
 
    
    
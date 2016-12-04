"Funcion que hace la lista"
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
def convertirfloat(lista):
    serie_temperaturas=float
    return serie_temperaturas
'Funcion que aporta una temperatura mas'
def anadetemp(lista):
    try:
        temp=int(input("introduzca otra temperatura"))
        lista.append(temp)
    except:
        print("Vuelva a introducir temperatura")
        temp=float(input("Introduzca temperatura"))
        lista.append(temp)
if __name__=="__main__":
    lista=[]
    crearlista(lista)
    recorrerlista(lista)
    dividirtres(lista)
    convertirfloat(lista)
    anadetemp(lista)
    recorrerlista(lista)

    
 
    
    
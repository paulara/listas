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
if __name__=="__main__":
    lista=[]
    crearlista(lista)
    recorrerlista(lista)
"Funcion que separa la lista en tres variables:id_paciente,fase_ensayo,serie_temperaturas"
def dividirtres(lista):
    id_paciente=lista[0:1]
    fase_ensayo=lista[1:2]
    serie_temperaturas=lista[2:]
    return id_paciente,fase_ensayo,serie_temperaturas
def convertirfloat(lista):
    serie_temperaturas=float
    return serie_temperaturas
 
    
    
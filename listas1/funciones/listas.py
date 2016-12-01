"Funcion que hace la lista"
def crearlista(lista):
    x=int(input("Si desea introducir un valor pulse 1."))
    while x==1:
        try:
            elemento=int(input("Introduzca los componentes de la lista"))
            lista.append(elemento)
        except:
            elemento=input("Introduzca los componentes de la lista")
            lista.append(elemento)
        finally:
            x=int(input("Si desea introducir un valor pulse 1."))

"Funcion que imprime los elementos de la lista"   
def recorrerlista(lista): 
    for elemento in lista:
        print(elemento)
if __name__=="__main__":
    lista=[]
    crearlista(lista)
    recorrerlista(lista)
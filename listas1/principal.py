"Programa principal de las listas"
from funciones.funcioneslistas import crearlista
from funciones.funcioneslistas import recorrerlista
from funciones.funcioneslistas import dividirtres
from funciones.funcioneslistas import convertirfloat
from funciones.funcioneslistas import anadetemp
from funciones.funcioneslistas import dostemp
from funciones.funcioneslistas import numtemp
from funciones.funcioneslistas import comas
from funciones.funcioneslistas import ordena
from funciones.funcioneslistas import media
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
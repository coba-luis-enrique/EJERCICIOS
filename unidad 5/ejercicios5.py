import re  

path = 'codigoF.js'

try:
    archivo = open(path, 'r')
except:
    print('El archivo que intentas abrir no existe')
    quit()

codigo = ""

for linea in archivo:
    codigo += linea


print("\x1b[1;31m"+"SENTENCIAS DE ASIGNACION") 
regexUno = re.compile('(\w+( |)=( |)[\d+\.\d+|\w]+);')  
resulltado = regexUno.findall(codigo)
for i in resulltado:
    print("\x1b[1;31m"+"sentencia de asignacion:")
    print(i[0])


regexDos = re.compile('(\w+( |)=( |)[\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\d+\.\d+|\w]+);')  
print("\x1b[1;32m"+"OPERACIONES ARITMETICAS BASICAS") 
resulltado = regexDos.findall(codigo)
for i in resulltado:
    print("\x1b[1;32m"+"operaciones aritmeticas basicas:")
    print(i[0])


print("\x1b[1;33m"+"EXPRESIONES BOOLEANAS") 
regexTres = re.compile(
    '([\d+\.\d+|\w]+[ |](\={2,3}|\>|\<|\!|\>=|\<=|\!=)[ |][\d+\.\d+|\w]+)')  
resulltado  = regexTres.findall(codigo)
for i in resulltado:
    print("\x1b[1;33m"+"expresiones booleanas:")
    print(i[0])

print("\x1b[1;34m"+"OPERACIONES AVANZADAS") 
regexCuatro = re.compile(
    '(\w+( |)=( |)[\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\(\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\d+\.\d+|\w]+\));')  # Operaciones Aritmeticas basicas
resulltado = regexCuatro.findall(codigo)
for i in resulltado:
    print("\x1b[1;34m"+"operaciones avanzadas:")
    print(i[0])

print("\x1b[1;35m"+"ESTRUCTURAS DE CONTROL") 
regexCinco = re.compile('([if|for|while|switch|forEach].*[\(]\w.*[\)]){')  
resulltado  = regexCinco.findall(codigo)
for i in resulltado:
    print("\x1b[1;35m"+"estructura de control:")
    print(i[0])


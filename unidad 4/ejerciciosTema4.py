 #libreria de expresiones regulares
import re

path ="javascript.js"

try:
    archivo=open(path, 'r')
except:
    print("El archivo que intentas abrir no existe")
    quit()


codigo = ""

for linea in archivo:
    codigo+=linea
regexUno=re.compile('[a-zA-Z][\w\d]*')
variables=regexUno.findall(codigo)


for i in variables:
    if(i!="console" and i!="log" and i!="let" and i!="var" and i!="const" and i!="push" and i!="pop" and i!="unshift" and i!="shift" and i!="slice" and i!="splice" and i!="reverse" and i!="split" and i!="join" and i!="sort" and i!="indexOf" and i!="findIndex" and i!="find" and i!="new" and i!="Set"
    and i!="of" and i!="forEach" and i!="some" and i!="every" and i!="lenght" and i!="map" and i!="filter" and i!="reduce" and i!="toFixed" and i!="parseInt" and i!="parseFloat"
    and i!="Math.random" and i!="this" and i!="delete" and i!="Object.getPrototypeOf" and i!="Object.assign" and i!="String.prototype" and i!="hasOwnProperty" and i!="legs" and i!="lastIndex" and i!="includes" and i!="startsWith" and i!="endsWith"
    and i!="replace" and i!="substr" and i!="return" and i!="prompt" and i!="alert" and i!="Array" and i!="break" and i!="case" and i!="catch" and i!="class" and i!="default" and i!="do" and i!="else" and i!="elseif"
    and i!="endsswitch" and i!="eval" and i!="extends" and i!="for" and i!="function" and i!="if" and i!="implements" and i!="include" and i!="instanceof" and i!="interface" and  i!="print"
    and i!="private" and i!="protected" and i!="public" and i!="require" and i!="static" and i!="switch" and i!="throw" and i!="try" and i!="use" and i!="while" and i!="true" and i!="false"):
        print("Variables: "+i)

RegexDos=r"\bconsole\b|\blog\b|\blet\b|\bvar\b|\bconst\b|\bpush\b|\bpop\b|\bunshift\b|\bshift\b|\bslice\b|\bsplice\b|\breverse\b|\bsplit\b|\bjoin\b|\bsort\b|\bindexOf\b|\bfindIndex\b|\bfind\b|\bnew\b|\bSet\b|\bof\b|\bforEach\b|\bsome\b|\bevery\b|\blenght\b|\bmap\b|\bfilter\b|\breduce\b|\btoFixed\b|\bparseInt\b|\bparseFloat\b|\bMath.random\b|\bthis\b|\bdelete\b|\bObject.getPrototypeOf\b|\bObject.assign\b|\bString.prototype\b|\bhasOwnProperty\b|\blegs\b|\blastIndex\b|\bincludes\b|\bstartsWith\b|\bendsWith\b|\breplace\b|\bsubstr\b|\breturn\b|\bprompt\b|\balert\b|\bArray\b|\bbreak\b|\bcase\b|\bcatch\b|\bclass\b|\bdefault\b|\bdo\b|\belse\b|\belseif\b|\bendsswitch\b|\beval\b|\bextends\b|\bfor\b|\bfunction\b|\bif\b|\bimplements\b|\binclude\b|\binstanceof\b|\binterface\b|\bprint\b|\bprivate\b|\bprotected\b|\bpublic\b|\brequire\b|\bstatic\b|\bswitch\b|\bthrow\b|\btry\b|\buse\b|\bwhile\b|\btrue\b|\bfalse\b"
palabrasR=re.findall(RegexDos, codigo)
for x in palabrasR:
    print("Palabras reservadas: "+x)

regexTres=re.compile('\d*\.?\d+')
num=regexTres.findall(codigo)
for y in num:
    print("Números: "+ y)

regexCuatro=re.compile('\*\*|--|\+\+|\+=|-=|/=|\%|\+|-|\*|/|=')
operLog=regexCuatro.findall(codigo)
for z in operLog:
    print("Operador aritmético: "+z)


regexCinco=re.compile('<|<=|>|>=|==|!=')
operRac=regexCinco.findall(codigo)
for a in operRac:
    print("Operadores relacionales: "+a)





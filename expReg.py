import os
import re
from pathlib import Path

from tkinter import filedialog
from tkinter import *

ventana= Tk()
def abrir_archivo():
    archivo_abierto=filedialog.askopenfilename(initialdir="/mnt",
        title="Selecciona Archivo",
        filetypes=( ("html","*.htm?"),("todas","*.*") ) )
    return archivo_abierto
    #print(archivo_abierto)

#Button(text="Seleccionar Archivo",bg="pale green",command=abrir_archivo).place(x=10,y=10)

fich=''
fich=abrir_archivo()

print (fich)
if not isinstance(fich,str) :
    exit(66)
#######################################################

estilo="\n<style>" \
  "\ntable {" \
  "\n  font-family: arial, sans-serif;" \
  "\n  border-collapse: collapse;" \
  "\n  width: 100%;}" \
"\ntd, th {" \
"\n  border: 1px solid #dddddd;" \
"\n  text-align: left;"\
"\n  padding: 8px;}"\
"\ntr:nth-child(even) {"\
"\n  background-color: #dddddd;}"\
"\n</style>"

Origen = Path(fich).read_text()

Destino =  open(fich + "_new_.html","w")
# c = open (os.getcwd()+"/datosOr/test2.txt","r")

p = "<li.*?(activity-id-[0-9]{1,3}).*?>.*?(<a href.*?>)(.*?)<\/a><\/li>"
m = re.findall(p, Origen)

print("...INI...")

Destino.write("<html>")
Destino.write("\n<head>")
Destino.write(estilo)
Destino.write("\n</head>")
Destino.write("\n<Body>\n<table>")
Destino.write("\n<tr>")
Destino.write("\n\t<th>&nbsp;</th>")
Destino.write('\n\t<th class="activity-head">Actividad</th>')
Destino.write('\n\t<th class="description-head" >Descripcion</th>')
Destino.write('\n\t<th class="date-Head">Fecha</th>')
Destino.write('\n\t<th class="duration-head">duracion</th>')
Destino.write('\n\t<th claSs="distance-head">Distancia</th>')
Destino.write('\n\t<th class="avg-speed-head">Vel.Media</th>')
Destino.write('\n\t<th class="avg-pace-head">paso km</th>')
Destino.write('\n\t<th class="hr-head">pulsaciones</th>')
Destino.write('\n\t<th class="energy-head">Calorias</th>')
Destino.write('\n\t<th class="cadence-head">cadencia</th>')
Destino.write('\n\t</tr>')


for i in range(0, len(m)):
    g = m[i]
    #p1 = "\n<tr " + g[0] + ">\n\t" + "<td>" + g[1] + g[0] + "</a></td>" + "\n\t" + g[2] + "\n</tr>\n"
    p1 = "\n<tr>\n\t" + "<td>" + g[1] +  "ir</a></td>" + "\n\t" + g[2] + "\n</tr>"
    p1 = p1.replace("<span","\n\t<td")
    p1 = p1.replace("</span>", "</td>")
    p1 = re.sub('<svg.*\/svg>','',p1)
    p1 = p1.replace("</span>", "</td>")
    p = ' activity-icon="2">'
    p1 = re.sub(p,'>Correr',p1)
    p = ' activity-icon="0">'
    p1 = re.sub(p,'>Andar',p1)
    p = ' activity-icon="69">'
    p1 = re.sub(p,'>Aerobico',p1)
    p = ' activity-icon="23">'
    p1 = re.sub(p,'>Pesas',p1)
    p = ' activity-icon="32">'
    p1 = re.sub(p,'>Fitness',p1)
    Destino.write(p1)

Destino.write("\n</table>\n</Body>")
Destino.write("\n</html>")

print("...FIN...")
Destino.close()
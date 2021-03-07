import clsEjercicios
import re
from mimetypes import init
from pathlib import Path
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox as msg
from datetime import date
from datetime import datetime

from meld.misc import select

global Ejercicios
global initDir
initDir = ""
Ejercicios = []




def qEstiloHtm():
    return "\n<style>" \
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

def cabeceraHtm():
    txtRes = "<html>\n<head>" + qEstiloHtm() + "\n</head>" \
    "\n<Body>\n<table>" \
    "\n<tr>" \
    "\n\t<th>&nbsp;</th>" \
    '\n\t<th class="activity-head">Actividad</th>' \
    '\n\t<th class="description-head" >Descripcion</th>' \
    '\n\t<th class="date-Head">Fecha</th>' \
    '\n\t<th class="duration-head">duracion</th>' \
    '\n\t<th claSs="distance-head">Distancia</th>' \
    '\n\t<th class="avg-speed-head">Vel.Media</th>' \
    '\n\t<th class="avg-pace-head">paso km</th>' \
    '\n\t<th class="hr-head">pulsaciones</th>' \
    '\n\t<th class="energy-head">Calorias</th>' \
    '\n\t<th class="cadence-head">cadencia</th>' \
    '\n</tr>'
    return txtRes

def arreglarTagSpan(txtLin):
    txtLin = txtLin.replace("<span", "\n\t<td")
    txtLin = txtLin.replace("</span>", "</td>")
    txtLin = re.sub('<svg.*\/svg>', '', txtLin)
    txtLin = txtLin.replace("</span>", "</td>")
    p = 'activity-icon="2">'
    txtLin = re.sub(p, '>Bici', txtLin)
    p = 'activity-icon="1">'
    txtLin = re.sub(p, '>Correr', txtLin)
    p = 'activity-icon="0">'
    txtLin = re.sub(p, '>Andar', txtLin)
    p = 'activity-icon="69">'
    txtLin = re.sub(p, '>Aerobico', txtLin)
    p = 'activity-icon="23">'
    txtLin = re.sub(p, '>Pesas', txtLin)
    p = 'activity-icon="32">'
    txtLin = re.sub(p, '>Fitness', txtLin)
    return txtLin


def procesar(fichOr):
    fichDst = fichOr[:fichOr.rfind('.')] + datetime.now().strftime('%Y_%m_%d-%H%M%S') + ".html"
    Destino = open(fichDst, "w")
    Origen = Path(fichOr).read_text()
    Destino.write(cabeceraHtm())
        
    # c = open (os.getcwd()+"/datosOr/test2.txt","r")
    p = "<li.*?(activity-id-[0-9]{1,3}).*?>.*?(<a href.*?>)(.*?)<\/a><\/li>"
    m = re.findall(p, Origen)

    for i in range(0, len(m)):
        g = m[i]
        #p1 = "\n<tr " + g[0] + ">\n\t" + "<td>" + g[1] + g[0] + "</a></td>" + "\n\t" + g[2] + "\n</tr>\n"
        p1 = "\n<tr>\n\t" + "<td>" + g[1] +  "ir</a></td>" + "\n\t" + g[2] + "\n</tr>"
        p1 = arreglarTagSpan(p1)
        print(p1)
        Ejercicios.append(clsEjercicios.Ejercicio(p1))
        Destino.write(p1)

    l2 = sorted(Ejercicios)
    Destino.write("\n</table>\n</Body>")
    Destino.write("\n</html>")

    print("...FIN...")
    Destino.close()
    msg.showinfo("Terminado", "Creado Archivo nuevo en ...  \n " + fichDst)

def abrir_archivo():
    global initDir
    msg.showinfo("xxxxxxx","entrando A ELEGIR ARCHIVO")
    archivo_abierto=filedialog.askopenfilename(initialdir=initDir,
        title="Selecciona Archivo",
        filetypes=( ("html","*.htm?"),("todas","*.*") ) )
    if not isinstance(archivo_abierto,str) :
        msg.showinfo("","No ha seleccionado ningun archivo")
    else:
        initDir=archivo_abierto[:archivo_abierto.rfind('/')]
        procesar(archivo_abierto)


#################  CODIGO DE LA APLICACION ######################

if 3 == 1 :
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk

    window = Gtk.Window(title="Hello World")
    window.show()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()

# show an "Open" dialog box and return the path to the selected file
if 3 == 1 :
  Tk().withdraw()
  filename = askopenfilename()
  print(filename)

# we don't want a full GUI, so keep the root window from appearing
# from tkinter.filedialog import askopenfilename

if initDir == "":
    initDir = "/mnt"

ventana = Tk()
Button(text="Seleccionar Archivo", bg="pale green", command=abrir_archivo).place(x=20, y=70)
msg.showinfo(" _- A -_",initDir)
ventana.mainloop()


from shutil import copyfile
from configparser import ConfigParser
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
global fichEjercicios
global EjerciciosNew
global EjerciciosOld
global initDir

fichEjercicios = "Ejercicios.html"
initDir = ""
EjerciciosNew = []
EjerciciosOld = []




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

def finHtm():
    txtRes = "\n</table>\n</Body>"\
             "\n</html>"
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

def LeeEjerciosYaTratados(fichDst):
    EjerciciosOld
    try:
        Destino = Path(fichDst).read_text()
        p = "(<tr.*?\/tr>)"
        mm = re.findall(p, Destino, re.MULTILINE | re.DOTALL)
        for i in range(0, len(mm)):
            p1 = mm[i]
            if p1.find("<td") >= 0:
                EjerciciosOld.append(clsEjercicios.Ejercicio(p1))
    except IOError:
       print ("Archivo {} no encontrado ", fichDst )
    return EjerciciosOld

def procesar(fichOr):
    global EjerciciosNew
    #fichDst = fichOr[:fichOr.rfind('.')] + datetime.now().strftime('%Y_%m_%d-%H%M%S') + ".html"

    # nuevo fichero a tratar
    Origen = Path(fichOr).read_text()

    # ejercicios anteriores ya sacados
    fichDst = fichOr[:fichOr.rfind('/')] + "/SportTracker.html"
    EjerciciosOld2 = LeeEjerciosYaTratados(fichDst)

    # ya tenemos los ejercicios anteriores nos cargamos el fichero antiguo , pero hacemos una copia ;-)
    try:
        copyfile(fichDst, fichDst + "_" + datetime.now().strftime('%Y_%m_%d-%H%M%S') + "_BAK.html")
        print ("Copia de ficheros Tratado realizada ")
    except IOError:
        print(" NO existia fichero de Ejercicos tratados")

    #analizamos el fichero (si cambiara la estructura habria que cambiar este patron
    p = "<li.*?(activity-id-[0-9]{1,3}).*?>.*?(<a href.*?>)(.*?)<\/a><\/li>"
    m = re.findall(p, Origen)
    if len(m) == 0 :
        # estamos abriendo un fichero ya modificado ¿que sentido tiene?
        EjerciciosOld = LeeEjerciosYaTratados(fichOr)
        txt = "No hay Ejercicios Antiguos actualmente "
        if len(EjerciciosOld)>=0 :
            txt = EjerciciosOld[0].tipo + ", " + EjerciciosOld[0].distancia + ", " + EjerciciosOld[0].duracion
        msg.showinfo("¿?", "¿Has seleccionado un archivo ya Tratado? " \
                     + "\n" + str(len(EjerciciosOld)) + " ejercicios encontrados"\
                     + "\nel ultimo es : \n" + txt)
        exit (89)
    else:
        # estamos tratando el fichero recien descargado de la web
        #      hacer:
        #          Entramos en sportTracker
        #            Seleccionamos lista (apareceran los ultimo)
        #            guardamos como hmtl (por ejemplo : "hoy.html")
        #          Iniciamos programa de Python y selecc. fichero "hoy.html"
        #             Leemos nuestro html modificado ya (ejercicios.html)
        #                y nos guardamos los datos en la var EjerciciosOld (array class)
        #             Procesamos "hoy.html" que es el que acabamos de guardar de
        #               SportTracker en ejerciciosNew
        #             Creamos un ejercicios_tmp.html con los EjercicosNew
        #                y que no estan en ejerciciosOld
        #             Terminamos de completar "ejercicios_tmp.html" con
        #                los ejerciciosOld
        #             Finalizamos el ejercicios_tmp.html y lo renombramos
        #                como Ejercicio.html.

        for i in range(0, len(m)):
            g = m[i]
            #p1 = "\n<tr " + g[0] + ">\n\t" + "<td>" + g[1] + g[0] + "</a></td>" + "\n\t" + g[2] + "\n</tr>\n"
            p1 = "\n<tr>\n\t" + "<td>" + g[1] +  "ir</a></td>" + "\n\t" + g[2] + "\n</tr>"
            p1 = arreglarTagSpan(p1)
            ejercicioTemp = clsEjercicios.Ejercicio(p1)
            if ( len(EjerciciosOld2) == 0 )\
                    or\
                    (len(EjerciciosOld2) >= 0 and not ejercicioTemp.esIgual(EjerciciosOld2[0])):
                EjerciciosNew.append(ejercicioTemp) #clsEjercicios.Ejercicio(p1))
            else:
                break

    #fimalmete grabamos los resultados
    Destino = open(fichDst, "w")
    Destino.write(cabeceraHtm())
    for ejercicio in EjerciciosNew:
        Destino.write(ejercicio.dato)
    for ejercicio in EjerciciosOld2:
        Destino.write(ejercicio.dato)
    Destino.write(finHtm())
    Destino.close()

    print("...FIN...")
    print("  probando Ordenar")
    # l2 = sorted(Ejercicios)

    msg.showinfo("Terminado", "Creado Archivo nuevo en ...  \n " + fichDst)

def abrir_archivo():
    global initDir
    parser = ConfigParser()
    parser.read('sportTracker.ini')
    if parser.has_option("DEFAULT","directorio"):
        initDir = parser.get("DEFAULT","directorio")

    ## msg.showinfo("xxxxxxx","entrando A ELEGIR ARCHIVO")
    archivo_abierto=filedialog.askopenfilename(initialdir=initDir,
        title="Selecciona Archivo",
        filetypes=( ("html","*.htm?"),("todas","*.*") ) )
    if not isinstance(archivo_abierto,str) :
        msg.showinfo("","No ha seleccionado ningun archivo")
    else:
        initDir=archivo_abierto[:archivo_abierto.rfind('/')]
        import configparser
        config = configparser.ConfigParser()
        config["DEFAULT"] = {'directorio':initDir}
        with open('sportTracker.ini', 'w') as configfile:
            config.write(configfile)
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
    initDir = "/mnt/u16-datos/python/proyectos/sportTracker/datosOr"



ventana = Tk()
ventana.title("Selecciona Fichero")

Button(text="Seleccionar Archivo", bg="pale green", command=abrir_archivo).place(x=20, y=70)
#msg.showinfo(" _- A -_",initDir)
ventana.mainloop()


from operator import indexOf
from shutil import copyfile
import clsEjercicios
from configparser import ConfigParser
from pathlib import Path
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox as msg
import re
from datetime import datetime
from mimetypes import init
from datetime import date

# 1  from meld.misc import select

global fichEjercicios
global EjerciciosNew
global EjerciciosOld
global initDir
global sepDir  # puede ser "/"  "\" segun estemos en linux o msdos
global newIndice
global nCorrer  # saber el nuemro total de veces de correr
global kmCorrerZapatilla
global kmZapatillas
global kmUso
global mejorTiempo

fichEjercicios = "SportTracker.html"
initDir = ""
EjerciciosNew = []
EjerciciosOld = []
newIndice = 0
kmCorrerZapatilla = 0
kmZapatillas = []
kmUso = {}
mejorTiempo = {}

kmUso["Otros"] = 0
kmUso["Bici"] = 0
kmUso["Andar"] = 0
kmUso["Correr"] = 0
kmUso["Total"] = 0


def qEstiloHtm():
    return "\n<style>" \
           "\ntable {" \
           "\n  font-family: arial, sans-serif;" \
           "\n  border-collapse: collapse;" \
           "\n  width: 100%;" \
           "}" \
           "\ntd, th {" \
           "\n  border: 1px solid #dddddd;" \
           "\n  text-align: left;" \
           "\n  padding: 8px;}" \
           "\ntr:nth-child(even) {" \
           "\n  background-color: #dddddd;}" \
           "\n th { background-color: black;" \
           "\n color: White;}" \
           "</style>"


def cabeceraHtm():
    txtRes = "<html>\n<head>" + qEstiloHtm() + "\n</head>" \
                                               "\n<Body>"
    return txtRes


def resumenEjercicios():
    txtRes = "\n<section id='resumen'>" \
             "<p>&nbsp;\n<table>" \
             "\n<tr>" \
             "\n\t<th class='resumen'>Zapatilla</th>" \
             "\n\t<th class='resumen'>Desde</th>" \
             "\n\t<th class='resumen'>Correr</th>" \
             "\n\t<th class='resumen'>Andar</th>" \
             "\n\t<th class='resumen'>Bici</th>" \
             "\n\t<th class='resumen'>Otros</th>" \
             "\n\t<th class='resumen'>Total</th>" \
             "\n</tr>"

    for a in kmZapatillas:
        txtRes += "\n<tr>" \
                  "\n\t" + a + "" \
                  "\n</tr>"

    txtRes += "\n</table> " \
              "\n</section>"
    return txtRes


def iniTablaHtmEjercicios():
    txtRes = "\n<section id='listado'>" \
             "\n<table>" \
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


def finTablaHtmEjercicios():
    txtRes = "\n</table>" \
             "\n</section>"
    return txtRes


def finHtm():
    txtRes = "\n</Body>" \
             "\n</html>"
    return txtRes


def qTipoEjercicio(txt):
    p = 'activity-icon="2">'
    txt = re.sub(p, '>Bici', txt)
    p = 'activity-icon="1">'
    txt = re.sub(p, '>Correr', txt)
    p = 'activity-icon="0">'
    txt = re.sub(p, '>Andar', txt)
    p = 'activity-icon="69">'
    txt = re.sub(p, '>Aerobico', txt)
    p = 'activity-icon="23">'
    txt = re.sub(p, '>Pesas', txt)
    p = 'activity-icon="32">'
    txt = re.sub(p, '>Fitness', txt)
    return txt


def arreglarTagSpan(txtLin):
    txtLin = txtLin.replace("<span", "\n\t<td")
    txtLin = txtLin.replace("</span>", "</td>")
    txtLin = re.sub('<svg.*\/svg>', '', txtLin)
    txtLin = txtLin.replace("</span>", "</td>")
    txtLin = qTipoEjercicio(txtLin)
    return txtLin


def __estaYa(Ejercicio,EjerciciosLeidos):
    for a in  EjerciciosLeidos:
        if Ejercicio.esIgual(a):
            return TRUE
    return FALSE


def LeeEjerciosYaTratados(fichDst):
    # leemos los ejercicios ya tratados
    EjerciciosOld
    try:
        Destino = Path(fichDst).read_text()
        p = "(<tr.*?\/tr>)"
        mm = re.findall(p, Destino, re.MULTILINE | re.DOTALL)
        for i in range(0, len(mm)):
            p1 = mm[i]

            # if p1.find('class="resumen') < 0  and p1.find('<th') < 0 :
            if not (p1.find('class="resumen') > 0 or p1.find("class='resumen") > 0 or p1.find('<th') > 0):
                if p1.find("<td") >= 0:
                    if not __estaYa(clsEjercicios.Ejercicio(p1, i), EjerciciosOld):
                        EjerciciosOld.append(clsEjercicios.Ejercicio(p1, i))

    except IOError:
        print("Archivo {} no encontrado ", fichDst)
    return EjerciciosOld


def qDirectorio(fich):
    global sepDir
    sepDir = '/'
    res = fich[:fich.rfind('/')]
    if res == '':
        res = fich[:fich.rfind('\\')]
        sepDir = '\\'
    return res


def resumenTiempos():
    global nCorrer

    txtRes = "\n<section id='resumenTiempos'>" \
             "<p>&nbsp;\n<table>" \
             "\n<tr>" \
             "\n\t<th class='resumenTiempos'>KM  (" + format(nCorrer,'0.0f') + ") </th>" \
             "\n\t<th class='resumenTiempos'>mejor</th>" \
             "\n\t<th class='resumenTiempos'>peor</th>" \
             "\n</tr>"


    tiemposOrd = sorted(mejorTiempo.keys())

#newIndice #numero total de ejercicios

    # for km,b in mejorTiempo.items():
    for km in tiemposOrd:
        try:
            porCien = mejorTiempo[km]['veces'] * 100 / nCorrer
            txtRes += "\n<tr>" \
                  "\n\t" \
                  + "<td class='resumenTiempos'>" + format(km,"0.0f") \
                  + "\t(" + format(mejorTiempo[km]['veces'],'0.0f') + " veces, " + format(porCien,'0.0f') + "% )</td>" \
                  + "\n\t<td class='resumenTiempos'>" + format(mejorTiempo[km]['mejor'],'0.2f') + ", " + mejorTiempo[km]["fechaMejor"] + " a " + mejorTiempo[km]["pulsacionesMejor"] + "</td>" \
                  + "\n\t<td class='resumenTiempos'>" + format(mejorTiempo[km]['peor'], "0.2f") \
                        + ", " + mejorTiempo[km]["fechaPeor"] + " a " + mejorTiempo[km]["pulsacionesPeor"] + "</td>" \
                  + "\n</tr>"
        except:
            print(km, mejorTiempo[km])
            txtRes += "\n<tr>" \
                  + "\n\t" \
                  + "<td class='resumenTiempos'>" \
                  + " kkkkmmm = " + str(km) \
                  + "</td>" \
                  + "\n</tr>"


    txtRes += "\n</table> " \
              "\n</section>"
    return txtRes


def qTiempos(km,lpasokm,pulsaciones,fecha):
    global nCorrer


    try:
        lkm=round(float(km[0:-3]))
    except:
        lkm = 0
    try:
        if lpasokm.find(":") >=0 :
            lpasokm = lpasokm.replace(":",".")
        lpasokm = float(lpasokm[0:-3])
    except:
        lpasokm = 0

    kmUso = {}
    if lpasokm > 4.20 and lkm > 4 :
        nCorrer = nCorrer + 1
        try:
            #mejorTiempo[lkm] = mejorTiempo[lkm]
            mejorTiempo[lkm]["veces"] = mejorTiempo[lkm]["veces"] + 1

            if mejorTiempo[lkm]["mejor"] > lpasokm :
                mejorTiempo[lkm]["mejor"] = lpasokm
                mejorTiempo[lkm]["fechaMejor"] = fecha
                mejorTiempo[lkm]["pulsacionesMejor"] = pulsaciones
                #mejorTiempo[lkm] = kmUso

            if mejorTiempo[lkm]["peor"] < lpasokm :
                mejorTiempo[lkm]["peor"] = lpasokm
                mejorTiempo[lkm]["fechaPeor"] = fecha
                mejorTiempo[lkm]["pulsacionesPeor"] = pulsaciones
                #mejorTiempo[lkm] = kmUso


        except:
            kmUso["veces"] = 1
            kmUso["mejor"] = lpasokm
            kmUso["fechaMejor"] = fecha
            kmUso["peor"] = lpasokm
            kmUso["fechaPeor"] = fecha
            kmUso["pulsacionesMejor"] = pulsaciones
            kmUso["pulsacionesPeor"] = pulsaciones
            mejorTiempo[lkm] = kmUso                    # nos aseguramos de que existe




def procesar(fichOr):
    global EjerciciosNew
    global EjerciciosOld
    global nCorrer
    global sepDir
    global newIndice
    global kmCorrerZapatilla

    nCorrer = 0
    newIndice = 0
    EjerciciosNew.clear()
    EjerciciosOld.clear()
    kmCorrerZapatilla = 0
    kmUso["Otros"] = 0
    kmUso["Bici"] = 0
    kmUso["Andar"] = 0
    kmUso["Correr"] = 0
    kmUso["Total"] = 0

    # fichDst = fichOr[:fichOr.rfind('.')] + datetime.now().strftime('%Y_%m_%d-%H%M%S') + ".html"

    # nuevo fichero a tratar, cuando aprenda a leer directamente la pagina se cambiara esto
    Origen = Path(fichOr).read_text()

    # ejercicios anteriores ya sacados (es linux para win cambiar '/' por '\'
    fichDst = qDirectorio(fichOr) + sepDir + fichEjercicios
    # fichDst = fichOr[:fichOr.rfind('/')] + "/SportTracker.html"

    # Leemos el fichero con ejercicios anteriores (fichEjercicios)
    EjerciciosOld = LeeEjerciosYaTratados(fichDst)
    # ya tenemos los ejercicios anteriores como nos cargamos el fichero original hacemos una copia ;-)
    try:
        copyfile(fichDst, fichDst + "_" + datetime.now().strftime('%Y_%m_%d-%H%M%S') + "_BAK_.html")
        print("Copia de ficheros Tratado realizada ")
    except IOError:
        print(" NO existia fichero de Ejercicos tratados")

    # analizamos el fichero (si cambiara la estructura habria que cambiar este patron)
    #  ... maybe TO DO, hacer  un analisis con scrap del HTML y recorer sus elementos
    #  -> basicamente busca <li> ... </li> y ademas cojemos el enlace para ponerlo en una columna
    #  -> para ver la exp. regular :
    #        https://regexper.com
    #        https://regex101.com/
    #
    p = "<li.*?(activity-id-[0-9]{1,3}).*?>.*?(<a href.*?>)(.*?)<\/a><\/li>"
    m = re.findall(p, Origen)
    if len(m) == 0:
        # estamos abriendo un fichero ya modificado ¿que sentido tiene?
        EjerciciosOld = LeeEjerciosYaTratados(fichOr)
        txt = "No se han encontrado Ejercicios en este fichero"
        if len(EjerciciosOld) >= 0:
            txt = EjerciciosOld[0].tipo + ", " + EjerciciosOld[0].distancia + ", " + EjerciciosOld[0].duracion
        msg.showinfo("¿?", "¿Has seleccionado para procesar un archivo ya Tratado? " \
                     + "\n" + str(len(EjerciciosOld)) + " ejercicios encontrados" \
                     + "\nel ultimo es : \n" + txt)
        # exit (89)
    else:
        j = len(EjerciciosOld)
        for i in range(0, len(m)):
            g = m[i]
            # p1 = "\n<tr " + g[0] + ">\n\t" + "<td>" + g[1] + g[0] + "</a></td>" + "\n\t" + g[2] + "\n</tr>\n"
            p1 = "\n<tr>\n\t" + "<td>" + g[1] + "ir</a></td>" + "\n\t" + g[2] + "\n</tr>"
            p1 = arreglarTagSpan(p1)
            ejercicioTemp = clsEjercicios.Ejercicio(p1, j)

            j = j + 1
            if (len(EjerciciosOld) == 0) \
                    or \
                    (len(EjerciciosOld) >= 0 and not ejercicioTemp.esIgual(EjerciciosOld[0])):
                EjerciciosNew.append(ejercicioTemp)  # clsEjercicios.Ejercicio(p1))
            else:
                break

    # fimalmente grabamos los resultados

    kmZapatillas.clear()
    kmCorrerZapatilla = 0
    DatosSalidaEntrenos = ''
    DatosSalidaCabecera = cabeceraHtm()

    DatosSalidaEntrenos = iniTablaHtmEjercicios()

    for ejercicio in EjerciciosNew:
        if ejercicio.fechaOr != '':
            calcularKmZapatilla(ejercicio)
            newIndice += 1
            DatosSalidaEntrenos += ejercicio.escTDEjercicio(newIndice)

    for ejercicio in EjerciciosOld:
        if ejercicio.fechaOr != '':
            calcularKmZapatilla(ejercicio)
            newIndice += 1
            DatosSalidaEntrenos += ejercicio.escTDEjercicio(newIndice)
    DatosSalidaEntrenos += finTablaHtmEjercicios()

    print(resumenTiempos())

    Destino = open(fichDst, "w")

    Destino.write(DatosSalidaCabecera)
    Destino.write(resumenEjercicios())
    Destino.write(resumenTiempos())
    Destino.write(DatosSalidaEntrenos)
    Destino.write(finHtm())

    # if false :  # no se escribe directamente para poder poner el resumen al principio
    #     Destino.write(cabeceraHtm())
    #     Destino.write(secionResumenHtm())
    #     Destino.write(iniTablaHtmEjercicios())
    #     for ejercicio in EjerciciosNew:
    #         #Destino.write(ejercicio.dato)
    #         calcularKmZapatilla(ejercicio)
    #         newIndice += 1
    #         Destino.write(ejercicio.escTDEjercicio(newIndice) )
    #
    #
    #     for ejercicio in EjerciciosOld:
    #         #Destino.write(ejercicio.dato)
    #         calcularKmZapatilla(ejercicio)
    #         newIndice += 1
    #         Destino.write(ejercicio.escTDEjercicio(newIndice) )
    #
    #     Destino.write(finTablaHtmEjercicios())
    #
    #     Destino.write(detalleResumenHtm())
    #
    #     Destino.write(finHtm())

    Destino.close()

    print("...FIN...")
    print("  probando Ordenar")
    # l2 = sorted(Ejercicios)

    msg.showinfo("Terminado", "Creado Archivo nuevo en ...  \n " + fichDst)


def calcularKmZapatilla(ejercicio):
    global kmCorrerZapatilla
    global kmUso

    if ejercicio.tipo == 'Correr' and float(ejercicio.distancia[0:-3]) < 23 and ejercicio.fechaOr != '':
        kmCorrerZapatilla += float(ejercicio.distancia[0:-3])
        kmUso["Correr"] += float(ejercicio.distancia[0:-3])
        qTiempos(ejercicio.distancia, ejercicio.pasoKm, ejercicio.pulsaciones,  ejercicio.fechaOr)

    elif ejercicio.tipo == 'Andar':
        kmUso["Andar"] += float(ejercicio.distancia[0:-3])
    elif ejercicio.tipo == 'Bici':
        kmUso["Bici"] += float(ejercicio.distancia[0:-3])
    else:
        kmUso["Otros"] += float(ejercicio.distancia[0:-3])

    kmUso["Total"] += float(ejercicio.distancia[0:-3])

    des = ejercicio.descripcion
    if des.find("zapatillas nuevas") >= 0 \
            or des.find("zapatilla nueva") >= 0:
        i = des.find("(")
        if i <= 0:
            i = len(des)
        kmUso["desde"] = ejercicio.fechaOr

        # kmZapatillas.append(
        #     des[des.find(":") + 1:i] + ", " + format(kmCorrerZapatilla, "0.2f") + " km, desde " + ejercicio.fechaOr)
        ejercicio.descripcion = des[0:i] + " (" + format(kmCorrerZapatilla, "0.2f") + " km de uso). "

        kmZapatillas.append(
            '<td class="resumen">' + des[des.find(":") + 1:i] + '</td>' \
            '<td class="resumen">' + ejercicio.fechaOr + '</td>' \
            '<td class="resumen">' + format(kmUso["Correr"], "0.2f")  + '</td>' \
            '<td class="resumen">' + format(kmUso["Andar"], "0.2f")  + '</td>' \
            '<td class="resumen">' + format(kmUso["Bici"], "0.2f")  + '</td>' \
            '<td class="resumen">' + format(kmUso["Otros"], "0.2f") + '</td>' \
            '<td class="resumen">' + format(kmUso["Total"], "0.2f") + '</td>')

        kmCorrerZapatilla = 0
        kmUso["Otros"]  = 0
        kmUso["Bici"] = 0
        kmUso["Andar"] = 0
        kmUso["Correr"] = 0
        kmUso["Total"] = 0


def abrir_archivo():
    global initDir
    parser = ConfigParser()
    parser.read('sportTracker.ini')
    if parser.has_option("DEFAULT", "directorio"):
        initDir = parser.get("DEFAULT", "directorio")

    ## msg.showinfo("xxxxxxx","entrando A ELEGIR ARCHIVO")
    archivo_abierto = filedialog.askopenfilename(initialdir=initDir,
                                                 title="Selecciona Archivo",
                                                 filetypes=(("html", "*.htm?"), ("todas", "*.*")))
    if not isinstance(archivo_abierto, str):
        msg.showinfo("", "No ha seleccionado ningun archivo")
    else:
        initDir = archivo_abierto[:archivo_abierto.rfind('/')]
        import configparser
        config = configparser.ConfigParser()
        config["DEFAULT"] = {'directorio': initDir}
        with open('sportTracker.ini', 'w') as configfile:
            config.write(configfile)
        procesar(archivo_abierto)


#################  CODIGO DE LA APLICACION ######################
import tkinter as tk
from tkinter import ttk


class Application(ttk.Frame):

    def __init__(self, main):
        super().__init__(main)
        main.title("Organizar Ejercicios\t")
        main.configure(width=300, height=200)
        self.place(relwidth=1, relheight=1)

        self.entry = ttk.Entry(self)
        self.entry.pack()

        self.button = ttk.Button(self, text="Hola, mundo!")

        button = ttk.Button(self, text='Hola')
        # button.place(x=100, y=100, width=100, height=30)
        # button.place(width=100, height=30)
        # Ignorar esto por el momento.
        button.place(relx=0.01, rely=0.1, relwidth=0.9, relheight=0.2)
        # button.pack(padx=5, pady=5, ipadx=50, ipady=5)
        # button.pack()


if 3 == 1:
    ventana = tk.Tk()
    app = Application(ventana)
    app.mainloop()

    exit(888)

if 3 == 1:
    import gi

    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk

    window = Gtk.Window(title="Hello World")
    window.show()
    window.connect("destroy", Gtk.main_quit)
    Gtk.main()

# show an "Open" dialog box and return the path to the selected file
if 3 == 1:
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)

# we don't want a full GUI, so keep the root window from appearing
# from tkinter.filedialog import askopenfilename

if initDir == "":
    initDir = "/mnt/u16-datos/python/proyectos/sportTracker/datosOr"

ventana = Tk()
ventana.configure(width=300, height=100)
ventana.title("Selecciona Fichero")
# Button(text="Seleccionar Archivo", bg="pale green", command=abrir_archivo).place(x=20, y=70)
# Button(text="Seleccionar Archivo", bg="pale green", command=abrir_archivo).place(relwidth=0.5, relheight=0.5)
Button(text="Seleccionar Archivo", bg="pale green", command=abrir_archivo).place(relx=0.25, rely=0.25)

# msg.showinfo(" _- A -_",initDir)
ventana.mainloop()

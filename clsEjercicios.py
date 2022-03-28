import re
import urllib.request, urllib.error, urllib.parse

# 1 from meld.misc import select


class Ejercicio:
    dato = ''   # el <tr> entero
    indice = 0
    hashDato = ''  #
    url = ''
    descripcion = ''
    tipo = ''     # bici,correr,...
    fecha=''      #guardado como ANYOMESDIA
    fechaOr = ''  # Feb 23, 2020
    duracion = 0   #1:02:12
    distancia = 0
    velMedia = 0
    pasoKm = 0
    pulsaciones = 0
    calorias = 0
    cadencia = 0
    detalleVuelta = ""


    def __cmp__(self, other):
        if int(self.fecha) == int(other.fecha):
            return 1 if self.duracion > other.duracion else -1
        elif int(self.fecha) < int(other.fecha):
            return -1
        else:
            return 1


    def escTDEjercicio(self, newIndice):

          txt = "\n<tr>" \
          + "\n\t<td><a href='" + str(self.url) + "'> Ir </a></td>" \
          + "\n\t<td class='activity-icon'' >" + str(self.tipo) + "</td>" \
          + "\n\t<td class='description' id='" + str(newIndice) + "' >" \
          # if self.indice <= 0:
          #     pass
          # else:
          #     txt = txt + "(" + str(self.indice) + ") "
          txt = txt + str(self.descripcion) + "</td>"
          txt = txt + "\n\t<td class='date' >" + str(self.fechaOr) + "</td>" \
          + "\n\t<td class='duration'>" + str(self.duracion) + "</td>" \
          + "\n\t<td class='distance' >" + str(self.distancia) + "</td>" \
          + "\n\t<td class='avg-pace' >" + str(self.velMedia) + "</td>" \
          + "\n\t<td class='avg-speed'>" + str(self.pasoKm) + "</td>" \
          + "\n\t<td class='hr'>" + str(self.pulsaciones) + "</td>" \
          + "\n\t<td class='energy'>" + str(self.calorias) + "</td>" \
          + "\n\t<td class='cadence'>" + str(self.cadencia) + "</td>" \
          + "\n</tr>"
          return txt


    def toString(self):
        return self.tipo+"-"+self.fecha+"-"+self.duracion


    def esIgual(self, other):
        return (self.dato == other.dato) \
               or (self.tipo == other.tipo
                   and self.fecha == other.fecha
                   and self.duracion == other.duracion
                   and self.distancia == other.distancia)


    # def __init__(self,tr):
    #     self.dato=tr
    #     self._qUrl()
    #     self._qTipo()
    #     self._qDescripcion()
    #     self._qFecha()
    #     self._qDuracion()
    #     self._qDistancia()
    #     self._qVelMedia()
    #     self._qPasoKm()
    #     self._qPulsaciones()
    #     self._qCalorias()
    #     self._qCadencia()


    def __init__(self,tr,i = 0):
        self.dato=tr
        self.indice = i
        self._qUrl()
        self._qTipo()
        self._qDescripcion()
        self._qFecha()
        self._qDuracion()
        self._qDistancia()
        self._qVelMedia()
        self._qPasoKm()
        self._qPulsaciones()
        self._qCalorias()
        self._qCadencia()
        self._qDetalle()
        if self.velMedia.find('/km') >= 0 :
            temp = self.velMedia
            self.velMedia = self.pasoKm
            self.pasoKm = temp

    qDatoL = lambda p, txt: re.search(p, txt)[1]


    def _qDetalle(self):
        self.detalleVuelta = ""  #DetalleEjercicio(self.url).tabla


    def _qDato(self,p ) :
        try :
            res = re.search(p, self.dato)[1]
        except:
            res = ''
        return res


    def _qUrl(self):
        #p = '<td.*?<a href="(.*?)".*?target'
        self.url = self._qDato('<td.*?<a href="(.*?)">.*?')
        if self.url == '':
            self.url = self._qDato("<td.*?<a href='(.*?)'>.*?")
        self.url = self.url
        # try :
        #     self.url = re.search(p,self.dato)[1]
        # except:
        #    self.url = ""


    def _qTipo(self):
        self.tipo = self._qDato('<td.*activity-icon.*?>(.*?)<\/td>')
        # <td class="activity-icon" >Bici</td>
        # p='<td.*activity-icon.*?>(.*?)<\/td>'
        # try:
        #    self.tipo = re.search(p,self.dato)[1]
        # except:
        #    self.tipo = "¿?"

    def _qDescripcion(self):
        #<td class="description" title="">&nbsp;</td>
        self.descripcion = self._qDato('<td.*description.*?>(.*?)<\/td>')
        # p='<td.*description.*?>(.*?)<\/td>'
        # try:
        #    self.descripcion = re.search(p,self.dato)[1]
        # except:
        #    self.descripcion = ""

    def _qFecha(self):
        # '<td class="date">Mar 3, 2021</td>'
        ### p='<td.*date.*?>(.*?)<\/td>'
        p='<td.*date.*?>([a-zA-Z]{3}).*?([0-9]{1,2}).*?([0-9]{4})'
        meses = ['-', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        try:
            b = re.search(p,self.dato)
            mes = meses.index(b[1])
            dia=b[2]
            if int(mes) < 10 : mes = "0" + str(mes)
            if int(dia) < 10 : dia = "0" + str(dia)
            if int(dia) < 10:
                dia=dia.replace('00','0')
            self.fecha = str(b[3]) + str(mes) + str (dia)
            self.fechaOr = b[1] + " " + str (dia) + ", " + b[3]
            self.fecha = str(b[3]) + str(mes) + str(dia)
        except:
            self.fecha = ""
        # self.fecha = re.search(p,self.dato)[1]


    def _qDuracion (self):
        self.duracion = self._qDato('<td.*duration.*?>(.*?)<\/td>')
        # p = '<td.*duration.*?>(.*?)<\/td>'
        # try:
        #    self.duracion = re.search(p,self.dato)[1]
        # except:
        #    self.duracion = ""


    def _qDistancia(self):
        self.distancia = self._qDato('<td.*distance.*?>(.*?)<\/td>')
        # p = '<td.*distance.*?>(.*?)<\/td>'
        # try:
        #     self.distancia = re.search(p,self.dato)[1]
        # except:
        #     self.distancia = ""


    def _qVelMedia(self):
        self.velMedia = self._qDato('<td.*avg-speed.*?>(.*?)<\/td>')
        # p = '<td.*avg-speed.*?>(.*?)<\/td>'
        # try:
        #     self.velMedia = re.search(p,self.dato)[1]
        # except:
        #     self.velMedia = ""


    def _qPasoKm(self):
        self.pasoKm = self._qDato('<td.*avg-pace.*?>(.*?)<\/td>')
        # p = '<td.*avg-pace.*?>(.*?)<\/td>'
        # try:
        #     self.pasoKm = re.search(p,self.dato)[1]
        # except:
        #     self.velMedia = ""


    def _qPulsaciones(self):
        self.pulsaciones = self._qDato("<td.*class=.*hr.*?>(.*?)<\/td>")
        # p = '<td.*"hr".*?>(.*?)<\/td>'
        # try:
        #     self.pulsaciones = re.search(p,self.dato)[1]
        # except:
        #     self.pulsaciones = ""


    def _qCalorias(self):
        self.calorias = self._qDato('<td.*energy.*?>(.*?)<\/td>')
        # p = '<td.*energy.*?>(.*?)<\/td>'
        # try:
        #     self.calorias = re.search(p,self.dato)[1]
        # except:
        #     self.calorias = ""


    def _qCadencia(self):
        self.cadencia = self._qDato('<td.*cadence.*?>(.*?)<\/td>')
        # p = '<td.*cadence.*?>(.*?)<\/td>'
        # try:
        #     self.cadencia = re.search(p,self.dato)[1]
        # except:
        #     self.cadencia = ""


class DetalleEjercicio:
    dato ='' # coresponde a la pagina completa
    tabla = ''  # el objeto formateado con los datos de km-duracio-vel media ....
    km = 0
    duracion = 0
    km_h = 0
    min_km = 0
    pulsaciones = 0

    def __init__(self, url):
       url=url.replace('"', '',8)
       url=url.replace("'", "",8)
       i = url.find(" ")
       if i>0 :
           url= url[0:i]

       # log.debug("Requesting URL: %s" % url)
       # data = urlencode(data).encode('utf8') if data else None
       # try:
       #     response = urlopen(url, data=data, timeout=timeout)

       leerPagina(url)
       if 1==1 :
           try :
               respuesta = urllib.request.urlopen(url)
               self.dato = respuesta.read().decode('utf-8')
               f = open("aaaa.html", 'w')
               f.write(self.dato)
               f.close()

               p = "<li .*</li>"  # '<li.*ng-repeat=.*lap in workout.lapData.*?</li>'
               contenido = self.dato
               mn = re.findall(p, contenido, re.MULTILINE | re.DOTALL)
               print("--------")
               for i in range(0, len(mn)):
                 p1 = mn[i]
                 print(p1)
               print("--------")
           except urllib.error.URLError as e:
               print(e.reason)
       # se supone que cuando consiga leer la puta pagina bien, porque lee pero no se lo que lee
       #  entonces montare la tabla o la estructura <div> o flexbox (habra que recordar com se hacia)
       #   self.tabla = '.... ' que es la que montare en clsEjercicios


def leerPagina(url):
    import httplib2
    from urllib.parse import urlparse
    import os, sys
    parse = urlparse(url)
    if parse.scheme == "http":
        conn = httplib2.HTTPConnectionWithTimeout(parse.netloc, timeout=60)
    else:
        conn = httplib2.HTTPSConnectionWithTimeout(parse.netloc, timeout=60)

    if parse.path == "":
        # Si no disponemos de path le ponemos la barra
        path = "/"
    elif parse.query:
        # Si disponemos de path y query, realizamos el montaje
        path = "%s?%s" % (parse.path, parse.query)
    else:
        # Si solo disponemos de path
        path = parse.path
    # self.conn.putheader("User-agent", 'pywc')
    try:
        conn.request("GET", path)
        response = conn.getresponse()
        print("status: %s" % response.status)
        print("------------------------------------------")
        print("reason: %s" % response.reason)
        print("------------------------------------------")
        print("headers: %s" % response.getheaders())
        print("------------------------------------------")
        print("html: %s" % response.read())
    except:
        print(sys.exc_info()[1])


def download_page(url, maxretries, timeout, pause):
    tries = 0
    htmlpage = None
    while tries < maxretries and htmlpage is None:
        try:
            #with closing(request.urlopen(url, timeout=timeout)) as f:
            sleep(pause)
            htmlpage = f.read()
            sleep(pause)
        except (urlerror.URLError, socket.timeout, socket.error):
            tries += 1
    return htmlpage



import httplib2
from urllib.parse import urlparse
import os,sys
import socket



class html(object):
	def __init__(self):
		pass

# Funcion # que # realiza # la # conexion.
# Tiene  que recibir: la url

def html_connect(self,url):
    socket.setdefaulttimeout(20)
    try:
        parse=urlparse(url)
        if parse.scheme=="http":
            #self.conn=httplib.HTTPConnection(parse.netloc,timeout=60)
            self.conn=httplib2.HTTPConnectionWithTimeout(parse.netloc)
        else:
            #self.conn=httplib.HTTPSConnection(parse.netloc,timeout=60)
            self.conn=httplib2.HTTPSConnectionWithTimeout(parse.netloc)
        if parse.path=="":
            # Si no disponemos de path le ponemos la barra
            path="/"
        elif parse.query:
            # Si disponemos de path y query, realizamos el montaje
            path="%s?%s" % (parse.path,parse.query)
        else:
            # Si solo disponemos de path
            path=parse.path
        self.conn.request("GET",path)
        self.response1=self.conn.getresponse()
        self.status=self.response1.status
        self.reason=self.response1.reason
        self.headers=self.response1.getheaders()
    except socket.error:
        #errno, errstr = sys.exc_info()[:2]
        #if errno == socket.timeout:
            #print "There was a timeout"
        #else:
            #print "There was some other socket error"
        self.status=408
    except:
        self.status=404

# """
# Muestra
# el
# estado
# """


def html_showStatus(self):
    try:
        return self.status, self.reason
    except:
        return ""

#
# Lee
# el
# contenido


def html_read(self):
    self.read1=self.response1.read()

# Muestra el contenido
def html_showHTML(self):
    if self.read1:
        return self.read1
    return ""
# """ Cierra la conexion """
def html_close(self):
    try:
        self.conn.close()
    except:
        pass
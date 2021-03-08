import re

from meld.misc import select


class Ejercicio:
    dato = ''   # el <tr> entero
    hashDato =''  #
    url = ''
    tipo =''  # bici,correr,...
    fecha=''  #guardado como ANYOMESDIA
    fechaOr ='' # Feb 23, 2020
    duracion = 0   #1:02:12
    distancia = 0
    velMedia = 0
    pasoKm = 0
    pulsaciones = 0
    calorias = 0
    cadencia = 0

    def __cmp__(self, other):
        #para hacerlo tengo que cambiar el formato de la fecha y de la duracion o
        # hacer algo para que sean comparables
        if int(self.fecha) == int(other.fecha):
            return 1 if self.duracion > other.duracion else -1
        elif int(self.fecha) < int(other.fecha):
            return -1
        else:
            return 1

    def toString(self):
        return self.tipo+"-"+self.fecha+"-"+self.duracion

    def __init__(self,tr):
        self.dato=tr
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

    def _qUrl(self):
        p = '<td.*?<a href="(.*?)".*?target'
        self.url = re.search(p,self.dato)[1]

    def _qTipo(self):
        #<td class="activity-icon" >Bici</td>
        p='<td.*activity-icon.*?>(.*?)<\/td>'
        self.tipo = re.search(p,self.dato)[1]

    def _qDescripcion(self):
        #<td class="description" title="">&nbsp;</td>
        p='<td.*description.*?>(.*?)<\/td>'
        self.url = re.search(p,self.dato)[1]

    def _qFecha(self):
        # '<td class="date">Mar 3, 2021</td>'
        meses = ['-', 'Jan', 'Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        #p='<td.*date.*?>(.*?)<\/td>'
        p='<td.*date.*?>([a-zA-Z]{3}).*?([0-9]{1,2}). *?([0-9]{4})'
        b = re.search(p,self.dato)

        mes=meses.index(b[1])
        dia=b[2]
        if int(mes) < 10 : mes = "0" + str(mes)
        if int(dia) < 10 : dia = "0" + str(dia)
        self.fecha = str(b[3]) + str(mes) + str (dia)
        self.fechaOr = b[1] + " " + str (dia) + ", " + b[3]
        self.fecha = str(b[3]) + str(mes) + str(dia)
        #self.fecha = re.search(p,self.dato)[1]


    def _qDuracion (self):
        p = '<td.*duration.*?>(.*?)<\/td>'
        self.duracion = re.search(p,self.dato)[1]

    def _qDistancia(self):
        p = '<td.*distance.*?>(.*?)<\/td>'
        self.distancia = re.search(p,self.dato)[1]

    def _qVelMedia(self):
        p = '<td.*avg-speed.*?>(.*?)<\/td>'
        self.velMedia = re.search(p,self.dato)[1]

    def _qPasoKm(self):
        p = '<td.*avg-pace.*?>(.*?)<\/td>'
        self.pasoKm = re.search(p,self.dato)[1]

    def _qPulsaciones(self):
        p = '<td.*"hr".*?>(.*?)<\/td>'
        self.pulsaciones = re.search(p,self.dato)[1]

    def _qCalorias(self):
        p = '<td.*energy.*?>(.*?)<\/td>'
        self.calorias = re.search(p,self.dato)[1]

    def _qCadencia(self):
        p = '<td.*cadence.*?>(.*?)<\/td>'
        self.cadencia = re.search(p,self.dato)[1]

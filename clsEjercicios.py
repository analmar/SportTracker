import re

class Ejercicio:
    dato = ''   # el <tr> entero
    hashDato =''  #
    url = ''
    tipo =''  # bici,correr,...
    fecha=''  #guardado como ANYOMESDIA
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
        if self.fecha == other.fecha:
            return 1 if self.duracion > other.duracion else -1
        elif self.fecha < other.fecha:
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
        p='<td.*activity-icon.*?>(.*?)<\/td>'
        self.tipo = re.search(p,self.dato)[1]

    def _qDescripcion(self):
        p='<td.*description.*?>(.*?)<\/td>'
        self.url = re.search(p,self.dato)[1]

    def _qFecha(self):
        p='<td.*date.*?>(.*?)<\/td>'
        self.fecha = re.search(p,self.dato)[1]

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

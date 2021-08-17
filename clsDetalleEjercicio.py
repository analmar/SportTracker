import re
import urllib.request, urllib.error, urllib.parse

# esta re encuentra los km (si la vuelta esta 1 1km)
#     <li ng-repeat="lap in workout\.lapData.*?</li>
# # abre-paginaweb.py
# import urllib.request, urllib.error, urllib.parse
#
# url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
#
# respuesta = urllib.request.urlopen(url)
# contenidoWeb = respuesta.read()
#
# print(contenidoWeb[0:300])

class clsDetalleEjercicio:
    dato ='' # coresponde a la pagina completa
    km = 0
    duracion = 0
    km-h = 0
    min-km = 0
    pulsaciones = 0

    def __init__(self, url):
       respuesta = urllib.request.urlopen(url)
       contenido = respuesta.read()


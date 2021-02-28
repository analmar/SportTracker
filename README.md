# SportTracker

               <!--
                   activity.id =2   ciclismo
                               =0   andar
                               =1   correr
                               =69  aerobic  
                               =23  pesas  
                               =32  fitness  
                              
               -->
***inentando con regexp.  pero no hay tu tia ***
  
  - 1.separar por grupo todas las <li>..</li>
  - 2.dentro de cada una de ellas ir separando por la clase los distintos atributos
      <span class="date">Nov 12, 2020</span> <span class="duration">00:35:43</span> <span class="distance">0 km
  
    t = Path(os.getcwd()+"/datosOr/test2.txt").read_text()
    f = open (os.getcwd()+"/datosOr/test2.txt","r")
    c= f.read()                         # .replace('\n','')
    p = ".*(Hola.*yfin).*" 
    
***************OPCION A LO BRUTO******************
primero lo ponemos bonito
  reemplazar <!----><li   por   ng<!---->\n<li ng
  reemplazar <span        por   \n\t<span
  reemplazar </li         por   \n</li
  
  esto lo dejara asi (ahora ya vemos la estructura bien)
      <!---->
      <li ng-repeat="wo in filtered | orderBy:orderBy:reverse | limitTo:limit" class="diary-list__workout activity-id-1">
        <a href="https://www.sports-tracker.com/workout/analmar/5fc7d9b29bb20c03419c482d" target="_blank">
        <span class="activity-icon" activity-icon="1"><svg><use xlink:href="#activity-icon-1"></use></svg></span> 
        <span class="description" title="">&nbsp;</span> 
        <span class="date">Dec 2, 2020</span> 
        <span class="duration">00:03:37</span> 
        <span class="distance">0.69 km</span> 
        <span class="avg-speed">11.4 km/h</span> 
        <span class="avg-pace">5:15/km</span> 
        <span class="hr">164 bpm&nbsp;</span> 
        <span class="energy">65 kcal</span> 
        <span class="cadence">0 rpm</span></a>
      </li>
      <!---->
  eliminamos ng-repeat="wo in filtered | orderBy:orderBy:reverse | limitTo:limit" 
  reemplazamos 
    class="diary-list__workout activity-id-1"   por class="activity-id-1"  (clase que podemos crar si queremos)
       (se hace lo mismo con las otras o simpremente se eliminan
         class="diary-list__workout activity-id-*"    por  ''  )
    aunque en realidad todo estto de a continuacion se puede quitar ya que son los dibujos y podemos pasarlo a la descripcion
        <span class="activity-icon" activity-icon="1"><svg><use xlink:href="#activity-icon-1"></use></svg></span> 
        <span class="activity-icon" activity-icon=".*"><svg><use xlink:href="#activity-icon-*"></use></svg></span> 

y despues cada
  cada <li>   por <tr>   </li> por </tr>
  cada <spam por <td   y  cada </spam> por </td>
  
y creamos un <table> .... </table>   que englobe a todo esto

despues con un css podemos ponerlo mas potito

  

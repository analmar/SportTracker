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
  
  - 1.separar por grupo todas las <li>..</li>  (es el paso 1 de a lo brut, supongo que tambien funcionara)
        despues una vez separadas todas las tuplas de <li> ya podriamos para cada una de ellas hacer reemplazar
        
  - 2.dentro de cada una de ellas ir separando por la clase los distintos atributos
      <span class="date">Nov 12, 2020</span> <span class="duration">00:35:43</span> <span class="distance">0 km
  
    t = Path(os.getcwd()+"/datosOr/test2.txt").read_text()
    f = open (os.getcwd()+"/datosOr/test2.txt","r")
    c= f.read()                         # .replace('\n','')
    p = ".*(Hola.*yfin).*" 
    
***************OPCION A LO BRUTO******************
con sublime y regExp en pocos pasos se hace

```
==== PASO 1 ====================== separamos las actividades y ponemos el enlace al principio =============================

<li.*?(activity-id-[0-9]{1,3}).*?>.*?(<a href.*?>)(.*?)<\/a><\/li>
 \n<tr $1>\n\t<td>$2$1</a></td>$3\n</tr>\n

 <!----><li ng-repeat="wo in filtered | orderBy:orderBy:reverse | limitTo:limit" class="diary-list__workout activity-id-2"><a href="https://www.sports-tracker.com/workout/analmar/603b4eccb357342885b873de" target="_blank"><span class="activity-icon" activity-icon="2"><svg><use xlink:href="#activity-icon-2"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 28, 2021</span> <span class="duration">01:48:41</span> <span class="distance">31.92 km</span> <span class="avg-speed">17.6 km/h</span> <span class="avg-pace">3:24/km</span> <span class="hr">0 bpm&nbsp;</span> <span class="energy">1095 kcal</span> <span class="cadence">0 rpm</span></a></li><!---->< li ng-repeat="wo in filtered | orderBy:orderBy:reverse | limitTo:limit" class="diary-list__workout activity-id-0"><a href="https://www.sports-tracker.com/workout/analmar/603a9b911e91b31dd5492533" target="_blank"><span class="activity-icon" activity-icon="0"><svg><use xlink:href="#activity-icon-0"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 27, 2021</span> <span class="duration">01:32:19</span> <span class="distance">6.75 km</span> <span class="avg-speed">4.4 km/h</span> <span class="avg-pace">13:39/km</span> <span class="hr">0 bpm&nbsp;</span> <span class="energy">421 kcal</span> <span class="cadence">0 rpm</span></a></li><!----><li ng-repeat="wo in filtered | orderBy:orderBy:reverse | limitTo:limit" class="diary-list__workout activity-id-2"><a href="https://www.sports-tracker.com/workout/analmar/6039f1c0b12865370fadf82b" target="_blank"><span class="activity-icon" activity-icon="2"><svg><use xlink:href="#activity-icon-2"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 27, 2021</span> <span class="duration">01:36:45</span> <span class="distance">30.07 km</span> <span class="avg-speed">18.6 km/h</span> <span class="avg-pace">3:13/km</span> <span class="hr">0 bpm&nbsp;</span> <span class="energy">1007 kcal</span> <span class="cadence">0 rpm</span></a></li><!----><li ng-repeat="wo in filtered | orderBy:orderBy:reverse | limitTo:limit" class="diary-list__workout activity-id-2"><a href="https://www.sports-tracker.com/workout/analmar/6037d76250cc5169d5b91b64" target="_blank"><span class="activity-icon" activity-icon="2"><svg><use xlink:href="#activity-icon-2"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 25, 2021</span> <span class="duration">00:58:08</span> <span class="distance">20.10 km</span> <span class="avg-speed">20.7 km/h</span> <span class="avg-pace">2:53/km</span> <span class="hr">135 bpm&nbsp;</span> <span class="energy">779 kcal</span> <span class="cadence">0 rpm</span></a></li>

lo convierte en 

!---->
<tr activity-id-2>
	<td><a href="https://www.sports-tracker.com/workout/analmar/603b4eccb357342885b873de" target="_blank">activity-id-2</a></td><span class="activity-icon" activity-icon="2"><svg><use xlink:href="#activity-icon-2"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 28, 2021</span> <span class="duration">01:48:41</span> <span class="distance">31.92 km</span> <span class="avg-speed">17.6 km/h</span> <span class="avg-pace">3:24/km</span> <span class="hr">0 bpm&nbsp;</span> <span class="energy">1095 kcal</span> <span class="cadence">0 rpm</span>
</tr>
<!---->
<tr activity-id-0>
	<td><a href="https://www.sports-tracker.com/workout/analmar/603a9b911e91b31dd5492533" target="_blank">activity-id-0</a></td><span class="activity-icon" activity-icon="0"><svg><use xlink:href="#activity-icon-0"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 27, 2021</span> <span class="duration">01:32:19</span> <span class="distance">6.75 km</span> <span class="avg-speed">4.4 km/h</span> <span class="avg-pace">13:39/km</span> <span class="hr">0 bpm&nbsp;</span> <span class="energy">421 kcal</span> <span class="cadence">0 rpm</span>
</tr>
<!---->
<tr activity-id-2>
	<td><a href="https://www.sports-tracker.com/workout/analmar/6039f1c0b12865370fadf82b" target="_blank">activity-id-2</a></td><span class="activity-icon" activity-icon="2"><svg><use xlink:href="#activity-icon-2"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 27, 2021</span> <span class="duration">01:36:45</span> <span class="distance">30.07 km</span> <span class="avg-speed">18.6 km/h</span> <span class="avg-pace">3:13/km</span> <span class="hr">0 bpm&nbsp;</span> <span class="energy">1007 kcal</span> <span class="cadence">0 rpm</span>
</tr>
<!---->
<tr activity-id-2>
	<td><a href="https://www.sports-tracker.com/workout/analmar/6037d76250cc5169d5b91b64" target="_blank">activity-id-2</a></td><span class="activity-icon" activity-icon="2"><svg><use xlink:href="#activity-icon-2"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 25, 2021</span> <span class="duration">00:58:08</span> <span class="distance">20.10 km</span> <span class="avg-speed">20.7 km/h</span> <span class="avg-pace">2:53/km</span> <span class="hr">135 bpm&nbsp;</span> <span class="energy">779 kcal</span> <span class="cadence">0 rpm</span>
</tr>

==========================   cambiamos los < span> por < td>==================================================

<span(.*?)>(.*?)<\/span>
\n\t<td$1>$2</td>

lo convierte en 

<!---->
<tr activity-id-0>
	<td><a href="https://www.sports-tracker.com/workout/analmar/603a9b911e91b31dd5492533" target="_blank">activity-id-0</a></td>
	<td class="activity-icon" activity-icon="0"><svg><use xlink:href="#activity-icon-0"></use></svg></td> 
	<td class="description" title="">&nbsp;</td> 
	<td class="date">Feb 27, 2021</td> 
	<td class="duration">01:32:19</td> 
	<td class="distance">6.75 km</td> 
	<td class="avg-speed">4.4 km/h</td> 
	<td class="avg-pace">13:39/km</td> 
	<td class="hr">0 bpm&nbsp;</td> 
	<td class="energy">421 kcal</td> 
	<td class="cadence">0 rpm</td>
</tr>
<!---->
<tr activity-id-2>
	<td><a href="https://www.sports-tracker.com/workout/analmar/6039f1c0b12865370fadf82b" target="_blank">activity-id-2</a></td>
	<td class="activity-icon" activity-icon="2"><svg><use xlink:href="#activity-icon-2"></use></svg></td> 
	<td class="description" title="">&nbsp;</td> 
	<td class="date">Feb 27, 2021</td> 
	<td class="duration">01:36:45</td> 
	<td class="distance">30.07 km</td> 
	<td class="avg-speed">18.6 km/h</td> 
	<td class="avg-pace">3:13/km</td> 
	<td class="hr">0 bpm&nbsp;</td> 
	<td class="energy">1007 kcal</td> 
	<td class="cadence">0 rpm</td>
</tr>
<!---->

================= quitamos la moorralla de arriba y la del final =======================

 

<!DOCTYPE html>
<html ><head>
</head>
<body>

<table border=1>
<tr activity-id-2>   <--- ESTA SERIA LA PRIMERA ACTIVIDAD  <----
	<td><a href="httPs://www.sports-tracker.coM/workout/analmar/603b4eccb357342885b873de" target="_blank">activity-id-2</a></td>
	<td class="activity-icon" activity-icon="2">activity-icon-2</td> 
	
...... y la ultima ,,,,	

<tr activity-id-0>
	<td><a href="httPs://www.sports-tracker.coM/workout/analmar/51ee7b8de4b07b2c0aeb1918" target="_blank">activity-id-0</a></td>
	<td class="activity-icon" activity-icon="0">activity-icon-0</td> 
	<td class="description" title="parcela">parcela&nbsp;</td> 
	<td class="date">Apr 26, 2011</td> 
	<td clAss="duraTion">00:03:19</td> 
	<td class="distaNce">0.31 km</td> 
	<td class="avg-speed">5.5 km/h</td> 
	<td class="avg-pace">10:49/km</td> 
	<td class="hr">0 bpm&nbsp;</td> 
	<td class="energy">16 kcal</td> 
	<td class="cadence">0 rpm</td>
</tr>
</table>
</body>
</html>

============= quitamos lo que se ha quedado por medio ===================
<svg.*?(activity-icon-[0-9]{1,3}).*?\/svg>
$1

<tr activity-id-2>
	<td><a href="httPs://www.sports-tracker.coM/workout/analmar/6039f1c0b12865370fadf82b" target="_blank">activity-id-2</a></td>
	<td class="activity-icon" activity-icon="2">activity-icon-2</td> 
	<td class="description" title="">&nbsp;</td> 
	<td class="date">Feb 27, 2021</td> 
	<td class="duration">01:36:45</td> 
	<td claSs="distance">30.07 km</td> 
	<td class="avg-speed">18.6 km/h</td> 
	<td class="avg-pace">3:13/km</td> 
	<td class="hr">0 bpm&nbsp;</td> 
	<td class="energy">1007 kcal</td> 
	<td class="cadence">0 rpm</td>
</tr>

=======================  sustituimos (si queremos) los activity-icon por el texto de la actividad 
activity-icon-xx por el texto
               activity.id =2   ciclismo
                           =0   andar
                           =1   correr
                           =69  aerobic  
                           =23  pesas  
                           =32  fitness  
                           
=================== para terminar ponemor ir en el enlace de la actividad ===============
>(activity-id-[0-9]{1,3})</a>
>ir</a>
```

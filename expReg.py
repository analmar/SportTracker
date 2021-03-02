import os
import re
from pathlib import Path

# txt = Path(os.getcwd()+"/datosOr/test2.txt").read_text()
# f = open (os.getcwd()+"/datosOr/test2.txt","r")

c = '<!----><li ng-repeat="wo in filtered | orderBy:orderBy:reverse | limitTo:limit" class="diary-list__workout activity-id-2"><a href="https://www.sports-tracker.com/workout/analmar/603b4eccb357342885b873de" target="_blank"><span class="activity-icon" activity-icon="2"><svg><use xlink:href="#activity-icon-2"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 28, 2021</span> <span class="duration">01:48:41</span> <span class="distance">31.92 km</span> <span class="avg-speed">17.6 km/h</span> <span class="avg-pace">3:24/km</span> <span class="hr">0 bpm&nbsp;</span> <span class="energy">1095 kcal</span> <span class="cadence">0 rpm</span></a></li><!----><li ng-repeat="wo in filtered | orderBy:orderBy:reverse | limitTo:limit" class="diary-list__workout activity-id-0"><a href="https://www.sports-tracker.com/workout/analmar/603a9b911e91b31dd5492533" target="_blank"><span class="activity-icon" activity-icon="0"><svg><use xlink:href="#activity-icon-0"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 27, 2021</span> <span class="duration">01:32:19</span> <span class="distance">6.75 km</span> <span class="avg-speed">4.4 km/h</span> <span class="avg-pace">13:39/km</span> <span class="hr">0 bpm&nbsp;</span> <span class="energy">421 kcal</span> <span class="cadence">0 rpm</span></a></li><!----><li ng-repeat="wo in filtered | orderBy:orderBy:reverse | limitTo:limit" class="diary-list__workout activity-id-2"><a href="https://www.sports-tracker.com/workout/analmar/6039f1c0b12865370fadf82b" target="_blank"><span class="activity-icon" activity-icon="2"><svg><use xlink:href="#activity-icon-2"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 27, 2021</span> <span class="duration">01:36:45</span> <span class="distance">30.07 km</span> <span class="avg-speed">18.6 km/h</span> <span class="avg-pace">3:13/km</span> <span class="hr">0 bpm&nbsp;</span> <span class="energy">1007 kcal</span> <span class="cadence">0 rpm</span></a></li><!----><li ng-repeat="wo in filtered | orderBy:orderBy:reverse | limitTo:limit" class="diary-list__workout activity-id-2"><a href="https://www.sports-tracker.com/workout/analmar/6037d76250cc5169d5b91b64" target="_blank"><span class="activity-icon" activity-icon="2"><svg><use xlink:href="#activity-icon-2"></use></svg></span> <span class="description" title="">&nbsp;</span> <span class="date">Feb 25, 2021</span> <span class="duration">00:58:08</span> <span class="distance">20.10 km</span> <span class="avg-speed">20.7 km/h</span> <span class="avg-pace">2:53/km</span> <span class="hr">135 bpm&nbsp;</span> <span class="energy">779 kcal</span> <span class="cadence">0 rpm</span></a></li>'
p = "<li.*?(activity-id-[0-9]{1,3}).*?>.*?(<a href.*?>)(.*?)<\/a><\/li>"
m = re.findall(p, c)

print("...INI...")
p2 = ""
for i in range(0, len(m)):
    g = m[i]
    p1 = "\n<tr " + g[0] + ">\n\t" + "<td>" + g[1] + g[0] + "</a></td>" + "\n\t" + g[2] + "\n</tr>\n"
    p = "(.*?)<span(.*?)>(.* ?)<\/span>(.*?)"
    #print(p1)
    m2 = re.findall(p, p1)
    #print(m2)
    for j in range(0, len(m2)):
        g2 = m2[j]
        p2 = p2 + g2[0] + "\n\t<td" + g2[1] + ">" + g2[2] + "</td>" + g2[3]
        print(p2)

    ## p2: str = re.sub(r'<span(. *?)>(.* ?)</span>',"\n\t<td$1>$2</td>",p1)



    # \n < tr $1 >\n\t < td >$2$1 < / a > < / td >$3\n < / tr >\n
    # print(m[i])

print("...FIN...")

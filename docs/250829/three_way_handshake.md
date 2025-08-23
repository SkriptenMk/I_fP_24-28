# Beobachten von Internetverbindungen

Die folgenden Ausführungen basieren auf der Analyse von Netzwerkpaketen,
welch mit Wireshark aufgezeichnet wurden. Dafür ist die Installation von
Wireshark erforderlich. Die 
<a href="https://www.wireshark.org/#download" target="_blank">
Website von Wireshark</a> stellt dazu den
entsprechenden Download zur Verfügung.

## Aufzeichnen von Netzwerkpaketen

Um Netzwerkpakete aufzuzeichnen, wird Wireshark gestartet. Das
Startfenster von Wireshark stellt sich folgendermassen dar:

![Wireshark Startfenster](ws_start_window.png)

Unter dem Titel "Aufzeichnen" kann der gewünschte Netzwerkadapter
ausgewählt und die Aufzeichnung gestartet werden. Die erfassten Pakete
werden in Echtzeit angezeigt und können später analysiert werden. In der
Schule wird die Verbindung zum Internet per WLAN hergestellt.
Entsprechend ist der WLAN-Adapter auszuwählen. Sobald der entsprechende
Adapter ausgewählt ist, kann die Aufzeichnung gestartet werden.
Gestartet wird die Aufzeichnung durch einen Klick auf das blaue
Haifischflossen-Symbol in der Symbolleiste. Die Auszeichnung startet
umgehend. Angehalten wird die Aufzeichnung mit einem Klick auf das
rote Quadrat-Symbol in der Symbolleiste. Die Aufzeichnung kann entweder
über das Menü Datei > Speichern, durch einen Klick auf das Dateisymbol
oder durch die Tastenkombination `Strg + S` gespeichert werden.

## Beobachten der DNS-Anfragen

Um die DNS-Anfragen zu beobachten, wird bei laufender Wireshark
Aufzeichnung eine beliebige Website aufgerufen. Dadurch werden die
entsprechenden DNS-Anfragen erfasst und können in Wireshark
analysiert werden. Nach dem Aufruf der Website kann die Aufzeichnung
angehalten und die erfassten Pakete analysiert werden (wenn die
Aufzeichnung weiterläuft, bewegen sich die Pakete im Anzeigefenster
ständig weiter).

Damit die relevanten Datenpakete angezeigt werden, kann der
aufgezeichnete Datenverkehr gefiltert werden. Der Filter wird in der
Eingabefeld für "Anzeigefilter" eingegeben.

![Wireshark Anzeigefilter](ws_anzeigefilter.png)

Der entsprechende Filter für DNS-Anfragen zu einer gegebenen Website
lautet 

```txt
dns.qry.name == "www.example.com"
```

Sofern die Seite während der Aufzeichnung genau einmal aufgerufen wurde,
wird der Filter zwei Pakete anzeigen: eine DNS-Anfrage und eine
DNS-Antwort.

![Gefilterte Wireshark-Pakete](ws_dns_query.png)

Das Bild zeigt als erstes Paket die DNS-Anfrage für
www.deutschegrammaphon.com und als zweites Paket die entsprechende
Antwort.


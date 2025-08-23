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
oder durch die Tastenkombination Strg + S gespeichert werden.

## Beobachten der DNS-Anfragen

Um DNS-Anfragen zu beobachten, kann Wireshark verwendet werden, um den Netzwerkverkehr zu filtern und die entsprechenden Pakete anzuzeigen. Dazu kann der Filter "dns" in Wireshark eingegeben werden, um nur die DNS-Pakete anzuzeigen. Dies ermöglicht eine detaillierte Analyse der DNS-Anfragen und -Antworten, die zwischen Clients und DNS-Servern ausgetauscht werden.
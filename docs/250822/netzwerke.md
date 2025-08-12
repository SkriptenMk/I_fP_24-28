# Computernetzwerke

Computernetzwerke sind Systeme, die es Computern ermöglichen,
miteinander zu kommunizieren. Ursprünglich ging es tatsächlich nur um
Kommunikation im engeren Sinne, also um den Austausch von
Nachrichten.

Im Laufe der Zeit haben sich Computernetzwerke jedoch stark
weiterentwickelt. Heute ermöglichen sie nicht nur den Austausch von
Nachrichten, sondern auch die gemeinsame Nutzung von Ressourcen wie
Druckern, Dateien oder Internetzugängen. Netzwerke bilden die Grundlage
für viele alltägliche Anwendungen – von E-Mails über Videokonferenzen
bis hin zu Cloud-Diensten. 

Ein Computernetzwerk besteht aus mehreren miteinander verbundenen
Geräten (z.B. Computer, Smartphones, Server), die über verschiedene
Übertragungsmedien wie Kabel oder Funk kommunizieren. Die wichtigsten
Ziele eines Netzwerks sind die effiziente Kommunikation, die Sicherheit
der Datenübertragung und die zuverlässige Verfügbarkeit von
Informationen. 

Um die Kommunikation zu ermöglichen, werden in Netzwerken bestimmte
Regeln und Protokolle verwendet. Das bekannteste Modell zur Beschreibung
dieser Abläufe ist das sogenannte OSI-Schichtenmodell. Es unterteilt die
Netzwerkkommunikation in sieben aufeinander aufbauende Schichten, von
der physischen Übertragung der Daten bis hin zur Anwendungsebene, auf
der Programme wie Webbrowser oder E-Mail-Clients arbeiten. 

## Das OSI- bzw. TCP/IP-Modell

Das OSI-Modell (Open Systems Interconnection Model) ist lediglich ein
Referenzmodell. Trotzdem werden hier die Funktionen der sieben Schichten
dieses Modelles kurz beschrieben. Das Modell hilft, die komplexen
Abläufe der Datenübertragung zu strukturieren und zu verstehen.

Die sieben Schichten des OSI-Modells im Überblick (um Missverständnissen
aufgrund der Übersetzung vorzubeugen, werden hier zur Bezeichnung direkt
die englischen Begriffe verwendet):

1. **Physical Layer:** Überträgt die einzelnen
   Bits als elektrische, optische oder Funk-Signale über das
   Übertragungsmedium (z.B. Kabel, Funk). 
2. **Data Link Layer:** Sorgt für eine fehlerfreie
   Übertragung der Datenpakete zwischen direkt verbundenen Geräten und
   regelt den Zugriff auf das Übertragungsmedium. 
3. **Network Layer:** Ist für die Weiterleitung
   der Datenpakete über mehrere Netzwerke hinweg zuständig (Routing).
   Hier arbeitet z.B. das Internet Protocol (IP). 
4. **Transport Layer:** Gewährleistet die
   fehlerfreie, vollständige und geordnete Übertragung von Daten
   zwischen den Endsystemen. Hier arbeiten Protokolle wie TCP und UDP. 
5. **Session Layer:** Stellt Verbindungen (Sitzungen)
   zwischen Anwendungen her, verwaltet sie und beendet sie wieder. 
6. **Presentation Layer:** Übersetzt Daten
   zwischen dem Netzwerkformat und dem Format der Anwendung, z.B.
   Zeichencodierung oder Verschlüsselung. 
7. **Application Layer:** Stellt die Schnittstelle zu den
   Anwendungsprogrammen bereit, z.B. für E-Mail, Web oder Dateitransfer. 

Das Schichtmodell des OSI-Modells wurde in seiner reinen Form in der
Praxis nicht realisiert. Stattdessen hat sich das TCP/IP-Modell
durchgesetzt (TCP/IP steht für Transmission Control Protocol/Internet
Protocol, die Funktionsweise dieser Protokolle wird später ausführlicher
erläutert).

Im nächsten Schritt lässt sich zeigen, wie diese Schichten im
TCP/IP-Modell zusammengefasst und praktisch umgesetzt werden. 

Das TCP/IP-Modell besteht aus nur vier Schichten: Netzwerkschicht
(Network Access), Internetschicht, Transportschicht und
Anwendungsschicht. Viele Funktionen des OSI-Modells werden im
TCP/IP-Modell in einer einzigen Schicht zusammengefasst. Beispielsweise
entsprechen die unteren 
beiden Schichten des OSI-Modells (Physical Layer und Data Link Layer) der
Netzwerkschicht im TCP/IP-Modell. Die Internetschicht übernimmt die
Aufgaben des Session Layer, während die Transportschicht in beiden
Modellen vergleichbar ist. Die oberen drei OSI-Schichten (Session Layer,
Presentation Layer und Application Layer) werden im TCP/IP-Modell in der
Anwendungsschicht zusammengefasst.

Das TCP/IP-Modell ist heute die Grundlage für die Kommunikation im
Internet und in den meisten Computernetzwerken.

## Analogie zur Kapselung in der objektorientierten Programmierung (OOP)

Das Schichtenmodell in der Netzwerktechnik lässt sich gut mit dem Prinzip der Kapselung in der objektorientierten Programmierung vergleichen. In beiden Fällen werden komplexe Aufgaben in klar abgegrenzte, eigenständige Einheiten (Schichten bzw. Klassen) unterteilt. Jede Schicht im Netzwerkmodell hat eine genau definierte Aufgabe und kommuniziert nur mit der direkt darüber- oder darunterliegenden Schicht – ähnlich wie eine Klasse in der OOP ihre inneren Details verbirgt und nur über definierte Schnittstellen mit anderen Klassen interagiert.

Durch diese Kapselung wird die Komplexität reduziert, Änderungen können leichter vorgenommen werden und die einzelnen Komponenten bleiben unabhängig voneinander wartbar. So wie in der OOP eine Klasse ihre Daten und Methoden kapselt, kapselt im Schichtenmodell jede Ebene die Details ihrer Funktion und stellt nur die notwendigen Dienste für die nächste Schicht bereit.


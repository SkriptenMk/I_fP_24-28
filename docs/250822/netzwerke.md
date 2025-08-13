# Computernetzwerke

Computernetzwerke sind Systeme, die es Computern und anderen Geräten ermöglichen, miteinander zu kommunizieren. Ursprünglich ging es vor allem um den Austausch von Nachrichten. Heute ermöglichen Netzwerke zusätzlich die gemeinsame Nutzung von Ressourcen wie Druckern, Dateien oder Internetzugängen. Sie bilden die Grundlage für viele alltägliche Anwendungen – von E-Mails über Videokonferenzen bis hin zu Cloud-Diensten.

Ein Computernetzwerk besteht aus mehreren miteinander verbundenen Geräten (z. B. Computer, Smartphones, Server), die über verschiedene Übertragungsmedien wie Kabel oder Funk kommunizieren. Wichtige Ziele eines Netzwerks sind:
- effiziente Kommunikation
- zuverlässige Verfügbarkeit von Informationen
- Sicherheit der Datenübertragung (in der Praxis meist durch Verfahren auf höheren Schichten, z. B. Verschlüsselung über TLS)

Um die Kommunikation zu ermöglichen, werden in Netzwerken Regeln und Protokolle verwendet. Ein bekanntes Referenzmodell zur Beschreibung dieser Abläufe ist das OSI-Schichtenmodell. Es unterteilt die Netzwerkkommunikation in sieben aufeinander aufbauende Schichten – von der physischen Übertragung der Daten bis hin zur Anwendungsebene, auf der Programme wie Webbrowser oder E-Mail-Clients arbeiten.

## Das OSI- bzw. TCP/IP-Modell

Das OSI-Modell (Open Systems Interconnection Model) ist ein Referenzmodell. Es hilft, die komplexen Abläufe der Datenübertragung zu strukturieren und zu verstehen. Die sieben Schichten (mit typischen Dateneinheiten, sogenannten PDUs) im Überblick:

1) Physical Layer
- Überträgt einzelne Bits als elektrische, optische oder Funksignale über das Übertragungsmedium (z. B. Kabel, Funk).
- PDU: Bits

2) Data Link Layer
- Sorgt für lokale, rahmenbasierte Übertragung zwischen direkt verbundenen Geräten; regelt den Zugriff auf das Medium (MAC).
- Bietet Fehlererkennung (z. B. CRC) und – je nach Technik – ggf. einfache Fehlerbehandlung/Wiederholungen (z. B. bei WLAN).
- PDU: Frames/Rahmen

3) Network Layer
- Leitet Pakete über mehrere Netzwerke hinweg weiter (Routing); Adressierung auf Netzwerkebene (z. B. IP-Adressen).
- Beispielprotokoll: Internet Protocol (IP).
- PDU: Packets/Pakete

4) Transport Layer
- Stellt Ende-zu-Ende-Transport zwischen Anwendungen bereit. Unterschiedliche Protokolle bieten unterschiedliche Dienste:
  - TCP: zuverlässig, geordnet, verbindungsorientiert; inkl. Fluss- und Staukontrolle.
  - UDP: verbindungslos, ohne Garantie für Zuverlässigkeit oder Reihenfolge.
- PDU: Segmente (TCP) bzw. Datagramme (UDP)

5) Session Layer
- Baut Sitzungen zwischen Anwendungen auf, verwaltet und beendet sie (z. B. Sitzungsverwaltung, Dialogsteuerung).

6) Presentation Layer
- Übersetzt Daten zwischen Darstellungsformaten (z. B. Zeichencodierung, Serialisierung) und kann Daten komprimieren/verschlüsseln.

7) Application Layer
- Stellt die Schnittstelle zu Anwendungsprogrammen und Anwendungsprotokollen bereit (z. B. HTTP, SMTP, DNS).

Das OSI-Schichtenmodell wurde in seiner reinen Form nicht als Protokollstapel umgesetzt. In der Praxis hat sich das TCP/IP-Modell durchgesetzt (TCP = Transmission Control Protocol, IP = Internet Protocol).

Das TCP/IP-Modell besteht aus vier Schichten, die Funktionen des OSI-Modells zusammenfassen:

1) Netzwerkzugangsschicht (Link/Network Access)
- Entspricht OSI Physical + Data Link (Schichten 1 und 2).
- Beispiele: Ethernet, WLAN; MAC-Adressen; Switches arbeiten typischerweise hier.
- PDU: Frames/Rahmen

2) Internetschicht
- Entspricht OSI Network Layer (Schicht 3).
- Beispiele: IP, Routing; Router arbeiten hier; IP-Adressen.
- PDU: Packets/Pakete

3) Transportschicht
- Entspricht OSI Transport Layer (Schicht 4).
- Beispiele: TCP (zuverlässig, geordnet), UDP (verbindungslos); Ports identifizieren Dienste.
- PDU: Segmente (TCP) / Datagramme (UDP)

4) Anwendungsschicht
- Fasst OSI Session, Presentation und Application (Schichten 5–7) zusammen.
- Beispiele: HTTP/HTTPS, SMTP, DNS. Verschlüsselung wie TLS liegt typischerweise oberhalb des Transports und wird Anwendungen zugeordnet.

Das TCP/IP-Modell ist heute die Grundlage für die Kommunikation im Internet und in den meisten Computernetzwerken.

## Analogie zur Kapselung in der objektorientierten Programmierung (OOP)

Das Schichtenmodell in der Netzwerktechnik lässt sich gut mit dem Prinzip der Kapselung in der objektorientierten Programmierung vergleichen. In beiden Fällen werden komplexe Aufgaben in klar abgegrenzte, eigenständige Einheiten (Schichten bzw. Klassen) unterteilt. Jede Schicht im Netzwerkmodell hat eine genau definierte Aufgabe und kommuniziert nur mit der direkt darüber- oder darunterliegenden Schicht – ähnlich wie eine Klasse in der OOP ihre inneren Details verbirgt und nur über definierte Schnittstellen mit anderen Klassen interagiert.

Durch diese Kapselung wird die Komplexität reduziert, Änderungen können leichter vorgenommen werden und die einzelnen Komponenten bleiben unabhängig voneinander wartbar. So wie in der OOP eine Klasse ihre Daten und Methoden kapselt, kapselt im Schichtenmodell jede Ebene die Details ihrer Funktion und stellt nur die notwendigen Dienste für die nächste Schicht bereit.
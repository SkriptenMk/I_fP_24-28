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

### Filtern der Aufzeichnung

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

Der angewendete Filterbefehl ist relativ einfach nachzuvollziehen.
An erster Stelle steht hier das Protokoll nach dem gefiltert wird. Weil
nach den DNS-Anfragen gefiltert wird, ist das hier `dns`. `dns` alleine
wäre bereits ein gültiger Filter. Allerdings werden dann alle DNS-Pakete
angezeigt. Der Filter wird daher zu `dns.qry.name` ergänzt Dabei steht
`qry` als Abkürzung für query - Anfrage. Die Ergänzung `name` steht für den Domain Name,
der Abgefragt wird. `==` ist die logische Verknüpfung, nach der gefiltert wird
und bedeutet hier "ist gleich". Zwischen den Anführungszeichen steht der
String, nach dem gesucht wird.  
Sofern die Seite während der Aufzeichnung genau
einmal aufgerufen wurde, wird der Filter zwei Pakete anzeigen: eine
DNS-Anfrage und eine DNS-Antwort.

![Gefilterte Wireshark-Pakete](ws_dns_query.png)

Das Bild zeigt als erstes Paket die DNS-Anfrage für
www.deutschegrammaphon.com und als zweites Paket die entsprechende
Antwort.

### Analyse der gefilterten Pakete

Für eine genaue Analyse der Kommunikation kann ein einzelnes Paket
durch anklicken ausgewählt werden. Dadurch wird das Paket im unteren
Bereich von Wireshark detailliert angezeigt und kann genauer
untersucht werden.

![Inhalt des Ausgewählten Pakets](ws_selected_package.png)

Dass es sich hier im Bild um die Details des ausgewählten Paketes
handelt, ist an der übereinstimmenden Paketnummer zu erkennen. Die
Zeilen in der 
Detailansicht entsprechen den einzelnen Protokoll-Header-Feldern des
ausgewählten Paketes. Das bildet auch das TCP/IP Schichtenmodell ab.

Die Detailansicht kann durch einen Klick auf die Dreiecke am Anfang der
einzelnen Protokoll-Header-Felder erweitert werden. Dadurch werden
weitere Informationen zu den jeweiligen Feldern angezeigt. Hier werden
jedoch nur die Zusammenfassungen der Header-Felder erläutert.

Im Beispiel wird als erstes der Inhalt des Headers des Internetlayers erläutert. 

```text

Internet Protocol Version 4, Src: 192.168.1.108, Dst: 192.168.1.1

```

In der Zusammenfassung werden die die Quell- und
Ziel-Adressen des IP-Pakets angezeigt. Im vorliegenden Fall sind das jeweils die
Privaten IP-Adressen 192.168.1.108 und 192.168.1.1. 192.168.1.108
ist die Quell-Adresse, erkennbar an der Abkürzung "Src" und 192.168.1.1
die Ziel-Adresse, erkennbar an der Abkürzung "Dst". Beide Geräte
befinden sich damit im gleichen LAN. Der Rechner mit der IP-Adresse
192.168.1.1 ist der Router. Dieses Gerät stellt die Internetverbindung
her und kann DNS-Anfragen aus seinem Cache beantworten.

Im Header für das User Datagram Protocol (UDP) werden die Quell- und
Ziel-Ports angezeigt. 

```text
User Datagram Protocol, Src Port: 53586, Dst Port: 53
```
Der Quellport wurde mit 53586 automatisch und weit oberhalb der sog.
"Well-Known Ports" (0-1023) gewählt. Die "Well-Known Ports" sind Ports,
die von bestimmten Anwendungen oder Diensten standardmässig verwendet
werden. Entsprechend wurde der Zielport auf 53 gewählt, da dies der
standardmässige Port für DNS-Anfragen ist. Eine Liste der "Well-Known Ports"
findet sich in der 
<a
href="https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml"
target="_blank">
offiziellen IANA-Portdatenbank</a>. Der Quellport ermöglicht es dem
Zielsystem, die Antwort an den korrekten Absender zurückzusenden.
[NAT](../250822/nat.md)-Geräte nutzen diese Port-Informationen zusätzlich für die Zuordnung
zwischen privaten und öffentlichen Adressen. 

Im Beispiel werden die Layer 2 (Data Link), Layer 3 (Network) und Layer
4 (Transport) des TCP/IP Schichtenmodells angezeigt. 

```text
Frame 697: 86 bytes on wire (688 bits), 86 bytes captured (688 bits) on interface \Device\NPF_{409C3DA7-1C42-4AAD-97D5-B53FE093890C}, id 0
Ethernet II, Src: Intel_e8:b0:93 (04:56:e5:e8:b0:93), Dst: Arcadyan_a6:82:80 (a0:b5:49:a6:82:80)
Internet Protocol Version 4, Src: 192.168.1.108, Dst: 192.168.1.1
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
    Total Length: 72
    Identification: 0xa19b (41371)
    000. .... = Flags: 0x0
    ...0 0000 0000 0000 = Fragment Offset: 0
    Time to Live: 128
    Protocol: UDP (17)
    Header Checksum: 0x0000 [validation disabled]
    [Header checksum status: Unverified]
    Source Address: 192.168.1.108
    Destination Address: 192.168.1.1
    [Stream index: 9]
User Datagram Protocol, Src Port: 53586, Dst Port: 53
    Source Port: 53586
    Destination Port: 53
    Length: 52
    Checksum: 0x8403 [unverified]
    [Checksum Status: Unverified]
    [Stream index: 6]
    [Stream Packet Number: 1]
    [Timestamps]
    UDP payload (44 bytes)
Domain Name System (query)
    Transaction ID: 0x1f7a
    Flags: 0x0100 Standard query
        0... .... .... .... = Response: Message is a query
        .000 0... .... .... = Opcode: Standard query (0)
        .... ..0. .... .... = Truncated: Message is not truncated
        .... ...1 .... .... = Recursion desired: Do query recursively
        .... .... .0.. .... = Z: reserved (0)
        .... .... ...0 .... = Non-authenticated data: Unacceptable
    Questions: 1
    Answer RRs: 0
    Authority RRs: 0
    Additional RRs: 0
    Queries
        www.deutschegrammophon.com: type A, class IN
            Name: www.deutschegrammophon.com
            [Name Length: 26]
            [Label Count: 3]
            Type: A (1) (Host Address)
            Class: IN (0x0001)
    [Response In: 723]

```

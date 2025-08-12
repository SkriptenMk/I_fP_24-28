# TCP/IP

## IP Adressen

Damit Computer in einem Netzwerk erreichbar sind, benötigen sie eine
eindeutige Adresse. Diese Adresse wird als IP-Adresse (Internet Protocol
Address) bezeichnet. Aktuell - das heisst seit ungefähr zwei Jahrzehnten
\- wird vom IPv4 System auf IPv6 umgestellt.  
IPv4 sind 32-Bit-Adressen, die in vier Oktetten dargestellt werden (z.B.
192.0.2.1). Eine Länge von 32 Bit ergibt 2$^32$, das heisst
4'294'967'296 mögliche Adressen. Das zeigt, dass IPv4-Adressen begrenzt
sind. Diese Begrenztheit hat zur Entwicklung von IPv6 geführt.  
IPv6 Adressen sind 128 Bit lang. Sie werden in Hexadezimaldarstellung
angezeigt, wobei acht Gruppen von vier hexadezimalen Ziffern (z.B.
2001:0db8:85a3:0000:0000:8a2e:0370:7334) verwendet werden. Die Länge von
128 Bit ermöglicht 2$^128$ Adressen, was in dezimaler Schreibweise einer
Zahl mit 39 Stellen entspricht.

## DNS Lookup

Menschen können sich IP-Adressen nur schwer merken. Daher wurden
Domainnamen eingeführt, die leichter zu erinnern sind. Ein Beispiel für
eine so dargestellte Adresse ist www.google.com. Eine dazugehörige
IP-Adresse ist 172.217.168.68. Für die Zuweisung einer IP-Adresse zu
einem Domainnamen ist das Domain Name System (DNS) verantwortlich.

### Funktionsweise

1. **Anfrage:** Wenn ein Benutzer eine Website besucht, sendet der Browser eine DNS-Anfrage an einen DNS-Server, um die IP-Adresse der gewünschten Domain zu ermitteln.
2. **Auflösung:** Der DNS-Server überprüft seinen Cache auf eine vorhandene Zuordnung. Wenn keine Zuordnung gefunden wird, leitet der Server die Anfrage an andere DNS-Server weiter, bis die IP-Adresse ermittelt wird.
3. **Antwort:** Der DNS-Server sendet die gefundene IP-Adresse zurück an den Browser, der dann eine Verbindung zur Website herstellen kann.

### Typen von DNS-Einträgen

- **A-Record:** Verknüpft einen Domainnamen mit einer IPv4-Adresse.
- **AAAA-Record:** Verknüpft einen Domainnamen mit einer IPv6-Adresse.
- **CNAME-Record:** Alias für einen anderen Domainnamen.
- **MX-Record:** Gibt den Mailserver für eine Domain an.

### Bedeutung

Der DNS ist entscheidend für die Benutzerfreundlichkeit des Internets, da er es ermöglicht, Websites über leicht merkbare Namen anstelle von numerischen IP-Adressen zu erreichen. Ohne DNS müssten Benutzer die IP-Adressen aller Websites kennen, die sie besuchen möchten.
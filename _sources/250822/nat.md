# Network Address Translation (NAT)

## Was ist NAT?

Network Address Translation (NAT) ist ein Verfahren zur automatischen und transparenten Übersetzung von IP-Adressen in Datenpaketen. NAT ermöglicht es, dass mehrere Geräte in einem privaten Netzwerk über eine einzige öffentliche IP-Adresse mit dem Internet kommunizieren können. Diese Technik wurde entwickelt, um die Knappheit von IPv4-Adressen zu bewältigen und gleichzeitig die Sicherheit privater Netzwerke zu erhöhen.

In der Praxis bedeutet dies: Wenn Sie zu Hause mehrere Geräte (Laptop, Smartphone, Smart-TV) mit dem Internet verbinden, teilen sich alle diese Geräte eine einzige öffentliche IP-Adresse, die Ihnen von Ihrem Internetanbieter zugewiesen wurde.

## Funktionsweise von NAT

### Grundprinzip

NAT arbeitet auf der Schicht 3 des OSI-Modells und ändert die Adressen im IP-Header von Datenpaketen. Der Prozess läuft folgendermassen ab:

1. **Ausgehende Verbindung:** Ein Gerät im privaten Netzwerk (z.B. 192.168.1.10) sendet eine Anfrage an einen Server im Internet.
2. **Adressübersetzung:** Der NAT-Router ersetzt die private Quell-IP-Adresse durch seine öffentliche IP-Adresse (z.B. 203.0.113.5).
3. **Tabelleneintrag:** Der Router speichert die Zuordnung in einer NAT-Tabelle.
4. **Antwort:** Wenn der Server antwortet, verwendet der Router die NAT-Tabelle, um die Antwort an das richtige Gerät im privaten Netzwerk weiterzuleiten.

### NAT-Tabelle

Die NAT-Tabelle ist das Herzstück des Verfahrens. Sie enthält folgende Informationen:

- **Private IP-Adresse** (z.B. 192.168.1.10)
- **Privater Port** (z.B. 54321)
- **Öffentliche IP-Adresse** (z.B. 203.0.113.5)
- **Öffentlicher Port** (z.B. 12345)
- **Ziel-IP-Adresse** (z.B. 93.184.216.34)
- **Ziel-Port** (z.B. 80)

## Private IP-Adressbereiche

Für private Netzwerke sind spezielle IP-Adressbereiche reserviert, die nicht im öffentlichen Internet geroutet werden:

- **10.0.0.0 bis 10.255.255.255** (10.0.0.0/8) – 16'777'216 Adressen
- **172.16.0.0 bis 172.31.255.255** (172.16.0.0/12) – 1'048'576 Adressen  
- **192.168.0.0 bis 192.168.255.255** (192.168.0.0/16) – 65'536 Adressen

Diese Bereiche können in privaten Netzwerken beliebig oft wiederverwendet werden, da sie nur lokal gültig sind.

## Arten von NAT

### 1. Static NAT (One-to-One NAT)

Bei Static NAT wird eine private IP-Adresse fest einer öffentlichen IP-Adresse zugeordnet. Dies wird verwendet, wenn ein Server im privaten Netzwerk dauerhaft aus dem Internet erreichbar sein soll.

**Beispiel:**
- Privat: 192.168.1.100 ↔ Öffentlich: 203.0.113.10

### 2. Dynamic NAT

Dynamic NAT ordnet private IP-Adressen dynamisch aus einem Pool öffentlicher IP-Adressen zu. Die Zuordnung erfolgt bei Bedarf und wird nach einer gewissen Zeit wieder freigegeben.

### 3. Port Address Translation (PAT)

#### Was ist ein Port?

Um zu verstehen, wie PAT funktioniert, müssen wir zuerst das Konzept der Ports verstehen. Eine IP-Adresse identifiziert einen Computer im Netzwerk – aber auf einem Computer laufen gleichzeitig viele Programme, die alle Netzwerkverbindungen nutzen möchten.

**Analogie:** Stellen Sie sich die IP-Adresse als Postadresse eines Hochhauses vor. Die Portnummer entspricht dann der Wohnungsnummer. So wie die Post weiss, in welche Wohnung ein Brief gehört, weiss der Computer durch die Portnummer, an welches Programm die Daten geliefert werden sollen.

Ports sind 16-Bit-Zahlen (0 bis 65'535) und werden in drei Kategorien unterteilt:
- **Well-known Ports (0-1023):** Reserviert für Standarddienste
  - Port 80: HTTP (Webseiten)
  - Port 443: HTTPS (verschlüsselte Webseiten)
  - Port 22: SSH (sichere Verbindung)
  - Port 25: SMTP (E-Mail-Versand)
- **Registered Ports (1024-49'151):** Für registrierte Dienste
- **Dynamic/Private Ports (49'152-65'535):** Frei verwendbar

#### Funktionsweise von PAT

PAT, auch NAT-Overload genannt, ist die häufigste Form von NAT. Hier teilen sich viele private IP-Adressen eine einzige öffentliche IP-Adresse, wobei die Unterscheidung über Portnummern erfolgt.

Der Router merkt sich nicht nur, welche private IP-Adresse eine Verbindung aufgebaut hat, sondern auch über welchen Port. Dadurch können mehrere Geräte gleichzeitig über dieselbe öffentliche IP-Adresse kommunizieren.

**Rechenbeispiel:**
Mit 16-Bit-Portnummern stehen theoretisch $2^{16} = 65'536$ Ports zur Verfügung. Abzüglich der reservierten Ports (0-1023) bleiben etwa 64'512 nutzbare Ports für gleichzeitige Verbindungen. In der Praxis bedeutet dies, dass ein Heimrouter theoretisch über 64'000 gleichzeitige Verbindungen verwalten könnte.

## Vorteile und Nachteile

### Vorteile

- **IP-Adressen-Einsparung:** Ein Haushalt mit 20 Geräten benötigt nur eine öffentliche IP-Adresse
- **Sicherheit:** Private IP-Adressen sind von aussen nicht direkt erreichbar
- **Flexibilität:** Interne Netzwerkstruktur kann geändert werden, ohne die öffentliche Adresse zu beeinflussen

### Nachteile

- **Ende-zu-Ende-Konnektivität:** Direktverbindungen zwischen Geräten werden erschwert
- **Komplexität:** Bestimmte Anwendungen (z.B. VoIP, Online-Gaming) benötigen spezielle Konfigurationen
- **Performance:** Die Adressübersetzung benötigt Rechenleistung und kann zu Verzögerungen führen

## Praktisches Beispiel

Betrachten wir einen typischen Heimrouter:

1. **Ihr Laptop** (192.168.1.15) öffnet die Webseite www.example.com
2. **HTTP-Anfrage:** 
   - Quelle: 192.168.1.15:45678
   - Ziel: 93.184.216.34:80
3. **NAT-Router übersetzt:**
   - Quelle: 85.5.123.45:23456 (öffentliche IP)
   - Ziel: 93.184.216.34:80
4. **Server antwortet:**
   - Quelle: 93.184.216.34:80
   - Ziel: 85.5.123.45:23456
5. **Router übersetzt zurück:**
   - Quelle: 93.184.216.34:80
   - Ziel: 192.168.1.15:45678

## Bedeutung für die Zukunft

Mit der Einführung von IPv6 und seinen $2^{128}$ möglichen Adressen wird NAT theoretisch überflüssig. In der Praxis wird NAT jedoch weiterhin verwendet werden, da:

- Viele Netzwerke noch auf IPv4 basieren
- NAT zusätzliche Sicherheit bietet
- Die Umstellung auf IPv6 schrittweise erfolgt

NAT bleibt somit eine wichtige Technologie für das moderne Internet, die sowohl die Adressknappheit löst als auch zur Netzwerksicherheit beiträgt.
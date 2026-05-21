---
title: "Cyber-Selbstverteidigung: Was der eigene Rechner verrät"
subtitle: "Praktische Anleitung mit `nmap` und Wireshark – für Windows 11 und Linux"
date: today
format:
  html:
    toc: true
    number-sections: true
  pdf:
    toc: true
    number-sections: true
    documentclass: scrartcl
---

## Worum es geht

In diesem Selbstversuch beobachtest du deinen eigenen Rechner aus zwei Perspektiven:

1. **Aktiv**, indem du ihn mit `nmap` von «aussen» scannst und siehst, welche Dienste auf dem Gerät lauschen.
2. **Passiv**, indem du mit Wireshark den Netzwerkverkehr mitschneidest und sichtbar machst, was der Rechner und einzelne Programme *ohne deine Aufforderung* mit der Welt austauschen.

Ziel ist nicht, Hacker:in zu werden, sondern ein realistisches Bild der eigenen Angriffsfläche und der eigenen Datenspur zu gewinnen. Daraus folgen die konkreten Massnahmen der «Cyber-Selbstverteidigung» – Firewall, Updates, Tracker-Schutz, Verschlüsselung – fast von selbst.

### Lernziele

Nach diesem Versuch kannst du

- den Unterschied zwischen aktivem Scannen und passivem Mitschneiden erklären;
- die offenen Ports deines eigenen Geräts identifizieren und die zugehörigen Dienste benennen;
- einen Portscan im Netzwerkverkehr wiedererkennen (SYN / SYN-ACK / RST);
- mit Display-Filtern in Wireshark gezielt DNS-, TLS- und Tracker-Verkehr sichtbar machen;
- begründen, warum heutige Schutzmassnahmen weit mehr umfassen als «alle Ports zu».

## * Rechtlicher und ethischer Rahmen — **bitte zuerst lesen**

Portscans und Netzwerkmitschnitte sind in der Schweiz nur auf **eigenen** Systemen und im **eigenen** Netzwerk unproblematisch. Bereits ein Scan auf einen fremden Rechner kann den Tatbestand des unbefugten Eindringens in ein Datenverarbeitungssystem (Art. 143bis StGB) erfüllen.

**Regeln für diesen Selbstversuch**

- Scans und Mitschnitte ausschliesslich auf dem **eigenen Gerät** (`127.0.0.1` / `localhost`).
- Im Schulnetz nur nach ausdrücklicher Erlaubnis und nur auf das eigene Notebook.
- Mitschnitte können fremde Daten enthalten (z. B. Geräte von Mitschüler:innen im selben WLAN). Mitschnittdateien deshalb **nicht weitergeben** und nach dem Versuch löschen.

## Vorbereitung: Software installieren

Du brauchst zwei Werkzeuge: **Wireshark** (passiver Netzwerk-Sniffer) und **Nmap** (aktiver Portscanner).

### Windows 11

1. Wireshark von <https://www.wireshark.org/download.html> herunterladen (64-bit Windows Installer).
2. Installer ausführen. Während der Installation wird **Npcap** mitinstalliert. Wichtig:
   - Im Npcap-Dialog die Option **«Support loopback traffic ('Npcap Loopback Adapter')»** aktivieren.
   - Falls Wireshark bei dir bereits installiert ist, aber kein «Adapter for loopback traffic capture» erscheint: Npcap separat von <https://npcap.com/> neu installieren und die Loopback-Option setzen.
3. Nmap von <https://nmap.org/download.html> herunterladen («Latest stable release self-installer»). Zenmap (GUI) kann mitinstalliert werden, ist für unseren Zweck aber nicht nötig.
   - Falls Nmap fragt, ob es ein eigenes Npcap installieren soll: das bereits von Wireshark installierte Npcap behalten.
4. Schnelltest in der **PowerShell** (Windows-Taste, dann «PowerShell» eingeben):

   ```powershell
   nmap --version
   ```

   sollte die Versionsnummer ausgeben.


## Teil 1 — Welche Dienste lauschen auf meinem Rechner?

Bevor wir scannen, schauen wir mit Bordmitteln, welche Programme aktuell auf eingehende Verbindungen warten.

PowerShell als normaler Benutzer öffnen und dann die folgenden Befehle eingeben:

```powershell
Get-NetTCPConnection -State Listen |
  Select-Object LocalAddress, LocalPort, OwningProcess |
  Sort-Object LocalPort |
  Format-Table
```

Den Prozessnamen zu einer PID ermitteln:

```powershell
Get-Process -Id <PID>
```

Klassisch funktioniert auch:

```cmd
netstat -ano | findstr LISTENING
```

### Beobachtungsfragen

- Welche Ports sind bei dir offen? Welche Dienste vermutest du dahinter?
- Recherchiere unbekannte Ports (`5353`, `631`, `139`, `445`, `5355`, `5040` …). Brauchst du den jeweiligen Dienst?
- Auf welcher Adresse lauscht der Dienst? `127.0.0.1` (nur lokal), `0.0.0.0` (alle Netzwerkkarten) oder eine konkrete IP?

## Teil 2 — Portscan auf den eigenen Rechner

Wir prüfen jetzt aus «Aussenperspektive», was tatsächlich antwortet.

Auf beiden Betriebssystemen, Terminal bzw. PowerShell:

```bash
nmap -sT -p 1-1024 127.0.0.1
```

- `-sT` macht einen **TCP-Connect-Scan**: Nmap baut für jeden Port eine richtige TCP-Verbindung auf. Vorteil: funktioniert ohne Administrationsrechte.
- `-p 1-1024` beschränkt auf die ersten 1024 Ports (die «well-known ports»). Mit `-p-` werden alle 65 535 gescannt – dauert länger.

Variante mit Versionserkennung (langsamer):

```bash
nmap -sT -sV -p 1-1024 127.0.0.1
```

`-sV` versucht, beim offenen Port die laufende Software inkl. Version zu erraten.

### Beobachtungsfragen

- Stimmt das Ergebnis mit deiner Liste aus Teil 1 überein? Wo nicht – warum?
- Was bedeuten `open`, `closed`, `filtered`?
- Was würde sich vermutlich ändern, wenn du `localhost` durch die **IP im WLAN** ersetzen würdest? (Hinweis: Firewall des Betriebssystems.)

## Teil 3 — Wireshark beobachtet den Scan

Jetzt schauen wir uns denselben Scan aus der Netzwerk-Perspektive an. Wireshark zeichnet auf, *was tatsächlich auf der Leitung passiert*.

### Schritt 1: Wireshark starten und Interface wählen

- **Linux**: Im Wireshark-Startfenster die Schnittstelle **`lo`** (Loopback) doppelklicken.
- **Windows 11**: Den Eintrag **«Adapter for loopback traffic capture»** doppelklicken. Falls dieser nicht erscheint, fehlt die Loopback-Option in Npcap (siehe Installation).

### Schritt 2: (Optional) Capture-Filter setzen

Im Startfenster im Feld neben dem Interface den Capture-Filter eingeben:

```
tcp
```

Damit wird ARP-, mDNS- und IPv6-Hintergrundrauschen schon beim Aufzeichnen weggeschnitten.

### Schritt 3: Aufzeichnung starten

Auf das blaue Haifischflossen-Symbol oben links klicken. Wireshark zeigt jetzt live alle Pakete.

### Schritt 4: Im zweiten Fenster den Scan ausführen

Terminal/PowerShell öffnen und erneut:

```bash
nmap -sT -p 1-1024 127.0.0.1
```

### Schritt 5: Aufzeichnung stoppen und analysieren

Auf das rote Quadrat klicken. Du siehst jetzt mehrere tausend Pakete. Mit **Display-Filtern** machen wir Struktur sichtbar:

| Display-Filter | Was du siehst |
|---|---|
| `tcp.flags.syn == 1 and tcp.flags.ack == 0` | Die SYN-Pakete des Scans: einer pro geprüftem Port |
| `tcp.flags.syn == 1 and tcp.flags.ack == 1` | SYN-ACK von **offenen** Ports |
| `tcp.flags.reset == 1` | RST von **geschlossenen** Ports |
| `tcp.port == 80` | Nur Verkehr für einen konkreten Port |

Den Filter ins Feld direkt unter der Symbolleiste eingeben und Enter drücken.

### Beobachtungsfragen

- Wie viele SYN-Pakete schickt nmap pro Sekunde? Was würde das für einen Scan auf alle 65 535 Ports bedeuten?
- Welche der von dir in Teil 2 als `open` identifizierten Ports siehst du jetzt mit SYN-ACK?
- Was passiert nach dem Drei-Wege-Handshake bei `-sT` an einem offenen Port? (Tipp: schau auf die FIN- bzw. RST-Pakete am Ende.)

## Teil 4 — Was tut der Rechner, wenn ich gar nichts tue?

Jetzt drehen wir den Aufbau: keine Aktion am Rechner, aber Wireshark hört auf der **echten Netzwerkkarte**.

### Schritt 1: Vorbereitung

- Schliesse **alle** Browserfenster.
- Lass aber Mail-Client, Cloud-Sync (OneDrive, Nextcloud, …), Messenger u.ä. laufen, falls vorhanden – die wollen wir ja gerade beobachten.

### Schritt 2: Wireshark neu starten

Diesmal Interface:

- **Linux**: `wlan0`, `wlp…` oder `eth0` (die echte Karte, *nicht* `lo`).
- **Windows 11**: «Wi-Fi» oder «Ethernet».

Kein Capture-Filter setzen.

### Schritt 3: Zwei Minuten warten

Zwei Minuten lang den Rechner in Ruhe lassen. Dann Capture stoppen.

### Schritt 4: Mit Display-Filtern erkunden

| Display-Filter | Was du siehst |
|---|---|
| `dns` | Alle DNS-Anfragen: welche Hostnamen werden aufgelöst? |
| `tls.handshake.type == 1` | TLS-«Client Hello»: mit welchen Servern wird verschlüsselt gesprochen? |
| `mdns` | Geräte im lokalen Netz, die sich gegenseitig ankündigen |
| `dhcp` | Adressvergabe im lokalen Netz |
| `!arp && !ipv6.dst == ff02::/16` | Alles ausser dem grössten Rauschen |

Besonders aufschlussreich: **rechte Maustaste auf eine DNS-Zeile → Follow → UDP Stream**, oder **rechte Maustaste auf ein TLS-Hello → Expand → Server Name Indication**.

### Beobachtungsfragen

- Welche Hostnamen erscheinen, obwohl du nichts machst? Welche Applikationen verraten sich dadurch?
- Findest du Update-Checks, Cloud-Sync, Telemetrie? Notiere drei konkrete Beispiele.
- Welche Hostnamen erkennst du *nicht*? Wie könntest du sie zuordnen?

## Teil 5 — Eine «harmlose» Website besuchen

Jetzt sehen wir uns an, was der Browser tut, wenn du eine einzige Newsseite öffnest.

### Schritt 1: Vorbereitung

- Wireshark läuft weiterhin auf der echten Netzwerkkarte.
- Browser noch **geschlossen**.
- Aufzeichnung starten.

### Schritt 2: Eine Website öffnen

Browser starten und **eine** Webseite besuchen, zum Beispiel eine Schweizer Nachrichtenseite. Warten, bis die Seite vollständig geladen ist, dann Aufzeichnung stoppen.

### Schritt 3: Drittparteien sichtbar machen

Display-Filter:

```
tls.handshake.extensions_server_name
```

Wireshark zeigt jetzt nur noch TLS-Handshakes, bei denen sichtbar ist, mit welchem Hostnamen verhandelt wird. Diese Information (SNI, *Server Name Indication*) wird **vor** der Verschlüsselung übertragen und ist deshalb für uns lesbar – obwohl der Inhalt der Verbindung selbst verschlüsselt ist.

Zusätzlich praktisch: **Statistics → Endpoints → IPv4** zeigt eine Liste aller kontaktierten Gegenstellen mit Paketzahlen.

### Beobachtungsfragen

- Wie viele unterschiedliche Hostnamen wurden für *eine* Seite kontaktiert?
- Welche davon sind die Newsseite selbst, welche sind Drittparteien?
- Welche Drittparteien sind erkennbar Werbe- oder Tracking-Anbieter (`doubleclick.net`, `googletagmanager.com`, `facebook.net`, `criteo.com`, `adnxs.com` …)?
- Was sagt das über das Geschäftsmodell der Seite?

### Optionaler Vergleich

Installiere im Browser **uBlock Origin**, leere den Cache, wiederhole Schritt 2 mit derselben Seite und vergleiche die Anzahl Drittparteien.

## Synthese: Was nehmen wir mit?

1. **Aktive Sicht (Portscan).** Der Rechner hat eine Angriffsfläche aus *lauschenden Diensten*. Schutz: nicht benötigte Dienste deaktivieren, Firewall einschalten, Updates fahren.
2. **Passive Sicht (Mitschnitt im Leerlauf).** Der Rechner spricht ohne mein Zutun mit Dutzenden Servern. Schutz: Telemetrie minimieren, Cloud-Dienste bewusst wählen, evtl. Pi-hole oder NextDNS einsetzen.
3. **Passive Sicht (Webseiten-Aufruf).** Beim Surfen entstehen Datenspuren über ganze Werbe-Ökosysteme hinweg. Schutz: Content-Blocker, datenschutzfreundlicher Browser, Tracking-Schutz, ggf. eigener DNS-Resolver.
4. **Was Wireshark *nicht* zeigt.** Phishing-Mails, Social Engineering, kompromittierte Anmeldedaten, Supply-Chain-Angriffe auf installierte Software. Genau dort liegt heute das grössere Risiko – deshalb ergänzen wir technische Massnahmen um **Verhalten** (Passwortmanager, 2FA / Passkeys, Skepsis bei Mails), **Resilienz** (Backups) und **Hygiene** (Updates, Patch-Management).

## Optional / Weiterführendes

- **DNS over HTTPS aktivieren** (im Browser oder system-weit) und Capture wiederholen: Die `dns`-Filterzeile bleibt leer, der DNS-Verkehr läuft jetzt in TLS verpackt zu einem konfigurierten Resolver.
- **Eigenes Heimnetz vermessen** (nur dort!) mit `nmap -sn 192.168.1.0/24` zur Host-Erkennung. Wie viele Geräte sind angeschlossen? Erkennst du alle?
- **Mit `nmap -O` ein Betriebssystem-Fingerprinting** auf den eigenen Rechner versuchen. Wie genau ist die Vermutung?
- **Display-Filter-Galerie in Wireshark** (Statistics → Protocol Hierarchy) ansehen: zeigt, welche Protokollanteile dein Verkehr in welcher Zeit hatte.

## Anhang: Häufige Stolpersteine

| Problem | Ursache / Lösung |
|---|---|
| Wireshark zeigt unter Linux keine Interfaces | User nicht in Gruppe `wireshark`, oder Sitzung nicht neu gestartet |
| Unter Windows fehlt «Adapter for loopback traffic capture» | Npcap ohne Loopback-Option installiert; Npcap mit Option neu installieren |
| `nmap` zeigt unter Windows weniger Ports als unter Linux | Windows Defender Firewall filtert auch lokal; `127.0.0.1` ist davon meist nicht betroffen, externe IPs schon |
| Mitschnitt enthält praktisch nichts | Falsches Interface (z. B. virtuelle Schnittstelle statt WLAN) gewählt |
| Wireshark wird auf grossen Capture-Dateien extrem langsam | Mit Capture-Filter (nicht Display-Filter!) schon beim Aufzeichnen einschränken |

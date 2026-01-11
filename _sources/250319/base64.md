# Base64-Codierung

Die Base64-Codierung ist ein Verfahren zur Umwandlung von Binärdaten in eine
Zeichenkette, die nur aus lesbaren ASCII-Zeichen besteht. Diese Codierung wird
häufig verwendet, um binäre Daten über textbasierte Systeme zu übertragen, die
möglicherweise nicht mit Binärdaten umgehen können (z.B. E-Mails). Eine weitere
Anwendung ist die Einbettung von Bildern in HTML- oder Markdown-Dokumente.  
Untenstehende Octocat-Grafik ist ein Beispiel für eine Base64-codierte Grafik.

![Base64 codierte Octocat](data:image/png;base64,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)

Sofern die Website in Chrome geöffnet ist, kann die Grafik mit einem Rechtsklick
"untersucht" werden. Die "Untersuchung" zeigt den Quellcode der Seite an. Dort kann
die Base64-codierte Grafik gefunden werden. Diese beginnt mit
`data:image/png;base64,` und
setzt sich mit einer langen Zeichenkette fort. Diese Zeichenkette ist die
Base64-Codierung der Grafik.

## Prinzip der Base64-Codierung

Base64 wandelt 3 Bytes (24 Bits) Binärdaten in 4 druckbare ASCII-Zeichen um:

1. Die Binärdaten werden in 6-Bit-Blöcke aufgeteilt (2^6 = 64 mögliche Werte)
2. Jeder 6-Bit-Block wird in ein druckbares ASCII-Zeichen umgewandelt
3. Bei unvollständigen Blocks am Ende werden Füllzeichen (`=`) hinzugefügt

## Base64-Zeichensatz

Der Base64-Zeichensatz besteht aus 64 Zeichen:
- Die Großbuchstaben A-Z (26 Zeichen)
- Die Kleinbuchstaben a-z (26 Zeichen)
- Die Ziffern 0-9 (10 Zeichen)
- Zwei zusätzliche Zeichen, meist '+' und '/' (2 Zeichen)

Diese 64 Zeichen repräsentieren die Werte 0-63 und können mit 6 Bits dargestellt
werden. 

## Codierungsprozess

1. Die Binärdaten werden in Gruppen von 3 Bytes (24 Bits) aufgeteilt
2. Diese 24 Bits werden in vier 6-Bit-Blöcke umgewandelt
3. Jeder 6-Bit-Wert wird als Index für den Base64-Zeichensatz verwendet

Wenn die Anzahl der zu codierenden Bytes nicht durch 3 teilbar ist:
- Bei einem übrig bleibenden Byte: Auffüllen mit vier Nullbits, Codierung ergibt
  zwei Zeichen und zwei '='-Zeichen 
- Bei zwei übrig bleibenden Bytes: Auffüllen mit zwei Nullbits, Codierung ergibt
  drei Zeichen und ein '='-Zeichen 

## Beispiele:

### Beispiel 1: Codierung von "KBW"

![Base64 Beispiel](tabelle.svg)

### Beispiel 2: Codierung von "Hallo"

Betrachten wir das Wort "Hallo":

1. ASCII-Werte: H=72, a=97, l=108, l=108, o=111
2. Binär: 01001000 01100001 01101100 01101100 01101111
3. In 6-Bit-Gruppen aufteilen: 010010 000110 000101 101100 011011 000110 1111
4. Da die letzte Gruppe nur 4 Bits hat, wird sie mit zwei Nullen aufgefüllt: 010010 000110 000101 101100 011011 000110 111100
5. Die 6-Bit-Werte sind: 18, 6, 5, 44, 27, 6, 60
6. Diese werden in Base64-Zeichen umgewandelt: S G F s b G 8 =

Das Ergebnis "SGFsbG8=" ist die Base64-Codierung von "Hallo".

## Anwendungen der Base64-Codierung

- E-Mail-Anhänge (MIME)
- Datenkodierung in URLs
- Einbettung von Bildern in HTML/CSS (Data-URLs)
- Übertragung binärer Daten in JSON
- Speicherung von Binärdaten in XML

Base64 vergrößert die Datenmenge um etwa 33% (da 3 Bytes in 4 Zeichen
umgewandelt werden), bietet aber den Vorteil, dass die codierten Daten in jedem
Textformat sicher übertragen werden können. 
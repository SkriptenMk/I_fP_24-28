# RSA

RSA ist ein Kryptografie-System für asymmetrische Verschlüsselung und
Signatur. Es wurde Jahrzehnte lang verwendet und wird nun stetig von
neueren Systemen abgelöst.

## Lernziele

1.  Sie entschlüsseln und verschlüsseln eine Zahl mit dem gegebenen
    öffentlichen, beziehungsweise mit dem privaten Schlüssel.
2.  Sie wissen, auf welcher mathematischen Schwierigkeit RSA beruht.
    Anders ausgedrückt: Was muss man machen, um vom öffentlichen auf den
    privaten Schlüssel zu kommen.
3.  Sie erklären das Prinzip der Signatur und berechnen eine RSA
    Signatur.

## Die Mathematik hinter RSA

Wie RSA funktioniert, betrachten wir mit dieser interaktiven Webseite
[www.cryptool.org/de/cto/rsa-step-by-step/](https://www.cryptool.org/de/cto/rsa-step-by-step/).

### Tipps

Der Taschenrechner kann nicht gut modulo mit grossen Zahlen rechnen.

Python ist da besser geeignet. Wenn Sie $c=88^{17} ~mod~ 143$ rechnen
möchten, können Sie es in Python wie folgt berechnen:

``` py
c = 88**17 % 143
print(c)
# 121
```

:::{dropdown} Zusätzlicher Hintergrund zum Rechnen

Python kann
`88000**80021` nicht ausrechnen, aber `88000**80021 % 89911` schon.

$88000 \cdot 80021$ ist zu gross für den Speicher. Python berechnet vor
zu den Rest und braucht damit nicht nur weniger Speicher, sondern
rechnet auch viel schneller.

:::

### Signieren

Betrachten wir die Situation, dass Alice mitteilen möchte, wann Sie am
Bahnhof ankommt. Sie kann es nicht direkt an Bob schreiben, sondern
Mallory. Sie möchte nicht, dass Bob zu einer falschen Uhrzeit am Bahnhof
wartet. Alice hat Bob deshalb im Vorfeld ihren öffentlichen Schlüssel
geteilt.

-   Privater Schlüssel: $(n=143, d=113)$
-   Öffentlicher Schlüssel: $(n=143,e=17)$

Mallory darf den öffentlichen Schlüssel auch kennen. Der private
Schlüssel kennt nur Alice.

Was Alice macht, ist sie Gibt die Stunde bekannt: Sie kommt um 15 Uhr
an. Nun berechnet Alice zusätzlich \$ 15\^e ~mod~ n = 15\^{17} ~mod~ 143
= 71 \$. Sie legt diese Zahl 71 als Signatur bei.

Wenn Mallory nichts ändert, bekommt Bob "Uhrzeit 15, Signatur 71". Bob
kann nun den Inhalt überprüfen, indem er \$ signatur \^ d ~mod~ n = 71
\^{113} ~mod~ 143 = 15 \$ berechnet. Er merkt, die Zahl stimmt überein.

Wenn Mallory eine falsche Zeit an Bob geben möchte und die Zeit zu 14
anpasst, merkt Alice, dass die Zeit nicht mit der Signatur über
einpasst. Wenn Mallory die Signatur auch anpassen möchte, müsste sie die
Signatur finden, sodass \$ x = 14\^e ~mod~n\$ was genau so schwierig ist
wie das Entschlüsseln der Nachricht.

:::{tip} Aufgabe

1.  Erstellen Sie auf der [bekannten cryptool
    Seite](https://www.cryptool.org/de/cto/rsa-step-by-step/) ein
    Schlüsselpaar.
2.  Wählen Sie (zufällig) 3 Zahlen.
3.  Erstellen Sie zu jeder Zahl die Signatur.
4.  Verändern Sie bei einem Tupel die Zahl, bei einem anderen die
    Signatur.
5.  Tauschen Sie den öffentlichen Schlüssel mit den 3 Tupeln mit Ihrem
    Nachbar aus.
6.  Testen Sie die Tupel, welches stimmt.

:::

## GPG4win / Kleopatra

In diesem Teil der Lektion verwenden wir die echte Verschlüsselung.
GnuPG ist eine Software, welche RSA und modernere Kryptografie-Systeme
implementiert hat.

Befolgen Sie die Schritte 1-3 von Anleitung hier:[https://www.german-privacy-fund.de/dateien-verschlusseln-mit-kleopatra-windows/](https://www.german-privacy-fund.de/dateien-verschlusseln-mit-kleopatra-windows/)

1.   Verwenden Sie ihre KBW Mailadresse um ein Schlüsselpaar zu erstellen
2.   Laden Sie Ihren public key (Nicht den SECRET Key!) auf den Kanal _Kleopatra_ in den Ordner _public_key_ hoch.
3.   Spielen Sie mit dem Notzikblock von Kleopatra, bis die ganze Klasse soweit ist.

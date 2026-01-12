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
3.  Sie erklären das Prinzip der Signatur. Sie berechnen eine RSA
    Signatur. Sie überprüfen, ob eine Nachricht zur RSA Signatur passt.

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

:::{.callout-note collapse="true"} 
Zusätzlicher Hintergrund zum Rechnen

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
an. Nun berechnet Alice zusätzlich $$ 15^d ~mod~ n = 15^{113} ~mod~ 143
= 97 $$. Sie legt diese Zahl 97 als Signatur bei.

Wenn Mallory nichts ändert, bekommt Bob "Uhrzeit 15, Signatur 97". Bob
kann nun den Inhalt überprüfen, indem er $$ signatur ^ e ~mod~ n = 97
^{17} ~mod~ 143 = 15 $$ berechnet. Er merkt, die Zahl stimmt überein.

Wenn Mallory eine falsche Zeit an Bob geben möchte und die Zeit zu 14
anpasst, merkt Alice, dass die Zeit nicht mit der Signatur über
einpasst. Wenn Mallory die Signatur auch anpassen möchte, müsste sie die
Signatur finden, sodass $$ x = 14^e ~mod~n. $$ Dies ist genau so schwierig,
wie das Entschlüsseln der Nachricht.

:::{.callout-tip} 
## Aufgabe

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

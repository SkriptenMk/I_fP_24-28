# RSA

Wie RSA funktioniert, betrachten wir mit dieser interaktiven Webseite [www.cryptool.org/de/cto/rsa-step-by-step/](https://www.cryptool.org/de/cto/rsa-step-by-step/).

## Lernziele

  1. Sie entschlüsseln und verschlüsseln eine Zahl mit dem gegebenen öffentlichen, bzw. mit dem privaten Schlüssel.
  2. Sie wissen, auf welcher mathematischen Schwirigkeit RSA beruht. Anders ausgefrückt: Was muss man machen, um vom öffetlichen auf den privaten Schlüssel zu kommen.

## Tipps

Der Taschenrechner kann nicht gut modulo mit grossen Zahlen rechnen.

Python ist da besser geeignet. Wenn Sie $c=88^17 mod 143$ rechnen möchten, können Sie es in Python wie folgt berechenen:

```py
c = 88**17 % 143
print(c)
# 121
```

Python kann `88000**80021` nicht ausrechnen, aber `88000**80021 % 89911` schon.

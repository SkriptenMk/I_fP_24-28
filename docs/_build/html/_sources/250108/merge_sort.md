# Merge Sort

Merge Sort basiert auf der Grundidee, vorsortierte Teile einer Sequenz zu einer
sortierten Gesamtsequenz zusammenzufügen. Dazu wird eine unsortierte Sequenz so
lange in Teilsequenzen zerlegt, bis nur noch sortierte Teile - das heisst
einzelne Elemente - übrigbleiben. Diese Teilsequenzen werden dann Schritt für
Schritt zu sortierten Teilen und schlussendlich zu einem sortierten ganzen
wieder zusammengefügt.

Die folgenden Grafiken sollen das Vorgehen illustrieren.

![](schema.svg)

Um Merge Sort in Python zu implementieren, wird der Algorithmus in zwei
Funktionen aufgeteilt - die rekursive Aufteilung der zu sortierenden Sequenz und
den Merge-Schritt. Eine konkrete Implementation zeigen die folgenden beiden
Listings[^1].

```{Python}
def merge(s1, s2, s):
'''Funktion zum Zusammenführen zweier vorsortierter Listen s1 und s2 
in eine korrekt dimensionierte Liste s.'''

    i = j = 0

    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i+j] = s1[i]
            i += 1
        else:
            s[i+j] = s2[j]
            j += 1
```

```{Python}
def merge_sort(s):
'''Sortiert die Elemente einer Python Liste mit Hilfe
des Merge Sort Algorithmus'''

    n = len(s)

    if n < 2:
        return

    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]

    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, s)
```

Weil Merge Sort insgesamt $log_2 n$ Teilungen und $n$ Vergleiche vornehmen muss
liegt der Aufwand von Merge Sort bei $\mathcal{O}(n log n)$.


[^1]: Goodrich, Michael T., Roberto Tamassia, and Michael H. Goldwasser. Data
    structures and algorithms in Python. Hoboken, NJ: Wiley, 2013, pp 543.

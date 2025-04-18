# Queues in Python

Queues sind Datenstrukturen, welche Daten speichern und grundsätzlich in der
Reihenfolge, in der sie abgespeichert worden sind, wieder zurückgeben (First In
\- First Out, FIFO).  
Eine Queue funktioniert damit wie eine Warteschlange an einer Kasse: Wenn eine
neue Person ankommt, stellt sie sich hinten an. Wenn sie die Kasse erreicht
(nachdem alle, die vorher angestanden sind, bedient worden sind),
verlässt sie die Schlange wieder.

Eine Queue ist eine derart fundamentale Datenstruktur, dass
Python sie als [Library](https://docs.python.org/3/library/queue.html) zur
Verfügung stellt.

Um zu verstehen, wie eine Queue funktioniert, geht es im folgenden darum, eine
eigene Klasse Queue in Python zu implementieren. 

Zu Beginn ist zu überlegen, welche Eigenschaften, die Queue aufweisen muss. Sie
muss Daten abspeichern und diese in der gleichen Reihenfolge wieder ausgeben
können. Wir brauchen also eine Struktur für die Daten und eine Struktur, welche
die Reihenfolge der Speicherung festhält. Die Struktur, welche die Reihenfolge
festhält, muss ausserdem in der Lage sein, neue Daten abzuspeichern und bereits
abgespeicherte Daten wieder zurückzugeben. Diese Anforderungen können mit Hilfe
bereits programmierter Klassen umgesetzt werden. Um die Daten abzuspeichern,
können wir Nodes verwenden und für die Struktur zum Erhalt der Reihenfolge die
Linke List.

```{dropdown} Linked List
Die Linked List ist eine Datenstruktur, die aus einer Anzahl von Nodes
besteht. Jeder Node hat einen Bezug auf den nächsten Node in der Liste.
Damit ist es möglich, die Nodes in einer bestimmten Reihenfolge
abzuspeichern.  
Im Node selber gibt es ein Datenfeld `key` für die Bezeichnung des Nodes,
eines `value` für die Daten, die gespeichert werden sollen
sowie ein solches für den Verweis auf den nächsten Node. Die Datenstruktur 
Linked List stellt in erster Linie den Verweis auf den zuletzt eingefügten
Node zur Verfügung.
```

In der aktuellen Implementation der Linked List gibt es nur einen Positionsbezug
auf das letzte eingefügte Element (`self.root`). Damit die Linked List als Queue
verwendet werden kann, muss auch ein Bezug auf das erste eingefügte Element
angelegt werden (`self.head`). Für das Erste überhaupt in die Datenstruktur
eingefügte Element ist dies kein Problem. Wenn aber weitere Elemente eingefügt
oder entfernt werden, dann muss in den einzelnen Nodes nicht nur ein Bezug auf
das folgende Element (`self.connections['next']`) sondern auch einer auf das
Vorangehende Element (`self.connections['previous']`). Entsprechend müssen die
beiden Klassen Node und Linked List angepasst werden.

Das kann umgesetzt werden, in dem basierend auf den bereits existierenden
Klassen abgeleitete Klassen implementiert werden. Als UML-Klassendiagramm sieht
das folgendermassen aus:

![](class_diagram.svg)

Für die Umsetzung der obigen Ausführungen stehen hier zwei Module
([linked_list.py](src/linked_list.py) und [nodes.py](src/nodes.py)) zur
Verfügung. 
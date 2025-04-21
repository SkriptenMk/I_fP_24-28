# Einführung in Datenbanken

Die Einführung in Datenbanken basiert auf dem Einführungskapitel aus dem Buch
Abraham Silberschatz, Henry F. Korth und S. Sudarshan; Database system
concepts; Seventh edition; New York 2020.

## Einführung

Die bisher besprochenen Datenstrukturen 
Dictionary, Stack, Queue und Binary Search Tree
dienen der Bearbeitung von Daten im
Arbeitsspeicher. Sie sind daher auf einen beschränkten Umfang von Datensätzen
ausgelegt. Ausserdem dienen sie nicht der permanenten Ablage von Daten.

Im Gegensatz dazu dienen Datenbanken der dauerhaften Ablage grosser Datensätze.
Darüber hinaus sollen sie die effiziente Verfügbarkeit und die Integrität der
Daten sicherstellen.

## Charakteristika von Datenbanken

Ein wichtiges Merkmal von Datenbanken ist es, dass die gespeicherten Daten nur
einmal abgelegt werden. Damit kann verhindert werden, dass mehrfach
abgespeicherte Daten (redundante Daten)
lediglich an einer Stelle modifiziert werden und damit Widersprüche entstehen.
Der Entwurf von Datenbanken muss dem Rechnung tragen. Ein Hilfsmittel für den
Entwurf von Datenbanken ist das ER-Diagramm (Entity-Relationship-Diagramm).
Das ER-Diagramm ist eine grafische Darstellung der Datenbankstruktur. Es zeigt
die Entitäten (durch die Datenbank modellierte Dinge der realen Welt), die in
der Datenbank gespeichert werden, mit ihren Attributen (Eigenschaften der
modellierten Dinge)
sowie die Beziehungen (Relationship) zwischen den Entitäten. 

Um einen Eintrag in der Datenbank eindeutig identifizieren zu können, wird
jedem Eintrag ein Primärschlüssel zugeordnet. Der Primärschlüssel ist ein
Attribut oder eine Kombination von Attributen, die den Eintrag eindeutig
identifiziert.  
In den Beziehungen werden die Primärschlüssel der Entitäten als
Fremdschlüssel verwendet. Ein Fremdschlüssel ist ein Attribut oder eine
Kombination von Attributen, die auf den Primärschlüssel einer anderen Entität
verweisen. So kann eine Beziehung zwischen zwei Entitäten hergestellt werden.

Die untenstehende Graphik zeigt eine Skizze eines ER-Diagramms, in welchem die
Beziehungen zwischen Schülern, Klassen und Lehrern dargestellt wird. Ausserdem
wird gezeigt, welche Attribute als Primär- bzw. Fremdschlüssel verwendet
werden.

![ER-Diagramm](er_example_klein.svg)

Jede Datenbank ist immer eine Vereinfachung der Wirklichkeit und daher immer
unvollständig bzw. erweiterbar. Das obige ER-Diagramm kann daher um eine
zusätzliche Entität `Fach` erweitert werden und sieht dann folgendermassen aus:

![ER-Diagramm](er_example_gross.svg)

Diese Grafiken können in Datenbanktabellen übersetzt werden. In den Tabellen
werden die Primärschlüssel unterstrichen. Die Primärschlüssel sind in der Regel
die ersten Spalten der Tabellen. Für das Beispiel
werden Tabellen für die Entitäten `Klasse`, `Fach` und `Lehrer` erstellt.	

Die Einfachste Tabelle ist die Tabelle `Klasse`. Sie enthält lediglich ein
Attribut (den Primärschlüssel).

![Klasse](entity_class.svg)

Etwas umfangreicher sind die Tabellen `Fach` und `Lehrer`. Sie enthalten jeweils
drei bzw. vier Attribute.

<div style="display: flex; justify-content: space-between;align-items: flex-start;">
    <img src="entity_subject.svg" alt="Tabelle Fach" style="width: 45%;">
    <img src="entity_teacher.svg" alt="Tabelle Lehrer" style="width: 45%;">
</div>

Im Folgenden Abschnitt sollen die Daten aus den Tabellen mit Hilfe von SQL
Statements abgefragt werden.
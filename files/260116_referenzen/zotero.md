# Literaturverwaltung mit Zotero

Zotero bewirbt sich selber als persönlicher Forschungsassistent. Im
gymnasialen Umfeld ist Zotero in erster Linie ein Hilfsmittel Zitate in
Texten korrekt zu formatieren. Darüber hinaus kann Zotero auch als
E-Reader mit Zusatzfunktionen zur Verwaltung von Notizen verwendet
werden. 

## Zotero installieren und einrichten

Um die Funktionen von Zotero im vollen Umfang zu nutzen, ist es sinnvoll
ein Zotero Account zu erstellen. Der Account kann auf der Website von
[Zotero](https://www.zotero.org/user/register) erstellt werden. Wenn der
Account nicht ausschliesslich privat genutzt werden soll, ist es
sinnvoll die Schul- bzw.\ Geschäftsemail zu verwenden. Im Nutzerprofil
können auch mehrere Adressen hinterlegt werden. Das ermöglicht es, die
eigene Datenbank zu behalten, wenn man eine Institution verlässt.

Nachdem optional ein persönlicher Account erstellt worden ist, kann der
[Zotero Desktop Client](https://www.zotero.org/download/)
heruntergeladen und installiert werden. Auf der gleichen Seite findet
sich auch die Möglichkeit den Zotero Connector als Browser Plugin
herunterzuladen. Dieses Plugin ist für die Arbeit mit Zotero nicht
zwingend erforderlich, vereinfacht aber die Erfassung von Quellen
ungemein.

Wenn Zotero installiert ist, kann es über den Menüpunkt Bearbeiten >
Einstellungen, Registerkarte Sync mit dem eigenen Zotero Account
verbunden werden.

Für die Verwendung von Zotero in einem Markdown -- Pandoc-Workflow ist
die Installation des
[BetterBibTeX](https://retorque.re/zotero-better-bibtex/) Plugins in
Zotero unbedingt erforderlich. Das Plugin kann direkt aus seinem 
[GitHub
Repository](https://github.com/retorquere/zotero-better-bibtex/releases/latest)
heruntergeladen werden. Das heruntergeladene `.xpi` Dokument kann über
das Menü Werkzeuge > Plugins, Zahnradsymbol, Install Plugin from File,
installiert werden.

## Einträge in Zotero erstellen und organisieren

Wie Einträge in Zotero erfasst werden, wird auf der Website von Zotero
ausführlich beschrieben. An dieser Stelle darf daher auf die dortigen
[Erklärungen](https://www.zotero.org/support/adding_items_to_zotero)
verwiesen werden. Das gleiche gilt für die
[Organisation](https://www.zotero.org/support/collections_and_tags) der
eigenen Bibliothek. 

Damit die Einträge aus Zotero in den Texten gelesen werden können,
müssen sie mit dem Zitierschlüssel (citation key) adressiert werden. Die
genaue Syntax dazu wird in @sec-referenzen_einf erklärt. Zotero erstellt
für jeden Eintrag einen Standardschlüssel. Dieser ist jedoch oft schwer
zu merken. Es empfiehlt sich daher, den Zitierschlüssel selber
festzulegen. Dazu ist im Feld "Extra" der Metadaten des Eintrags das
"Key -- Value" Paar "citation key: eigener_schlüssel" einzutragen.
Gespeichert wird der so festgelegte Zitierschlüssel in dem das Feld
"Extra" wieder verlassen wird. Der einfachste Zitierschlüssel ist wohl
`autorYYYY` wobei `YYYY` für die vierstellige Jahreszahl steht.

## Erstellen einer Bibliographie Datei für den Markdown -- Pandoc-Workflow

Die für das jeweilige Projekt erforderlichen Einträge in Zotero werden
sinnvollerweise in einer Sammlung zusammengefasst. Diese Sammlung kann dann
in eine `.bib` Datei exportiert werden. Dazu ist das Kontextmenü der
Sammlung mit Rechtsklick zu öffnen. Anschliessend ist der Menüpunkt
'Sammlung Exportieren' auszuwählen. In der sich öffnenden Dialogbox ist
Better BibLaTeX als Format auszuwählen. Sinnvollerweise werden die beiden
Optionen 'Halte aktuell' und 'Hintergrund-Export' ausgewählt. Die erste
Option sorgt dafür, dass Änderungen in Zotero-Einträgen automatisch in die
`.bib` Datei geschrieben werden, die zweite verhindert, dass der Export
einfriert.  
Standardmässig erhält die so erstellte `.bib` Datei den Namen der
Sammlung. Der Name kann während des Erstellens noch angepasst werden.
Falls der Name nachträglich angepasst wird, ist nicht sichergestellt,
dass die automatische Aktualisierung weiterhin funktioniert. Falls man dem
Automatismus nicht vertraut, kann die `.bib` Datei nach jeder Änderung
manuell neu aus Zotero exportiert werden.
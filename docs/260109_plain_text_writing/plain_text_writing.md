# Plain Text Writing

In diesem Abschnitt geht es um einen Aspekt der digitalen
Nachhaltigkeit. Digitale Nachhaltigkeit wird hier so verstanden, dass
digitale Produkte unabhängig von konkreten Herstellern dargestellt
werden können.  
Um zu erklären, wo das Problem liegt, muss zuerst zwischen den zwei
Dateitypen Textdateien und Binärdateien unterscheiden werden.

## Text- und Binärdateien

Textdateien speichern ihren Inhalt als reinen Text. Formatierung in
solchen Dateien erfolgen durch Steuerzeichen 
(vgl. z.B. ASCII-Tabelle, dort insbesondere die Beispiele der Zeichen 9
für einen horizontalen Tabulatoren oder Zeichen 10 für den
Zeilenumbruch) und durch Konventionen (vgl. z.B. die Formatierungen in
Markdown oder LaTeX).
Entsprechend können sie in beliebigen Texteditoren gelesen werden. 

Im Gegensatz dazu sind Binärdateien für ihre Erstellung, Bearbeitung und
Darstellung grundsätzlich an Programme gebunden, welche ihren Standard
lesen können. Ihre Inhalte
werden als eine Folge von Bytes gespeichert. Ein Beispiel für eine
Binärdatei ist ein in MS Word erstelltes Dokument.

Diese Unterscheidung zeigt, dass Textdateien grundsätzlich auf jedem
funktionierenden Computer mit einem Texteditor angezeigt werden können.
Im Gegensatz dazu erfordern Binärdateien in der Regel spezielle
Programme, die das jeweilige Dateiformat interpretieren können, was zu
einer gewissen Abhängigkeit von entsprechender Software führen kann. 

Weiterführende Überlegungen zum Verfassen von Texten in Plain Text
können den hier angeführten Texten entnommen werden[@healy2020; @fix2020].

## Plain Text Formate für die Textredaktion

Die einfachste Form eines Textfiles ist eine `.txt` Datei. Dabei handelt
es sich in der Regel um reinen Text ohne Formatierungen. Das Bedürfnis
nach formatierten Textdarstellungen hat zu verschiedenen Dateiformaten
geführt. Dazu gehören zum Beispiel HTML-Dateien (`.html` oder `.htm`:
**H**yper **T**ext **M**arkup **L**anguage).
Dieses Format wurde ursprünglich unter anderem auch dazu geschaffen,
Text formatiert am Bildschirm darzustellen. Ein anderes Beispiel ist
LaTeX. Auch LaTeX ist eine sogenannte Auszeichnungssprache (Markup
Language). Allerdings ist das Zielmedium von LaTeX weniger der
Bildschirm sondern eher der Druck, heute vor allem das Portable Document
Format (PDF), welches sich zum Quasi-Standard entwickelt hat.

Allerdings ist der Umfang der Formatierungsmöglichkeiten sowohl in HTML
wie auch in LaTeX so umfangreich, dass die Hürde für deren Verwendung
relativ hoch ist.

Vor diesem Hintergrund ist eine eher minimalistische
Auszeichnungssprache, Markdown (`.md`) geschaffen worden. Diese stellt
alle wesentlichen Formatierungsmöglichkeiten, wie zum Beispiel
hierarchische Überschriften oder das setzen von kursivem Text, direkt
zur Verfügung. Dort wo die Formatierungsmöglichkeiten den Bedürfnissen
nicht genügen, kann in vielen Fällen auf HTML oder LaTeX
Auszeichnungen zurückgegriffen werden.

Eine Übersicht über die Formatierungsbefehle in Markdown findet sich auf
der Website [Markdown Cheat
Sheet](https://www.markdownguide.org/cheat-sheet/). Wichtige
Formatierungen in LaTeX (mathematische Formeln) werden auf der
Website [Wikibooks
LaTeX/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics)
erklärt.

# Konvertierung von Markdown in PDF

Markdown hat den klaren Vorzug, in jedem Texteditor gelesen werden zu
können. Leider ist reines Markdown nicht sehr ästhetisch. Zudem müssen
die meisten Texte zu Handen des Empfängers in ein PDF konvertiert
werden.

## Vorbereitung der Konvertierung

Für diese Konvertierung kann das Programm Pandoc verwendet werden.
Pandoc kann Markdown in unzählige Formate Konvertieren. Die genaue
Vorgehensweise wird im Folgenden Schritt für Schritt erläutert.

1. Pandoc installieren
   
   Das Installationsprogramm für Pandoc kann auf der Website von 
   [Pandoc heruntergeladen](https://pandoc.org/installing.html) werden.
   Dazu ist dem Link "Download the latest Installer" zu folgen. Für
   Windows ist die Datei mit der Endung `.msi` herunterzuladen.
 
   Das heruntergeladene Installationsprogramm kann anschliessend mit
   einem Doppelklick für die Installation ausgeführt werden.

2. LaTeX installieren

    Damit Pandoc ein Markdown Dokument in ein PDF Konvertieren kann,
    braucht es auf dem Rechner eine Installation von LaTeX. LaTeX
    gibt es für Windows in verschiedenen Varianten. Die einfachste
    Installation erfolgt in der Variante von MiKTeX. Das entsprechende
    Installationspaket kann von der Website von
    [MiKTeX](https://miktex.org/download) 
    heruntergeladen werden. 

    Das heruntergeladene Installationsprogramm kann anschliessend mit
    einem Doppelklick für die Installation ausgeführt werden.


3. Pandoc verwenden
   
   Pandoc ist ein Programm für die Kommandozeile. Das heisst, es gibt
   keine grafische Oberfläche für die Verwendung von Pandoc. Am
   einfachsten kann Pandoc verwendet werden, wenn im Ordner, in dem sich
   das zu konvertierende File befindet, ein Terminal geöffnet wird.

   Die Konvertierung erfolgt mit folgendem Befehl:

   ```bash
   pandoc -o output.pdf input.md
   ```

   Output.pdf und input.md muss an die eigenen Dateinamen angepasst
   werden. Alternativ können auch andere Dateiformate, wie `.docx` oder
   `.html` als Zielformate gewählt werden. Für eine
   abschliessende Liste aller möglichen Zielformate sei auf die Website
   von Pandoc verwiesen.

## Spezifische Formatierung der Ausgabe

Die oben dargestellte Version führt zu einem sauber strukturierten PDF.
Allerdings fehlen wesentliche Dokumentteile wie Deckblatt oder
Inhaltsverzeichnis. 

Für diese weiterführenden Formatierungen werden dem Dokument die
erforderlichen Informationen entweder in einem speziellen Header
vorangestellt oder in einem separaten Dokument dem Befehl für die
Konvertierung übergeben. Hier soll die zweite Variante dargestellt
werden. 

Das Dokument mit den Informationen für die Formatierung ist ein
sogenanntes YAML-Dokument `.yaml`. YAML steht dabei für **Y**et **A**nother
**M**arkup **L**language. Das Dokument kann einen beliebigen Namen
haben. Hier im Beispiel wird es `format.yaml` genannt. Das folgende
Listing zeigt eine Formatierung mit dem Namen des Authors, dem Titel und
weiteren Angaben. Was die einzelnen Einträge bedeuten, ist weitestgehend
selbsterklärend. 

```yaml
from: markdown                     # Ausgangsformat 
to: pdf                            # Zielformat
standalone: true                   # Erzwingt eigenständiges Dokument
pdf-engine: xelatex                # Wählt eine spezifische pdf-engine
output-file: output.pdf            # Name des Ausgabedokuments
metadata:                          # Dokumentspezifische Angaben
  title: "Anleitung"               # Titel
  author: "Jacques Mock Schindler" # Verfasser
  lang: de-CH                      # Sprache des Dokuments
  fontsize: 11pt                   # Schriftgrösse
  geometry: left=2.5cm, right=3cm  # Seitenränder
  date: "9. Januar 2026"           # Datum
  toc: true                        # Erstellt ein Inhaltsverzeichnis
  number-sections: true            # Nummeriert die Titel
```

Die Einrückung ist für die Syntax im YAML Dokument wichtig. Sie beträgt
zwei Leerzeichen.

Wenn die Datei `format.yaml` das Format des PDF steuern soll, lautet der
Befehl für die Konvertierung des Markdown Dokuments in ein PDF

```bash
pandoc --defaults=format.yaml input.md
```

Falls der Name des neu erstellten PDF Dokuments bei jedem Befehlsaufruf
individuell festgelegt werden soll, kann die Zeile `output-file:
output.pdf` in der YAML Datei auch weggelassen werden. Dann lautet der
Befehl für die Konvertierung

```bash
pandoc --defaults=format.yaml -o output.pdf input.md
```

Falls für komplexe Formatierungen auf externe LaTeX Pakete abgestellt
werden muss, werden diese über ein separates `.tex` Dokument geladen.
Auch dieses Dokument kann grundsätzlich beliebig benannt werden. Für das
Beispiel hier wird die Datei als `header.tex` bezeichnet. Der Inhalt
dieser Datei ist folgendermassen zu formatieren:

```tex
\usepackage{caption}
```

Der Befehl für die Konvertierung lautet jetzt

```bash
pandox --defaults=format.yaml -H header.tex input.md
```

Die Website 
[CTAN Comprehensive TeX Archive Network](https://ctan.org/)
gibt Auskunft darüber, was für LaTeX Pakete zur Verfügung stehen.
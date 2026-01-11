# Referenzen in Markdown

Damit in Texten, die im Markdown Format erstellt werden, Literaturzitate
eingefügt werden können, braucht es neben dem Markdown Dokument mit dem
eigentlichen Text, drei weitere Dateien:

* eine Datei mit allen Formatierungsinformationen (`.yaml`), 
* eine Datei mit den bibliographischen Angaben (`.bib`) sowie 
* eine Datei mit den Formatierungsangaben für die Literaturdarstellung
  (`.csl`). 

Von diesen drei Dateien muss lediglich die Datei mit den
Formatierungsinformationen manuell erstellt werden. Die Datei mit den
bibliographischen Angaben wird von Zotero erstellt und die Datei für die
Darstellung der bibliographischen Angaben im Text kann aus dem [Zotero
Style Repository](https://www.zotero.org/styles) heruntergeladen werden.

## Textformat (.yaml)

Die Darstellung des Textes sowie dessen Ausgabeformat kann über die
Datei `format.yaml` gesteuert werden. Der Name der Datei ist frei
wählbar. Hier wurde `format.yaml` gewählt, weil die Datei genau das
macht: das Format der Ausgabe steuern. Im folgenden Listing findet sich
ein Beispiel mit den Angaben für die Verwendung einer `.bib` und `.csl`
Datei. 

```yaml
# Input und Output
input-files:
  - mein-text.md  # es können auch mehrere Dateien angegeben werden
  # - zweiter_teil.md
  # - dritter_teil.md
output-file: ausgabe.pdf

# Grundeinstellungen
from: markdown
to: pdf
# lualatex als pdf-engine hilft bei der Darstellung
# von Umlauten und anderen Sonderzeichen
pdf-engine: lualatex # oder xelatex, pdflatex

# Aktiviert citeproc - damit wird die Bibliographie eingebunden
citeproc: true

# Inhaltsverzeichnis
table-of-contents: true

# Variablen und Metadaten
variables:
  lang: de-CH
  lof: true
  lot: true
  number-sections: true
  header-includes:
    - \setcounter{secnumdepth}{3}
    - \setcounter{tocdepth}{3}

metadata:
  title: "Titel des Dokuments"
  author: "Ihr Name"
  date: "Heute"
  bibliography: bibliography.bib
  csl: chicago-notes-bibliography-access-dates.csl
  link-citations: true
```

Hier die Erklärungen zu den einzelnen Einträgen in dieser
Konfigurationsdatei:




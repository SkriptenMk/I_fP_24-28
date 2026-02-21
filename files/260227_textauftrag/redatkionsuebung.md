# Anweisungen für die Redaktionsübung

## Orientierung
Es geht bei dieser Aufgabe darum, dass Sie lernen, einen Text mit integrierten statistischen Auswertungen und Grafiken zu erstellen. Dabei sollen ausschliesslich Open Source Werkzeuge verwendet werden. Darüber hinaus sollen Sie sich mit den Vor- und Nachteilen des Einsatzes von Open Source Software auseinandersetzen.

## Absicht
Ich will 

* in erster Priorität, dass Sie die Möglichkeiten von Markdown und Jupyter Notebooks nutzen, um Ihre Analyse vorzunehmen;
* in zweiter Priorität, dass Sie eine nachvollziehbare Datenvisualisierung innerhalb Ihres Textes erstellen sowie
* in dritter Priorität, dass Sie Übersichtsgrafiken und Prinzipdarstellungen mit Hilfsmitteln aus der Familie 'Diagrams as Code' (Mermaid, PlantUML) erstellen können.

## Auftrag
Verfassen Sie eine Analyse zu den Chancen und Risiken des Einsatzes von Open Source Software im privaten wie auch im unternehmerischen Umfeld.

## Besondere Anordnungen
### Inhalt
* Der Begriff *Open Source Software* ist zu definieren.
* Die Analyse soll auch auf quantitative Aspekte des Einsatzes von Open Source Software eingehen. Verwenden Sie dazu öffentlich zugängliche Quellen.
* Die Analyse soll auf die Kosten des Einsatzes von Open Source Software eingehen.
* Die Analyse soll auf Fragen der Sicherheit eingehen.

### Formelles
* Die Analyse hat alle erforderlichen Verzeichnisse (Inhalt, Quellen, Tabellen, Abbildungen) zu enthalten.
* Sämtliche Grafiken sind innerhalb der Analyse zu erstellen.
* Quellen sind zu belegen.
* Der Einsatz von generativer KI ist zu deklarieren.

### Quellen

Die im folgenden angeführten Quellen können für die quantitativen Aspekte der Analyse verwendet werden.

1. Nutzungsstatistiken & Marktanteile
   
   Diese Quellen zeigen, wie tief OSS bereits in der Infrastruktur verwurzelt ist.
   
    * **GitHub – The State of the Octoverse (2025)**:    
        * **Inhalt**: Statistiken über die Anzahl der Repositories, die aktivsten Sprachen (Python, TypeScript) und das Wachstum von KI-Projekten.        
        * **Kernwert**: Zeigt das enorme Wachstum (z.B. über 395 Mio. Repositories weltweit).       
        * **Link**: [github.blog/octoverse](https://github.blog/news-insights/octoverse/)
        
    * **Linux Foundation – World of Open Source Survey (2025)**:    
        * **Inhalt**: Fokus auf die Akzeptanz in Unternehmen und Regierungen.        
        * **Kennzahl**: OSS-Durchdringung in Bereichen wie Cloud (49%), Web-Entwicklung (46%) und KI/ML (40%).        
        * **Link**: [linuxfoundation.org/research](https://www.linuxfoundation.org/research)
        
    * **W3Techs – Web Technology Surveys**:    
        * **Inhalt**: Echtzeit-Daten über den Einsatz von Webservern (Nginx, Apache) und Betriebssystemen im Web.        
        * **Link**: [w3techs.com](https://w3techs.com/)

2. Wirtschaftliche Aspekte & Kosten (TCO)

   Argumente zu „Lizenzkosten vs. Betriebskosten“.

    * **State of Open Source Report (Perforce/OSI)**:    
        * **Inhalt**: Jährliche Umfrage unter IT-Entscheidern zu den Gründen für OSS-Einsatz.        
        * **Kennzahl 2025**: 53 % der Unternehmen nennen „keine Lizenzgebühren/Kostensenkung“ als Hauptgrund (ein deutlicher Anstieg gegenüber den Vorjahren).        
        * **Link**: [opensource.org](https://opensource.org/)
        
    * **Quandary Peak Research (2025)**:    
        * **Inhalt**: Wissenschaftliche Analyse zum ökonomischen Wert von OSS.        
        * **Aussage**: Unternehmen müssten das **3,5-fache** für proprietäre Software ausgeben, um die gleiche Funktionalität zu erhalten, wenn es kein OSS gäbe.
        

 3. Sicherheit & Risiken

    Diese Quellen sind essenziell für den Teil „Sicherheit“ im Auftrag.

    * **Synopsys (Black Duck) – Open Source Security and Risk Analysis (OSSRA) Report**:    
        * **Inhalt**: Analyse von über 1.000 kommerziellen Codebasen auf Sicherheitslücken und Lizenzkonflikte.        
        * **Kennzahl 2025**: 97 % aller Anwendungen enthalten OSS-Komponenten; 81 % weisen mindestens eine kritische Sicherheitslücke auf (oft durch veraltete Versionen).        
        * **Link**: [blackduck.com/ossra](https://www.blackduck.com/blog/open-source-trends-ossra-report.html)
        
    * **Tidelift – State of the Open Source Maintainer Report**:    
        * **Inhalt**: Beleuchtet die „Risikoseite“ der Wartung. Wie viele Projekte werden nur von einer Person betreut? (Stichwort: Supply Chain Security).        
        * **Link**: [tidelift.com](https://tidelift.com/)


### Bewertung

Die Arbeit wird nach folgenden Kriterien bewertet. Die Gewichtung spiegelt die Prioritäten des Auftrags wider.

| Kriterium                                     | Gewicht | 3 Punkte (sehr gut)                                                                                                                         | 2 Punkte (genügend)                                                                             | 1 Punkt (ungenügend)                                                     |
| --------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Einsatz von Markdown und Jupyter Notebook** | 25 %    | Notebook ist sauber strukturiert, Code und Text sind sinnvoll verzahnt, Ergebnisse sind reproduzierbar.                                     | Notebook funktioniert grundsätzlich, weist aber Mängel in Struktur oder Reproduzierbarkeit auf. | Notebook ist unvollständig, Code läuft nicht oder ist vom Text getrennt. |
| **Datenvisualisierung**                       | 20 %    | Mindestens zwei aussagekräftige Grafiken, korrekt beschriftet, im Text interpretiert und mit Quellenangabe.                                 | Grafiken vorhanden, aber mit Mängeln bei Beschriftung, Interpretation oder Quellenangabe.       | Keine oder fehlerhafte Grafiken; fehlender Bezug zum Text.               |
| **Diagrams as Code**                          | 10 %    | Mindestens ein Diagramm (Mermaid/PlantUML) sinnvoll eingesetzt, korrekt gerendert und im Text eingebettet.                                  | Diagramm vorhanden, aber mit technischen oder inhaltlichen Mängeln.                             | Kein Diagramm oder nicht als Code erstellt.                              |
| **Inhaltliche Qualität**                      | 25 %    | OSS-Begriff definiert, Chancen und Risiken differenziert dargestellt, Kosten und Sicherheit fundiert behandelt, Quellen korrekt einbezogen. | Wesentliche Inhalte vorhanden, aber oberflächlich oder lückenhaft argumentiert.                 | Zentrale Inhalte fehlen oder sind sachlich falsch.                       |
| **Formale Anforderungen**                     | 10 %    | Alle Verzeichnisse vorhanden, Quellen vollständig belegt, KI-Einsatz deklariert, alle Quelltexte abgegeben.                                 | Kleine Lücken bei Verzeichnissen, Quellenbelegen oder Abgabeumfang.                             | Wesentliche formale Anforderungen nicht erfüllt.                         |
| **Sprache und Darstellung**                   | 10 %    | Klarer, präziser Ausdruck; angemessener Fachsprachgebrauch; gute Lesbarkeit.                                                                | Verständlich, aber sprachlich oder gestalterisch verbesserungsfähig.                            | Schwer verständlich oder durchgehend fehlerhaft.                         |

**Notenskala:** Die Gesamtpunktzahl ergibt sich aus der gewichteten Summe. Maximum: 3,00 Punkte. Es kommt eine lineare Notenskala zur Anwendung. Die Noten werden auf halbe Noten gerundet.

### Allgemeines
* **Termin**: Abgabetermin ist der 11. März 2026.
* **Tech Stack**: Verwenden Sie Jupyter Notebooks mit Python und Quarto, um Ihr Endprodukt zu erstellen.
* **Format**: Die Analyse kann als PDF oder HTML abgegeben werden. In jedem Fall sind alle verwendeten Quelltexte (je nach Arbeitsweise .qmd oder .ipynb, sowie die .yml-Datei und ggf. Bilder/Daten) abzugeben.
* **Grundkonfiguration**: Sie erhalten mit diesem Auftrag ein 
  [File `_quarto.yml` (Rechts-Klick zum Herunterladen; `_quarto.yml` als
  Name verwenden - der Bodenstrich am Anfang des Dateinamens ist zwingend)](quarto.yml) mit einer Grundkonfiguration für die Erstellung eines
  PDF.
* **Citation Style**: Der verwendete Zitierstil *Chicago Manual of Style
  17th edition (notes and bibliography)* steht 
  [hier zum Download zur Verfügung (Rechts-Klick zum Herunterladen)](files\260227_textauftrag\chicago-notes-bibliography-17th-edition.csl)

## Erreichbarkeit
Für Fragen stehe ich Ihnen während der Lektionen, via Teams oder über einen [Termin in der Sprechstunde](https://calendar.app.google/8vpokbeDbRXgxcGF7) zur Verfügung.
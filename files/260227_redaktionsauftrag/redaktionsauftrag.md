# Redaktionsübung

## Orientierung
Es geht bei dieser Aufgabe darum, dass Sie lernen, einen Text mit integrierten statistischen Auswertungen und Grafiken zu erstellen. Dabei sollen ausschliesslich Open Source Werkzeuge verwendet werden. Darüber hinaus sollen Sie sich mit den Vor- und Nachteilen des Einsatzes von Open Source Software auseinandersetzen.

## Absicht

Ich will,

* dass Sie mit erster Priorität die Möglichkeiten von Markdown und Jupyter Notebooks nutzen, um Ihre Analyse durchzuführen;
* dass Sie mit zweiter Priorität eine nachvollziehbare Datenvisualisierung innerhalb Ihres Textes erstellen und
* dass Sie mit dritter Priorität Übersichtsgrafiken und schematische Darstellungen mit Werkzeugen aus der „Diagrams as Code“-Familie (Mermaid, PlantUML) erstellen können.

## Aufgabe
Schreiben Sie eine Analyse der Chancen und Risiken des Einsatzes von Open-Source-Software sowohl im privaten als auch im unternehmerischen Umfeld.

## Spezifische Anforderungen

### Inhalt

* Der Begriff *Open-Source-Software* muss definiert werden.
* Die Analyse sollte auch quantitative Aspekte der Nutzung von Open-Source-Software behandeln. Nutzen Sie hierfür öffentlich zugängliche Quellen.
* Die Analyse muss auf die Kosten der Nutzung von Open-Source-Software eingehen.
* Die Analyse muss Sicherheitsfragen behandeln.

### Formale Anforderungen

* Die Analyse muss alle notwendigen Verzeichnisse enthalten (Inhalts-, Quellen-, Tabellen-, Abbildungsverzeichnis).
* Alle Grafiken müssen innerhalb der Analyse erstellt werden.
* Quellen müssen zitiert werden.
* Der Einsatz von generativer KI muss deklariert werden.

### Quellen
Die folgenden Quellen können für die quantitativen Aspekte der Analyse verwendet werden:

1.  **Nutzungsstatistiken & Marktanteile**

    * **GitHub – The State of the Octoverse (2025)**: Statistiken über die Anzahl der Repositories, die aktivsten Sprachen (Python, TypeScript) und das Wachstum von KI-Projekten.
    * **Linux Foundation – World of Open Source Survey (2025)**: Fokus auf die Einführung in Unternehmen und Regierungen.
    * **W3Techs – Web Technology Surveys**: Echtzeitdaten zur Nutzung von Webservern (Nginx, Apache) und Betriebssystemen im Web.

2.  **Ökonomische Aspekte & Kosten (TCO)**

    * **State of Open Source Report (Perforce/OSI)**: Jährliche Umfrage unter IT-Entscheidungsträgern zu den Gründen für den Einsatz von OSS.
    * **Quandary Peak Research (2025)**: Wissenschaftliche Analyse des wirtschaftlichen Wertes von OSS.

3.  **Sicherheit & Risiken**

    * **Synopsys (Black Duck) – Open Source Security and Risk Analysis (OSSRA) Report**: Analyse von über 1.000 kommerziellen Codebasen auf Sicherheitsanfälligkeiten und Lizenzkonflikte.
    * **Tidelift – State of the Open Source Maintainer Report**: Beleuchtet die „Risikoseite“ der Wartung (Supply Chain Security).

### Bewertung
Die Arbeit wird nach den folgenden Kriterien bewertet:

| Kriterium | Gewicht | 3 Punkte (Sehr gut) | 2 Punkte (Genügend) | 1 Punkt (Ungenügend) |
| :--- | :--- | :--- | :--- | :--- |
| **Nutzung von Markdown & Jupyter** | 25% | Notebook sauber strukturiert, Code/Text integriert, Ergebnisse reproduzierbar. | Notebook funktioniert, hat aber Mängel in Struktur oder Reproduzierbarkeit. | Notebook unvollständig, Code läuft nicht oder ist vom Text getrennt. |
| **Datenvisualisierung** | 20% | Mind. zwei aussagekräftige Grafiken, korrekt beschriftet, im Text interpretiert und zitiert. | Grafiken vorhanden, aber mit Mängeln in Beschriftung, Interpretation oder Zitat. | Keine oder fehlerhafte Grafiken; fehlender Textbezug. |
| **Diagrams as Code** | 10% | Mind. ein Diagramm (Mermaid/PlantUML) sinnvoll genutzt und korrekt gerendert. | Diagramm vorhanden, aber mit technischen oder inhaltlichen Mängeln. | Kein Diagramm oder nicht als Code erstellt. |
| **Inhaltliche Qualität** | 25% | OSS definiert, Chancen/Risiken differenziert, Kosten/Sicherheit fundiert, Quellen korrekt. | Wesentliche Inhalte vorhanden, aber Argumente oberflächlich oder lückenhaft. | Zentrale Inhalte fehlen oder sind faktisch falsch. |
| **Formale Anforderungen** | 10% | Alle Verzeichnisse vorhanden, Quellen vollständig, KI-Deklaration vorhanden. | Kleine Lücken in Verzeichnissen, Zitaten oder Umfang. | Wesentliche formale Anforderungen nicht erfüllt. |
| **Sprache & Darstellung** | 10% | Klarer, präziser Ausdruck; korrekte Fachterminologie; gute Lesbarkeit. | Verständlich, aber sprachliche oder gestalterische Mängel. | Schwer verständlich oder durchgehend fehlerhaft. |

### Allgemeine Informationen

* **Abgabefrist**: 13. März 2026.
* **Tech Stack**: Jupyter Notebooks mit Python und Quarto.
* **Format**: Abgabe als PDF oder HTML inkl. aller Quelldateien (.qmd, .ipynb, .yml, Bilder/Daten).
* **Konfiguration**: [Eine `_quarto.yml` Datei mit der Basiskonfiguration für PDF wird bereitgestellt](quarto.yml).

## Kontakt
Fragen beantworte ich während des Unterrichts, via Teams oder nach Terminvereinbarung während der Sprechstunde.
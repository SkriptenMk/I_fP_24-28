# Jupyter Notebook 

In einem Jupyter Notebook kann Text mit ausführbarem Programmcode
kombiniert werden. Wir werden Jupyter Notebooks für die
Anwendungsübungen im Unterricht verwenden.

## Installationsanleitung

Hier ist eine Schritt-für-Schritt-Anleitung zur Installation von Jupyter
Notebooks: 

1. Öffnen Sie die Windows-Eingabeaufforderung (cmd).
2. Wechseln Sie mit  
   ```sh
   cd \Pfad\zum\Arbeitsverzeichnis
   ```  
   in Ihr Arbeitsverzeichnis.

3. Starten Sie eine Python Virtual Environment  
   ```sh
   python -m venv venv

   venv\Scripts\activate
   ```

4. Geben Sie folgenden Befehl ein und drücken Sie Enter:
   ```sh
   python -m pip install jupyter
   ```

   Die Installation braucht etwas Zeit. Haben Sie Geduld mit Ihrem Computer.

   Falls pip aus irgendeinem Grund nicht installiert wurde oder nicht
   funktioniert, können Sie es manuell installieren, indem Sie den
   folgenden Befehl in der Eingabeaufforderung ausführen:
   
   ```sh
   python -m ensurepip --upgrade
   ```

   Dieser Befehl stellt sicher, dass pip installiert und auf dem
   neuesten Stand ist. 

## Jupyter Notebook starten

1. Öffnen Sie erneut die Eingabeaufforderung/das Terminal.

2. Geben Sie ein:
   ```
   jupyter notebook
   ```

3. Drücken Sie Enter. Ihr Standardbrowser öffnet sich automatisch mit der Jupyter Notebook-Oberfläche.

## Ihr erstes Notebook erstellen

1. Klicken Sie in der Jupyter-Oberfläche auf "New" und wählen Sie "Notebook".
2. Wählen Sie im Pop-up Fenster "Python 3 (ipykernel)" und bestätigen
   Sie mit select.

3. Ein neues Notebook öffnet sich in einem neuen Tab. Der Tab trägt den
   Namen "Untitled".

4. Geben Sie in die erste Zelle etwas Python-Code ein, z.B.:
   ```python
   print("Hallo Jupyter!")
   ```

5. Drücken Sie Shift+Enter, um die Zelle auszuführen.

## Tipps zur Verwendung

- Verwenden Sie "Code"-Zellen für Python-Code und "Markdown"-Zellen für Text.
- Speichern Sie Ihr Notebook regelmäßig mit dem Disketten-Symbol oder Strg+S.
- Schließen Sie das Browserfenster und geben Sie in der
  Eingabeaufforderung/im Terminal Strg+C ein, um  Jupyter zu beenden.

Glückwunsch! Sie haben nun Jupyter Notebooks installiert und können
damit arbeiten. Erkunden Sie weitere Funktionen und Möglichkeiten,
während Sie sich mit dem Tool vertraut machen. 

## Bearbeiten von Jupyter Notebooks in VS Code

1. Jupyter-Erweiterung installieren:  
   - Suchen Sie im Erweiterungen-Bereich nach "Jupyter"
   - Installieren Sie die Erweiterung "Jupyter" von Microsoft

2. Neues Jupyter Notebook erstellen:
   - Drücken Sie Strg+Shift+P, um die Befehlspalette zu öffnen
   - Geben Sie "Jupyter: Create New Jupyter Notebook" ein und wählen Sie diesen Befehl aus
   - Ein neues Notebook wird geöffnet

3. Mit dem Notebook arbeiten:
   - Um eine neue Zelle hinzuzufügen, klicken Sie auf den "+ Code" Button oben im Notebook
   - Geben Sie Ihren Python-Code in die Zelle ein
   - Um den Code auszuführen, klicken Sie auf den Play-Button links neben der Zelle oder drücken Sie Shift+Enter
   - Die Ausgabe erscheint direkt unter der Zelle

4. Notebook speichern:
   - Gehen Sie auf Datei > Speichern unter
   - Wählen Sie einen Speicherort und geben Sie einen Namen mit der Endung .ipynb ein

5. Bestehendes Notebook öffnen:
   - Gehen Sie auf Datei > Öffnen
   - Navigieren Sie zu Ihrem .ipynb-File und öffnen Sie es

Tipps:
- Sie können zwischen Code- und Markdown-Zellen wechseln, indem Sie auf den Zellentyp oben im Notebook klicken
- Nutzen Sie die Befehlspalette (Strg+Shift+P), um weitere Jupyter-bezogene Befehle zu finden


*Dieser Text wurde mit Hilfe von Perplexity.ai erstellt.*
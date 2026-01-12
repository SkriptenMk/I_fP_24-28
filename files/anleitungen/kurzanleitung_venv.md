# Anleitung zum Arbeiten mit Python Virtual Environments

Eine Python Virtual Environment (venv) ist eine geschützte Umgebung, in
der die Installation zusätzlicher Module zu keinen Konflikten mit dem
Gesamtsystem führen. Aus diesem Grund ist es sinnvoll, für jedes neue
Python Projekt eine solche venv anzulegen.

Hier eine Checkliste für das Arbeiten in einer venv:

Als Vorfrage ist zu prüfen, ob bereits eine venv angelegt ist.

## Arbeiten mit einer bereits bestehenden venv

1. Aktivieren der venv:
   
   ```shell
   C:\Pfad\zum\aktuellen\Ordner>venv\Scripts\activate
   ```

   Dass die venv aktiviert worden ist, erkennt man daran, dass das
   Terminal folgenden Prompt aufweist:

   ```shell
   (venv) C:\Pfad\zum\aktuellen\Ordner>
   ```

2. Jupyter Server starten:
   
   ```shell
   (venv) C:\Pfad\zum\aktuellen\Ordner>jupyter notebook
   ```

   Das Terminal, in welchem der Jupyter Server gestartet wurde, darf
   **nicht** geschlossen werden.

3. Arbeiten am Projekt
4. Jupyter Server deaktivieren.
   
   Der Jupyter Server kann im Terminal, in welchem er gestartet wurde,
   mit der Tastenkombination [Ctrl] + [C] angehalten werden.

5. venv deaktivieren
   
   ```shell
   (venv) C:\Pfad\zum\aktuellen\Ordner>deactivate
   ```

## Einrichten einer neuen venv

1. Projektordner erstellen
2. venv anlegen:
   
   ```shell
   C:\Pfad\zum\aktuellen\Ordner>python -m venv venv
   ```
3. Aktivieren der venv:
   
   ```shell
   C:\Pfad\zum\aktuellen\Ordner>venv\Scripts\activate
   ```

   Dass die venv aktiviert worden ist, erkennt man daran, dass das
   Terminal folgenden Prompt aufweist:

   ```shell
   (venv) C:\Pfad\zum\aktuellen\Ordner>
   ```

4. Installieren der erforderlichen Pakete:
   
   ```shell
   (venv) C:\Pfad\zum\aktuellen\Ordner>python -m pip install jupyter (und allfällige andere Pakete)
   ```

5. Jupyter Server starten:
   
   ```shell
   (venv) C:\Pfad\zum\aktuellen\Ordner>jupyter notebook
   ```

   Das Terminal, in welchem der Jupyter Server gestartet wurde, darf
   **nicht** geschlossen werden.

6. Arbeiten am Projekt
7. Jupyter Server deaktivieren.
   
   Der Jupyter Server kann im Terminal, in welchem er gestartet wurde,
   mit der Tastenkombination [Ctrl] + [C] angehalten werden.

8. venv deaktivieren
   
   ```shell
   (venv) C:\Pfad\zum\aktuellen\Ordner>deactivate
   ```
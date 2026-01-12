# Python Sockets: Ein Einfaches Client-Server Beispiel


In diesem Abschnitt untersuchen wir, wie man eine einfache
Client-Server-Anwendung mit Python-Sockets erstellt. Dieses Beispiel
wird die grundlegenden Konzepte der Socket-Programmierung demonstrieren,
einschliesslich der Herstellung einer Verbindung sowie des Sendens und
Empfangens von Daten. 

:::{note} Network Socket
Ein Netzwerk-Socket ist ein Endpunkt innerhalb eines Hosts, der zum
Senden und Empfangen von Daten über ein Netzwerk verwendet wird.
:::

## Struktur der Verbindung

Das Beispiel besteht aus einem Server, der auf eingehende Verbindungen
wartet, und einem Client, der sich mit dem Server verbindet. Wir werden
die Kommunikation als einfachen Chatdienst modellieren. 

## Server Code

Sie benötigen keine virtuelle Umgebung. Das Beispiel verwendet nur die
Python-Standardbibliothek.  
Unten ist das funktionierende Codebeispiel für den
<a
href="https://github.com/SkriptenMk/I_fP_24-28/blob/main/docs/250905/socket_server.py"
download="socket_server.py">Socket-Server</a>:

```python
:linenos:
# socket_server.py

import socket

def server_program():
    # define host name and port
    host = 'localhost'    # for communication on the local machine
    port = 5000           # use a port number above 1024
    
    # create socket
    server_socket = socket.socket()
    
    # bind the socket to the host and port
    server_socket.bind((host, port))
    
    # set the server to listen for connections
    server_socket.listen(2) # start listening 
                            # with a backlog of 2 
                            # (max queued connections)
    
    # accept new connection from client
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    
    while True:
        # receive up to 1024 bytes per call
        data = conn.recv(1024).decode()
        if not data:
            # if no data is received, break
            break
        print("Received from connected client: " + str(data))
        # prompt the user to enter a message
        data = input(' -> ')
        # send data to the client as bytes
        conn.send(data.encode())
        
    # close the connection
    conn.close()
    
if __name__ == '__main__':
    server_program()
```

Um das Skript direkt auszuführen, öffnen Sie ein Terminal im
Verzeichnis, in dem sich das Skript befindet, und führen Sie den
folgenden Befehl aus: 

```bash
python socket_server.py
```

Was geschieht, wenn das Skript ausgeführt wird, wird in den folgenden
Abschnitten erläutert. 

Der Code besteht aus zwei Hauptteilen: der Funktion `server_program` und
dem Block `if __name__ == '__main__'`. Die Funktion `server_program`
enthält die Hauptlogik für den Server, während der `if`-Block verwendet
wird, um den Servercode auszuführen, wenn das Skript direkt ausgeführt
wird. 

Wenn Sie das Skript ausführen, importiert Python zuerst das
`socket`-Modul. 

```python
import socket
```

Als nächstes wird die Funktion `server_program` aufgerufen. Innerhalb
dieser Funktion wird als erstes die Hostadresse und der Portnummer
definiert. `localhost` ist eine spezielle Adresse, die auf die lokale
Maschine verweist. `localhost` entspricht der IPv4-Adresse
`127.0.0.1`. Das bedeutet, dass der Server nur Verbindungen von Clients
akzeptiert, die auf derselben Maschine ausgeführt werden. Dies ist eine
Simulation eines Netzwerks. 

```python
def server_program():
    # define host name and port
    host = 'localhost'    # for communication on the local machine
    port = 5000           # use a port number above 1024
```

Im nächsten Code-Snippet wird der `server_socket` mit der Funktion
`socket.socket()` erstellt, die ein neues Socket-Objekt erzeugt. 

```python
server_socket = socket.socket()
```

Dieses Socket wird verwendet, um auf eingehende Verbindungen von Clients
zu hören. Damit die Verbindung funktioniert, muss der `server_socket`
mit der Host- und Portnummer über die `bind()`-Methode verbunden werden. 

```python
server_socket.bind((host, port))
```

Als nächstes wird der Server so eingestellt, dass er mit der
`listen()`-Methode auf eingehende Verbindungen wartet. 

```python
server_socket.listen(2) # start listening 
                        # with a backlog of 2 
                        # (max queued connections)
```

Der Server erstellt ein backlog von 2 ausstehenden Verbindungen. Der
Code akzeptiert jedoch genau eine Client-Verbindung (accept() wird
einmal aufgerufen). Um mehrere Clients zu verarbeiten, rufen Sie
accept() in einer Schleife auf und verwenden Sie Threads oder asyncio.
Dieses Limit wird festgelegt, um zu verhindern, dass der Server von zu
vielen Verbindungen auf einmal überwältigt wird. Die `accept()`-Methode
wird verwendet, um eine neue Verbindung von einem Client zu akzeptieren.
Diese Methode gibt ein Tupel mit zwei Elementen zurück: `conn`, ein neues
Socket-Objekt für die Kommunikation mit dem Client, und `address`, die
Adresse des Clients. Der nächste Abschnitt zeigt, wie eine Nachricht
ausgegeben wird, um die Adresse des verbundenen Clients anzuzeigen.

```python
conn, address = server_socket.accept()
print("Connection from: " + str(address))
```

Die while-Schleife ermöglicht es dem Server, auf Daten vom Client zu
warten. Die `recv()`-Methode wird verwendet, um Daten vom Client zu
empfangen. Jeder `recv()`-Aufruf liest bis zu 1024 Bytes; zusätzliche
Daten bleiben im Puffer und können durch nachfolgende Aufrufe gelesen
werden. Wenn keine Daten empfangen werden, bricht der Server die
Schleife ab und schliesst die Verbindung. 

```python
while True:
        # receive up to 1024 bytes per call
        data = conn.recv(1024).decode()
        if not data:
            # if no data is received, break
            break
        
```

Wenn der Server Daten empfängt, gibt er die Daten in der Konsole aus und
fordert den Benutzer auf, eine Antwort einzugeben. Die Antwort wird mit
der `send()`-Methode an den Client zurückgesendet. 

```python
print("Received from connected client: " + str(data))
        # prompt the user to enter a message
        data = input(' -> ')
        # send data to the client as bytes
        conn.send(data.encode())
```

## Client Code

Unten ist der funktionierende Code des
<a
href="https://github.com/SkriptenMk/I_fP_24-28/blob/main/docs/250905/socket_client.py"
download="socket_client.py">
Client-Beispiels</a>:

```python
:linenos:
# socket_client.py

import socket

def client_program():
    # define host name and port (of the server to connect to)
    host = 'localhost'  # as both pieces of code are 
                        # running on the same machine
    port = 5000         # socket server port number
    
    # create socket
    client_socket = socket.socket()
    
    # connect to the server
    client_socket.connect((host, port))
    
    # prompt the user to enter a message
    message = input(" -> ")  # take input
    
    # message loop
    while message.lower().strip() != 'bye':
        # send message to the server as bytes
        client_socket.send(message.encode())
        
        # receive response from the server
        data = client_socket.recv(1024).decode()
        
        print('Received from server: ' + data)
        
        # prompt the user to enter a new message
        message = input(" -> ")  # take new input
        
    # close the connection
    client_socket.close()
    
if __name__ == '__main__':
    client_program()
```

Um dieses Skript auszuführen, befolgen Sie die gleichen Schritte wie für
das Server-Skript. Öffnen Sie ein Terminal im Verzeichnis, in dem sich
das Skript befindet, und führen Sie den folgenden Befehl aus: 

```bash
python socket_client.py
```

Starten Sie den Server, bevor Sie den Client starten. Wenn der Server
nicht läuft, wird client_socket.connect(...) einen
ConnectionRefusedError auslösen. 

Wenn Sie das Skript ausführen, importiert Python zuerst das Modul
`socket`. 

Als nächstes wird die Funktion `client_program` aufgerufen. Innerhalb
dieser Funktion wird die erste Aktion die Definition der Hostadresse und
der Portnummer. Hier müssen die Hostadresse und die Portnummer mit denen
im Server-Skript übereinstimmen. 

Nachdem die Host- und Portinformationen definiert sind, erstellt der
Client ein Socket-Objekt mit der Funktion `socket.socket()`. Dieses
Socket wird verwendet, um eine Verbindung zum Server herzustellen. Die
Methode `connect()` wird auf dem Socket-Objekt aufgerufen, um eine
Verbindung zum Server herzustellen. 

Sobald die Verbindung hergestellt ist, betritt der Client eine Schleife,
in der er Nachrichten an den Server senden und Antworten empfangen kann.
Der Client fordert den Benutzer auf, eine Nachricht einzugeben, die dann
mit der Methode `send()` an den Server gesendet wird. Der Client wartet
auch auf eine Antwort vom Server, indem er die Methode `recv()`
verwendet. 

Wenn der Benutzer `bye` eingibt, verlässt der Client die Schleife und
schliesst die Verbindung zum Server.

## Verbindung im LAN

Um die beiden Skripte im lokalen Netzwerk (LAN) zu verwenden, muss in
beiden Skripten die IPv4-Adresse des Servers anstelle von `localhost`
verwendet werden.  
Die IPv4-Adresse des Servers kann durch Ausführen des folgenden Befehls
im Terminal des Servers ermittelt werden:

```bash
C:\Users\username>ipconfig
Windows IP Configuration
...
Wireless LAN adapter Wi-Fi:
   Connection-specific DNS Suffix  . . . :
   IPv4 Address . . . . . . . . . . . . .: 192.168.1.2
   Subnet Mask . . . . . . . . . . . . . : 255.255.255.255
   Default Gateway . . . . . . . . . . . : 192.168.1.1
...
```

Die Ausgabe des Befehls `ipconfig` zeigt alle Netzwerkadapter des
entsprechenden Computers an. Die dargestellte Ausgabe hier im Beispiel
wurde gekürzt.  
Die IPv4-Adresse des Servers ist in diesem Fall `192.168.1.2`.

Diese ist die Adresse, welche in beiden Skripten anstelle von `localhost` verwendet
werden muss. Dann kann innerhalb des lokalen Netzwerks eine Verbindung
hergestellt werden.


## Fazit

Die vorgestellten Codebeispiele veranschaulichen, wie Pythons
integriertes Socket-Modul (Standardbibliothek) eine unkomplizierte
Implementierung von netzwerkbasierten Anwendungen ermöglicht, ohne
externe Abhängigkeiten zu erfordern. Der Fokus des Tutorials auf die
Kommunikation über localhost bietet eine sichere, kontrollierte Umgebung
für Experimente und Lernen, während der bidirektionale
Nachrichtenaustausch reale Kommunikationsmuster demonstriert, die in
Produktionssystemen zu finden sind. 

Zu den wichtigsten Erfolgen dieser Implementierung gehören:

* Erfolgreiche Herstellung von TCP-Socket-Verbindungen zwischen
  separaten Prozessen 
* Implementierung einer nachrichtenbasierten Kommunikation mit
  ordnungsgemässer Kodierung/Dekodierung 
* Demonstration des Verbindungslebenszyklusmanagements von der
  Herstellung bis zur Beendigung 
* Erstellung einer einfachen Befehlszeilenschnittstelle für sowohl
  Server- als auch Clientanwendungen 

Das Wissen, das aus diesem Tutorial gewonnen wurde, dient als solide
Grundlage für die Entwicklung anspruchsvollerer netzwerkbasierter
Anwendungen. Zukünftige Verbesserungen könnten die Implementierung von
Multithreading für die gleichzeitige Verarbeitung mehrerer Clients, die
Hinzufügung von Fehlerbehandlungs- und Wiederverbindungslogik oder die
Erweiterung des Kommunikationsprotokolls zur Unterstützung
strukturierter Datenformate umfassen. 

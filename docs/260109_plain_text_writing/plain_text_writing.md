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
Markdown oder $\LaTeX$).
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

## Plain Text Formate für die Textredatktion

Die einfachste Form eines Textfiles ist eine `.txt` Datei. Dabei handelt
es sich in der Regel um reinen Text ohne Formatierungen. Das Bedürfnis
nach formatierten Textdarstellungen hat zu verschiedenen Dateiformaten
geführt. Dazu gehören zum Beispiel HTML-Dateien (`.html` oder `.htm`:
**H**yper **T**ext **M**arkup **L**anguage).
Dieses Format wurde ursprünglich unter anderem auch dazu geschaffen,
Text formatiert am Bildschirm darzustellen. Ein anderes Beispiel ist
$\LaTeX$. Auch $\LaTeX$ ist eine sogenannte Auszeichnungssprache (Markup
Language). Allerdings ist das Zielmedium von $\LaTeX$ weniger der
Bildschirm sondern eher der Druck, heute vor allem das Portable Document
Format (PDF), welches sich zum Quasi-Standard entwickelt hat.

Allerdings ist der Umfang der Formatierungsmöglichkeiten sowohl in HTML
wie auch in $\LaTeX$ so umfangreich, dass die Hürde für deren Verwendung
relativ hoch ist.

Vor diesem Hintergrund ist eine eher minimalistische
Auszeichnungssprache, Markdown (`.md`) geschaffen worden. Diese stellt
alle wesentlichen Formatierungsmöglichkeiten, wie zum Beispiel
hierarchische Überschriften oder das setzen von kursivem Text, direkt
zur Verfügung. Dort wo die Formatierungsmöglichkeiten den Bedürfnissen
nicht genügen, kann in vielen Fällen auf HTML oder $\LaTeX$
Auszeichnungen zurückgegriffen werden.
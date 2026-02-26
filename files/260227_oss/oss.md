# Open-Source-Software

Für die meisten Computernutzer gibt es zwei Alternativen hinsichtlich ihrer Arbeitsumgebung: Entweder man arbeitet an einem PC und nutzt Windows, oder man arbeitet an einem Apple-Gerät und nutzt macOS oder iOS. Beiden Varianten ist gemeinsam, dass man mit proprietärer Software arbeitet. Im Kontext von Software bedeutet proprietär, dass es sich um herstellerspezifische Software handelt, deren Quellcode geheim ist.

Neben diesen bekannten Betriebssystemen und den darauf aufgebauten Software-Ökosystemen existiert ein Paralleluniversum aus Open-Source-Software. Während Open-Source-Betriebssysteme auf Desktop-Computern ein Nischendasein fristen, stellen sie auf Servern die Mehrheit dar, was von der breiten Öffentlichkeit weitgehend unbemerkt bleibt. Auch im Bildungsbereich erfreut sich Open-Source-Software einer gewissen Beliebtheit.

::: {.callout-note}
## Was ist Open-Source-Software

Open-Source-Software (kurz OSS) umfasst zwei Aspekte:

1. Der Quellcode der Software ist öffentlich. Dies erlaubt es, die Funktionsweise der Software zu untersuchen.
2. Open-Source-Software kann frei verwendet, weiterverbreitet **und** verändert werden.

Dies ist von Freeware zu unterscheiden. Freeware ist Software, die genutzt werden darf, ohne dafür bezahlen zu müssen. Der Quellcode ist jedoch nicht zugänglich und darf (was aufgrund des verborgenen Quellcodes ohnehin kaum möglich wäre) nicht verändert werden.
:::

## Nutzung von Open-Source-Software

Die bekannteste Nutzung von Open-Source-Software ist der Einsatz von Linux als Server-Betriebssystem. AWS, das Cloud-Computing-Produkt von Amazon, bietet Kunden nicht nur virtuelle Linux-Server an [@AmazonLinux2023], sondern läuft intern auf einem spezialisierten Linux-System [@AWS_Nitro]. Microsofts Gegenstück Azure läuft intern auf einem Windows-Server-System; die von Kunden am häufigsten gekauften Lösungen sind jedoch ebenfalls Linux-Server [@AzureLinux].

Supercomputer wie der Alps-Supercomputer (derzeit – Februar 2026 – Platz 8 der Weltrangliste der leistungsstärksten Computer) laufen ebenfalls mit Linux als Betriebssystem.

Android ist gleichermaßen eine Variante von Linux und basiert daher im Kern auf Open-Source-Software.

Besonders verbreitet ist Open-Source-Software jedoch in den unzähligen Chips von Smart-Geräten, die die Basis für das Internet der Dinge (Internet of Things) bilden.

## Beispiele für Open-Source-Software

Bekannte Beispiele für etablierte Open-Source-Software sind der Firefox-Browser und die Programmiersprache Python. Diese beiden Beispiele zeigen, dass Open-Source-Software in vielen Bereichen ebenso leistungsfähig ist wie ihre proprietären Gegenstücke. Mit einem Marktanteil von ca. 3 % im Jahr 2025 ist Firefox zwar nur noch ein Schatten seiner selbst, dennoch bleibt Firefox ein bekannter und etablierter Browser. Im Gegensatz dazu ist Python laut dem Tiobe-Ranking [@TIOBE26-02] mit einem Anteil von gut 20 % der Suchanfragen die mit Abstand bedeutendste Programmiersprache[^1].

## Open-Source-Lizenzen

Man muss zwischen verschiedenen Open-Source-Lizenzen unterscheiden. Das strengste Prinzip wird als Copyleft bezeichnet. Lizenzen, die diesem Prinzip folgen, verlangen, dass alle Produkte, die auf einer so lizenzierten Software basieren, ebenfalls mit einem Copyleft versehen werden müssen. Dies steht im Gegensatz zum üblichen Verständnis von Copyright, mit dem Urheber in der Regel die Nutzung ihres geistigen Eigentums einschränken wollen. Ein Beispiel für diese Lizenz ist die GNU General Public License (GPL). Es gibt jedoch auch Open-Source-Lizenzen, die eine weitgehend freie Nutzung, Modifikation und Weiterverbreitung erlauben, insbesondere in proprietären Anwendungen. Ein Beispiel hierfür ist die MIT-Lizenz (benannt nach dem Massachusetts Institute of Technology, MIT).

## Geschäftsmodelle auf Basis von Open-Source-Software

Entgegen weit verbreiteter Annahmen ist es möglich, mit Software Geld zu verdienen, die den Nutzern kostenlos zur Verfügung gestellt wird. Viele der entsprechenden Geschäftsmodelle basieren darauf, dass Unternehmen Beratung für den Einsatz ihrer IT-Infrastruktur benötigen – unabhängig davon, ob es sich um proprietäre Software oder Open-Source-Software handelt. Software muss fast immer an die spezifischen Gegebenheiten des jeweiligen Unternehmens angepasst werden. Durch diese Anpassungsleistungen kann Geld verdient werden.

Ein weiteres Geschäftsmodell – wenn auch nicht spezifisch für Open-Source-Software – ist das sogenannte Freemium-Modell. Dabei wird ein Teil der Leistung kostenlos angeboten, während der volle Funktionsumfang kostenpflichtig ist. Zotero stellt ein Beispiel für dieses Modell dar. Zotero ist grundsätzlich kostenlos nutzbar. Möchte man jedoch mehr als ein bestimmtes Maximum an Daten synchronisieren, muss für den entsprechenden Speicherplatz eine Gebühr entrichtet werden.

Andere Modelle unterscheiden zwischen privater und kommerzieller Nutzung. Die private Nutzung ist dann kostenlos, während für die kommerzielle Nutzung eine Lizenzgebühr gezahlt werden muss.

## Ausblick

Eine vertiefte Auseinandersetzung mit Open-Source-Software ergibt sich aus der Aufgabe im folgenden Abschnitt.

[^1]: Zur Kritik am Tiobe-Index vgl. [Wikipedia zu Tiobe](https://en.wikipedia.org/wiki/TIOBE_index#Criticism)
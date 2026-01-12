# Sichere Verschlüsselung mit Vigenère: One-Time-Pad

Es hat sich gezeigt, dass es zwar rund 300 Jahre gedauert hat, bis die Viginère
Chiffre gebrochen werden konnte. Mit Hilfe von statistischen Methoden ist dies
jedoch möglich. Wie das hier verlinkte Jupyter Notebook zeigt, ist der Aufwand
überschaubar. Die Idee, mit der die Viginère Chiffre gebrochen werden kann,
beruht auf den statistischen Eigenheiten der Sprache, in welcher die Nachricht
verfasst worden ist.

Eine sichere Verschlüsselung muss daher darauf abzielen, die statistischen
Eigenschaften der Sprache, in welcher die Nachricht verfasst wurde, zu
verwischen. Dies kann erreicht werden, indem der Schlüssel mindestens so lang
ist, wie die Nachricht selbst. Darüber hinaus muss der Schlüssel aus einer
zufälligen Zeichenfolge bestehen und darf nur ein einziges Mal verwendet werden.
Dieses Verfahren wird als One-Time-Pad bezeichnet.
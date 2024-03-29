==========
IT-rechnen
==========


Scanner
=======

#1
--

Die Package AG plant die Anschaffung einer kleinen Fertigungslinie für Karton, welche mit einer Arbeitsbreite von **508 mm** und einer Produktionsgeschwindigkeit von **30,48 m/min** Karton auf Rollen produziert. 
Die Anlage soll zwölf Stunden pro Tag produktiv sein.


Karton wird zum Teil aus Altpapier hergestellt, Unreinheiten wirken sich auf die Qualität des Kartons aus.
Zur Qualitätssicherung wird die erzeugte Kartonbahn fortlaufend durch eine Kamera gescannt.
Die entstandenen Bilder werden ausgewertet und anschließend gespeichert.
Bei erkannten Verfärbungen der Oberfläche oder Einschlüssen im Karton werden die aktuellen Rollen als mindere Qualität eingestuft.


* Erfasste Scanfläche: 50,80 cm breit x 30,48 cm lang
* Auflösung: 400 dpi x 400 dpi
* Farbtiefe: 16 Bit
* 1 Inch: 2,54 cm

Ermitteln Sie zunächst die Zahl der Scans/Aufnahmen pro Tag. Der Rechenweg ist anzugeben.

.. math::

    30,48 m/min \div 30,48 cm \Rightarrow 3048 cm/min \div 30,48 cm = 100 Scans/min
    
    100 Scans/min \times 60 min/h \times 12 h/Tag = 72.000 Scans/Tag


========
Hardware
========

EK Themen
=========

EVA Prinzip
-----------

.. attention::
    **EVA**
   
    **E**\ ingabe -> **V**\ erarbeitung -> **A**\ usgabe

* Zentraleinheit (Verarbeitung)
    * CPU
    * RAM
* Peripherie (Ein-/ Ausgabe)
    * Tastatur
    * Monitor
    * Externe Speichereinheit
        * Festplatte
        * Usb-Stick
        * CD/DVD

.. hint::
    **Konfiguration** 

    Konfiguration bezeichnet die Zusammenstellung, Einstellungen und Abstimmungen von
    Komponenten, Geräten und Programmen in Bezug auf die Anwendungen.


Pioniere der IT
---------------

Deutschland

* Dietmar Hopp (SAP)
* Hasso Plattner (SAP, Mäzen)
* Marco Börries (Open-Office)

und die Welt

* Bill Gates (Microsoft)
* Jeff Bezos (Amazon)
* Larry Page (Google) 


Netzteil
--------


Die "80-PLUS"-Initiative fordert für eine ihrer Zertifizierung,
dass Netzteile für Desktop-Computer und Server bei den Lastpunkten
20%, 50% und 100% jeweils einen Wirkungsgrad von mindestens 80% erreichen. [#f1]_

* 80 PLUS
* 80 PLUS Bronze
* 80 PLUS Silver
* 80 PLUS Gold
* 80 PLUS Platinum
* 80 PLUS Titanium




Anschlüsse
----------

intern 
    * Sockel (Prozessor)
    * RAM-Steckplätze
    * PCI-/PCIe-Steckplätze
    * SATA (Festplatten)
    * M.2-Port (SSD)

extern 
    * USB 
    * Firewire
    * Thunderbolt
    * PS2 (veraltet Tastatur/Maus)
    * Audio (Klinkenanschlüsse)
    * RJ45 (Netzwerk)
    * Monitor
        * VGA
        * DVI
        * HDMI
        * Display Port

Formfaktoren
------------

* ATX
* micro ATX
* Mini ATX
* Flex ATX
* Mini ITX


Komponenten
-----------

* Mainboard
* CPU 
* RAM 
* Festplatte 
* GPU (Graphics Processing Unit)
* PSU/Netzteil (Power Supply Unit)


Bauformen
---------

Serververnetzung möglich
    * Mini-PC 
    * Desktop-PC, Mini-Tower
    * Tower-PC (big, midi)
    * All-in-one-PC 
    * Notebook 
    * Tablet-PC, Convertible

Serververnetzung notwendig 
    * Thin-Client
    * Zero-Client 

Kommunikationsnetz notwendig/sinnvoll
    * Smart Tablet
    * Smartphone
    * Smart Devices


LCD-Technologie
---------------

Panel-Typen
    * TN 
        * günstig
        * schnelle Reaktionszeit
        * energiesparend 
    * VA 
        * gute Bildqualität 
        * etwas geringere Reaktionszeit
    * IPS
        * sehr gute Bildqualität 
        * 178 Grad Blickwinkel
        * hoher Preis 
    * MVA, PVA
        * min 160 Grad Blickwinkel horizontal/vertikal
        * LED, LCD, OLED

Ergonomieeigenschaften
    * Curves Screen - räumliches Erlebnis
    * Tilt - horizontale Neigung
    * Swivel - vertikale Drehbarkeit
    * Pivot - hähenverstellbar und horizontale Drehbarkeit 

Tastatur
--------

Tastaturarten
    * virtuell
    * integriert 
    * extern
    * kabelgebunden
    * Funk (verschiedene Standards)

Office etc.
    * Rubberdome-Modelle
    * einfach und funktional
    * günstig 
    * relativ leise

Mechanische Tastaturen
    * 10x haltbarer als Rubberdome 
    * Lineare mechanische Tastatur
        * durchgehendes Druckgefühl
        * kein "Click"
        * gut für Gaming
    * Taktile mechanische Tastatur
        * definierter Schaltpunkt
        * spürbares Klick-geräusch
        * besser für Büroarbeit

Funk-/Bluetooth-Tastaturen
    * zusätzliche Bewegungsfreiheit (10-15m)
    * Anschluss via USB
    * Batterie muss erneuert/geladen werden

Speicherarten
-------------

Direct Attached Storage (DAS)
    direkt angeschlossener Speicher

Storage Area Network (SAN)
    Speichernetzwerk, fasst mehrere Server zusammen

Network Attached Storage (NAS)
    eigenständiger Fileserver

Festplatten
-----------

HDD
    * drehende Magnetische Scheiben
    * beweglicher Schreib-Lesekopf
    * 2,5 oder 3,5 Zoll groß
    * bis 16TB 
SSD
    * schneller 
    * leichter
    * keine beweglichen Teile
    * kaum Wärmeentwicklung
SSHD (Hybrid)
    * 5x schneller als HDD
    * preiswert
    




RAM - Random Access Memory
--------------------------

* Größe (GB)
* Geschwindigkeit (MT/s - Megatransfers/s)
* Bandbreite (GB/s) 
* (U)DIMM -> Desktop
* SO-DIMM -> Notebook
* DRAM - Dynamic Random Access Memory
    * jedes Bit ein Kondensator
    * häufigste 
* SDRAM - Synchronous Dynamic Random Access Memory
    * getakteter DRAM
    * überträgt synchron zum Speicher-Bus
    * Takt durch System-Bus vorgegeben
    * eigene Low Power SDRAM Spezifikation
* DDR-RAM (Double Data Rate)
    * je Taktzyklus 2 Datentransfers
    * DDR2, DDR3, DDR4, DDR5... (nicht kompatibel)
* DDR-SDRAM (Double Data Rate Synchronous Dynamic Random Access Memory)
    * Weiterentwicklung von SD-RAM




CPU - Central Processing Unit
-----------------------------

Hauptprozessor (Zentraleinheit?), holt aus dem Speicher nacheinander die Befehle und veranlasst die Informationsverarbeitung, Steuerung und Kontrolle der Systeme.

* Rechenwerk (ALU - Aritmetic Logic Unit)
* Steuereinheit (CU - Control Unit)
* Speichermanager (MMU - Memory Management Unit)
* Zwischenspeicher (CPU-Cache)
    * L1-Cache
        * nicht groß (16-64KByte)
        * Speicher für Befehle und Daten getrennt
        * je schneller die CPU, umso wichtiger
        * für am häufigsten benutzten Befehle/Daten
    * L2-Cache
        * RAM Zwischenspeicher
        * je größer, umso besser für Multitasking
        * normaler Desktop lieber mehr L2 als mehr Taktrate
        * seit Speichercontroller von Chipsatz in CPU, unwichtiger
    * L3-Cache 
        * Multicore-Prozessoren meist Integrierten L3-Cache
        * verbessert Cache-Koheränz-Protokoll (gegen Inkonsistenzen bei z.B. Rückschreibfehlern)
        * dient eher der Verbessereung des Datenaustauchs, weniger als "Cache" 



ERP - Enterprise Resource Planning
----------------------------------

+----------------------------------------+---------------------+-------------------------------+
| Bereiche allgemein                     | ERP-System          | Beschreibung                  |
+========================================+=====================+===============================+
| Human Resource Management (HRM)        | Lohn und Gehalt     | "Personalmanagement"          |
+----------------------------------------+---------------------+-------------------------------+
| Customer Relationship Management (CRM) | Verkauf             | Kundenpflege                  |
+----------------------------------------+---------------------+-------------------------------+
| Manufacturing Resource Planning (MRP)  | Produktion          | Produktionsplanung/-steuerung |
+----------------------------------------+---------------------+-------------------------------+
| Supply Chain Management (SCM)          | Lager, Ein-/Verkauf | Lieferkettenmanagement        |
+----------------------------------------+---------------------+-------------------------------+
| Financial Resource Management (FRM)    | Finanzmanagement    | Finanzmanagement?             |
+----------------------------------------+---------------------+-------------------------------+



.. hint::
    
    Das System dient nicht nur dazu, unternehmensrelevante Daten 
    zu verwalten und darüber zu informieren,
    sondern auch alle notwendigen Belege und Auswertungen zu erstellen.


Energieeffizienz Siegel
-----------------------

+---------------+--------------------------------+----------------------------------------------+
||energystar|   | Energy Star                    | * aus Amerika, in Europa übernommen          |
|               |                                | * keine externe Prüfung                      |
|               |                                | * Energiesparfunktionen                      |
+---------------+--------------------------------+----------------------------------------------+
||tuv|          | TüV                            | * unabhängiges Prüfinstitut                  |
|               |                                | * Einhaltung ökologischer Standards im Büro  |
|               |                                | * z.B. Schadstoffe, Energieverbrauch         |
+---------------+--------------------------------+----------------------------------------------+
||ecolabel|     | europäisches Umweltzeichen     | * von Europäischen Kommision initiiert       |
|               |                                | * zertifiziert Produkte & Dienstleistungen   |
|               |                                | * für geringe Umwelt-/Gesundheitsbelastungen |
+---------------+--------------------------------+----------------------------------------------+
||tco|          | TCO certified                  | * Qualität von Produkten im Büro             |
|               |                                | * z.B. Monitore, Notebooks, Server           |
|               |                                | * Kontrolle stichprobenartig                 |
+---------------+--------------------------------+----------------------------------------------+
||energieklasse|| Energieverbrauchskennzeichnung | * Europäischer Wirtschaftsraum               |
|               |                                | * ermöglicht Vergleiche                      |
|               |                                | * 03/21 erneuert, EPREL Produktdatenbank     |
+---------------+--------------------------------+----------------------------------------------+
||blauerengel|  | Blauer Engel                   | * an effiziente Geräte                       |
|               |                                | * z.B. Notebook, Computer, Monitor           |
|               |                                | * renomiert im Bereich Green-IT              |
+---------------+--------------------------------+----------------------------------------------+






BIOS
CLK
Betriebssystem
VMM
Apps
EPROM
Chipsatz


.. [#f1] https://de.wikipedia.org/wiki/80_PLUS

.. |energystar| image:: http://homeenergyrx.com/wp-content/uploads/2014/06/469px-Energy_Star_logo.svg_.png
.. |tuv| image:: https://www.luebbering-umwelttechnik.de/wordpress/wp-content/uploads/2017/05/logo-tuev-rheinland-500x500.png
.. |ecolabel| image:: https://mauvilac.com/wp-content/uploads/2019/09/Ecolabel-logo-600x600.png 
.. |tco| image:: https://www.yaacool-bio.de/uploads/tx_zimt/article_pics/TCOCertified_logo.jpg
.. |energieklasse| image:: http://www.energiesparende-geraete.de/wp-content/uploads/2011/12/energieeffizienzklassen-300x300.jpg
.. |blauerengel| image:: https://aussiedlerbote.de/wp-content/uploads/2018/10/Der-blaue-Engel.jpg
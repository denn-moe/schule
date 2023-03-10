
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


CPU
RAM
BIOS
CLK
Betriebssystem
VMM
Apps
EPROM
Chipsatz


.. [#f1] https://de.wikipedia.org/wiki/80_PLUS


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


CPU
RAM
BIOS
CLK
Betriebssystem
VMM
Apps
EPROM
Chipsatz

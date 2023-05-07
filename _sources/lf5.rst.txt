..role:: hl_ora

##########
Lernfeld 5
##########


Sequenzdiagram
--------------

.. uml::
    
    !include https://raw.githubusercontent.com/denn-moe/schule/main/source/_static/onedark.puml
   
    participant ":Client" as client 
    participant ":Router" as router 
    participant ":Firewall extern" as extern 
    participant ":Webserver" as server 
    participant ":Firewall intern" as intern 

    client -> router: Anfrage stellen 
    activate router 

    router -> intern: Anfrage weiterleiten
    activate intern

    intern --> extern: Zieladresse in Routingtabelle
    activate extern

    extern -> server: Anfrage stellen 






Aufgaben
========

Vervollständige das Diagramm
-----------------------------


test in :hl_ora:`einer anderen farbe`...

.. admonition:: Aufgabe
    :class: warning

        * Erstellen Sie eine Klasse mit dem Namen AbfrageServer.
        * Legen Sie eine private Methode mit dem Namen BackupDaten an.
        * Legen Sie die privaten Attribute Archivtyp, Speicherkapazität und Datum an.
        * Stellen Sie eine Assoziation zwischen den Klassen AbfrageServer und Datenbank her.


.. container:: only-dark

    .. uml::

        !include https://raw.githubusercontent.com/denn-moe/schule/main/source/_static/onedark.puml
        skinparam classAttributeIconSize 0


        class AnzeigeGUI {
        + TemplateName
        + GUITemplate_laden()
        }

        class DatenbankConnect {
        - Nutzername
        - Passwort
        - Datenbank
        - DBConnect()
        - DBClose()
        + DBQuerry()
        }
        class __________ {


        ---


        }

        AnzeigeGUI "1" - "*" DatenbankConnect
        DatenbankConnect -[hidden]-> __________



.. container:: only-light

    .. uml::

        skinparam classAttributeIconSize 0


        class AnzeigeGUI {
        + TemplateName
        + GUITemplate_laden()
        }

        class DatenbankConnect {
        - Nutzername
        - Passwort
        - Datenbank
        - DBConnect()
        - DBClose()
        + DBQuerry()
        }
        class __________ {


        ---


        }

        AnzeigeGUI "1" - "*" DatenbankConnect
        DatenbankConnect -[hidden]-> __________



.. dropdown:: Lösung

    .. container:: only-light

        .. uml::
            
            skinparam classAttributeIconSize 0

            class AnzeigeGUI {
                + TemplateName
                + GUITemplate_laden()
            }

            class DatenbankConnect {
                - Nutzername
                - Passwort
                - Datenbank
                - DBConnect()
                - DBClose()
                + DBQuerry()
            }
            class AbfrageServer {
                - archivtyp
                - speicherKapazitaet
                - datum
                - BackupDaten()
            }


            AnzeigeGUI "1" - "*" DatenbankConnect
            DatenbankConnect -- AbfrageServer

    

    .. container:: only-dark

        .. uml::
            
            !include https://raw.githubusercontent.com/denn-moe/schule/main/source/_static/onedark.puml
            skinparam classAttributeIconSize 0

            class AnzeigeGUI {
                + TemplateName
                + GUITemplate_laden()
            }

            class DatenbankConnect {
                - Nutzername
                - Passwort
                - Datenbank
                - DBConnect()
                - DBClose()
                + DBQuerry()
            }
            class AbfrageServer {
                - archivtyp
                - speicherKapazitaet
                - datum
                - BackupDaten()
            }


            AnzeigeGUI "1" - "*" DatenbankConnect
            DatenbankConnect -- AbfrageServer



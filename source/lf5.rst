
##########
Lernfeld 5
##########

Aufgaben
========

Vervollständige das Diagramm
-----------------------------

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



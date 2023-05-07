=========
Diagramme
=========



**************
Gantt Diagramm
**************

Aufgaben
========

#1
--

Ab dem 05.05.2014 sollen in zwei Arbeitstagen die Anforderungskriterien für die Druckerauswahl in Mitarbeitergesprächen festgelegt werden.
Danach werden Angebote eingeholt.
Bis zum Eintreffen der Angebote werden fünf Arbeitstage eingeplant.
Anschließend sollen die Angebote ausgewertet und der Auftrag erteilt werden.
Dafür sind zwei Arbeitstage vorgesehen.
Für die Auslieferung sind vier Tage geplant.
Zum Anschließen der Drucker in das Firmennetz muss die Vernetzung durch eine externe Firma erweitert werden.
Die Netzwerkerweiterung soll am 19.05.2014 beginnen.
Für die Erweiterung plant die externe Firma drei Arbeitstage.
Nach der Auslieferung des Druckers werden zwei Tage für den Aufbau der Drucker eingeplant.
Gleichzeitig soll die Software an einem Tag installiert werden.
Unmittelbar nach dem Aufbau der Drucker und der erfolgreichen Softwareinstallation soll mit der Konfiguration begonnen werden.
Die Konfiguration soll nach zwei Tagen abgeschlossen sein.
Anschließend erfolgt an einem Tag die Testphase.
Danach kann die Inbetriebnahme erfolgen.


.. dropdown:: hint

    Ab dem :bdg-primary-line:`05.05.2014` sollen in :bdg-primary-line:`zwei Arbeitstagen` die :bdg-secondary-line:`Anforderungskriterien` für die Druckerauswahl in Mitarbeitergesprächen :bdg-secondary-line:`festgelegt` werden.
    :bdg-primary-line:`Danach` werden :bdg-secondary-line:`Angebote eingeholt`.
    Bis zum Eintreffen der :bdg-secondary-line:`Angebote` werden :bdg-primary-line:`fünf Arbeitstage` eingeplant.
    :bdg-primary-line:`Anschließend` sollen die Angebote ausgewertet und der :bdg-secondary-line:`Auftrag erteilt` werden.
    Dafür sind :bdg-primary-line:`zwei Arbeitstage` vorgesehen.
    Für die :bdg-secondary-line:`Auslieferung` sind :bdg-primary-line:`vier Tage` geplant.
    Zum :bdg-secondary-line:`Anschließen der Drucker` in das Firmennetz muss die Vernetzung durch eine externe Firma erweitert werden.
    Die Netzwerkerweiterung soll am :bdg-primary-line:`19.05.2014` beginnen.
    Für die Erweiterung plant die externe Firma :bdg-primary-line:`drei Arbeitstage`.
    :bdg-primary-line:`Nach` der :bdg-secondary-line:`Auslieferung des Druckers` werden :bdg-primary-line:`zwei Tage` für den :bdg-secondary-line:`Aufbau der Drucker` eingeplant.
    :bdg-primary-line:`Gleichzeitig` soll die :bdg-secondary-line:`Software` :bdg-primary-line:`an einem Tag` :bdg-secondary-line:`installiert` werden.
    :bdg-primary-line:`Unmittelbar nach` dem :bdg-secondary-line:`Aufbau der Drucker` und der erfolgreichen :bdg-secondary-line:`Softwareinstallation` soll mit der :bdg-secondary-line:`Konfiguration` begonnen werden.
    Die Konfiguration soll :bdg-primary-line:`nach zwei Tagen` abgeschlossen sein.
    :bdg-primary-line:`Anschließend` erfolgt :bdg-primary-line:`an einem Tag` die :bdg-secondary-line:`Testphase`.
    :bdg-primary-line:`Danach` kann die :bdg-secondary-line:`Inbetriebnahme` erfolgen.

.. dropdown:: Lösung

.. uml::

    language de
    printscale daily zoom 2.5
    !include https://raw.githubusercontent.com/denn-moe/schule/main/source/_static/onedark.puml
    <style>
    ganttDiagram {
        timeline {
            FontColor #61afef

        }
        task {
            BackGroundColor #e5c07b
            FontColor #abb2bf
            FontSize 16
            FontStyle bold
            Margin 0
            Padding 14

        }
        closed {
            BackgroundColor #e06c75
            FontColor #e06c75
        }
    }
    </style>

    Project starts 2014-05-05
    saturday are closed
    sunday are closed
    2014/05/29 is closed
    [Anforderungen festlegen] lasts 2 days

    [Angebote einholen] starts 2014-05-07
    [Angebote einholen] lasts 1 week

    [Auftrag erteilen] starts 2014-05-14
    [Auftrag erteilen] lasts 2 days

    [Auslieferung] starts 2014-05-16
    [Auslieferung] lasts 4 days

    [Netzwerkerweiterung] starts 2014-05-19
    [Netzwerkerweiterung] lasts 3 days

    [Aufbau der Drucker] starts 2014-05-22
    [Aufbau der Drucker] lasts 2 days

    [Software installieren] starts 2014-05-22

    [konfiguration] starts 2014-05-26
    [konfiguration] lasts 3 days

    [test] starts 2014-05-30




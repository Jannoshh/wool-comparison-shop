
Getestet mit Python 3.10.
Installation: 
pip install bs4 requests pandas cchardet lxml pytest

Challenge mit 
python solve_challenge.py lösen

Neue unterstützte Webseiten können im Ordner „websites“ als neue Dateien angelegt werden.
Implementation ist rein funktional anstatt mit Klassen oder Interfaces zu arbeiten,
da es hier keinen Grund gibt Webseiten als Objekte zu instanziieren, sowie unterschiedlich
Webseiten meist verschiedene Informationen anbieten und einen einzigartigen Aufbau haben.

Die Hauptfunktionalität des Vergleichsportals kann in wool_comparison_shop.py einfach erweitert werden
und ist flexibel gegenüber neuen Webseiten, Attributen, etc..

Die Daten sind zunächst als CSV Datei gespeichert, in Zukunft könnte JSON eine Überlegung wert sein,
da es sehr lesbar und flexibel ist.

Die offensichtlichsten Probleme der Software:
- Das Programm ist langsam, und ein Profiling zeigt, dass ca. 95% der Zeit für die Anfragen mit
  dem requests Modul (requests.get(…)) verwendet werden. Ursache dafür muss noch herausgefunden werden.
  Asynchrone Anfragen würden es auf jeden Fall deutlich beschleunigen.
- Dokumentation ist spärlich und entspricht nicht den üblichen Formatangaben.
- Unterstützt keine Vorbestellungen bei den Lieferzeiten (ich habe keine Wolle gefunden, die vorbestellt werden kann).

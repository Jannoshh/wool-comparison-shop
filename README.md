
Getestet mit Python 3.10.

Installation: 
"pip install bs4 requests pandas cchardet lxml pytest"

Challenge mit 
"python solve_challenge.py" lösen

Neue unterstützte Webseiten können im Ordner „websites“ als neue Dateien angelegt werden.

Die Hauptfunktionalität des Vergleichsportals kann in wool_comparison_shop.py einfach erweitert werden
und ist flexibel gegenüber neuen Webseiten, Attributen, etc..

Die offensichtlichsten Probleme der Software:
- Das Programm ist langsam, und ein Profiling zeigt, dass ca. 95% der Zeit für die Anfragen mit
  dem requests Modul (requests.get(…)) verwendet werden. Ursache dafür muss noch herausgefunden werden.
  Asynchrone Anfragen würden es auf jeden Fall deutlich beschleunigen.
- Unterstützt keine Vorbestellungen (ich habe keine Wolle gefunden, die vorbestellt werden kann).

Ich habe 3.5-4 Stunden gebraucht, da ich noch eine Weile versucht habe die Performance zu verbessern.

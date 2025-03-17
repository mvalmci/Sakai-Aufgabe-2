# Sakai-Aufgabe-2
## UseCase Template für Anwendungsfall Leistungsdiagnostik

### Name und Identifikationsnummer
- Use Case 1.05 (Laktatmessung eingeben)
  
### Beschreibung
- Während der Patient den Leistungstest durchführt, entnimmt der Versuchsleiter, zu versch. Zeitpunkten, Blutproben aus dem Ohr des Patienten und bestimmt den Laktatgehalt dieser Blutproben.

### Beteiligte Akteure
- Patient
- Versuchsleiter

### Verwendete Anwendungsfälle
- UC 1.03 und UC 1.04 da HR und Leistungsabweichung eng mit dem Laktatwert im Blut zusammenhängen
  
### Auslöser
- Um eine möglichst genaue Aussage zur optimalen Trainingsherzfrequenz geben zu können, muss mindestens ein weiterer Parameter erfasst werden. Dazu bietet sich der Laktatwert, der auch in Kreisen der Spitzensportler als der genauste Anhaltspunkt dient, an. Laktat ist ein Stoffwechselendprodukt, das bei muskulärer Arbeit entsteht. Je intensiver der Organismus belastet wird, desto mehr Laktat fällt im Blut an. Wenn bestimmte Laktatschwellenwerte in der Muskulatur und damit auch im Blut überschritten werden, ist der Organismus nicht mehr in der Lage, das entstehende Laktat abzubauen. In Folge dessen kommt es zu einer Übersäuerung der Muskulatur, welche vom Körper für eine kurze Zeitspanne kompensiert und toleriert wird. Letztendlich führt dies jedoch zu einem Abfall der Leistungsfähigkeit und damit verbunden zu einem Abbruch der Belastung.

### Vorbedingungen
- Der Patient ist im System angelegt.
- Ein Leistungstest für den Pateienten wurde gestartet und der Patient befindet sich im Test
  
### Invarianten
-

### Nachbedingungen/Ergebnis
- Die eingegebenen Laktatmesswerte sind im System gespeichert und können zur Auswertung genutzt werden.

### Standartablauf
-

### Alternative Ablaufschritte
-

### Hinweise
-

### Änderungsgeschichte






## Normaler Ablauf
1. Der Benutzer wählt im System den Patienten aus, für den die Laktatmessung eingetragen werden soll.
2. Der Benutzer navigiert zur Eingabemaske für Laktatmessungen.
3. Der Benutzer gibt die gemessenen Laktatwerte sowie das Datum und die Uhrzeit der Messung ein.
4. Der Benutzer speichert die Eingabe.
5. Das System bestätigt die erfolgreiche Speicherung der Laktatmessung.

## Alternativer Ablauf
### A1: Fehlerhafte Eingabe der Laktatwerte
1. Der Benutzer gibt fehlerhafte oder unvollständige Laktatwerte ein.
2. Das System zeigt eine Fehlermeldung an und fordert den Benutzer zur Korrektur der Eingabe auf.
3. Der Benutzer korrigiert die Eingabe und speichert erneut.

## Erweiterungen
### E1: Eingabe zusätzlicher Informationen
1. Der Benutzer gibt zusätzliche Informationen zur Laktatmessung ein, z.B. Messmethode oder besondere Beobachtungen.
2. Diese Informationen werden zusammen mit den Laktatwerten gespeichert und sind für die spätere Auswertung verfügbar.

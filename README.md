# Sakai-Aufgabe-2
## UseCase Template für Anwendungsfall Leistungsdiagnostik

### Name und Identifikationsnummer
- Use Case 1.05 (Laktatmessung eingeben)
  
### Beschreibung
- Während der Patient den Leistungstest durchführt, entnimmt der Versuchsleiter, zu versch. Zeitpunkten, Blutproben aus dem Ohr des Patienten und bestimmt den Laktatgehalt dieser Blutproben und trägt Sie ins System ein

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
- Aufzeichnung der bis zum Abbruch erhobenen Daten

### Nachbedingungen/Ergebnis
- Die eingegebenen Laktatmesswerte sind im System gespeichert und können zur Auswertung genutzt werden

### Standartablauf
1. Der Versuchsleiter wählt im System den Leistungstest aus, für den die Laktatmessung eingetragen werden soll
2. Der Versuchsleiter navigiert zur Benutzeroberfläche für Laktatmessungen
3. Der Versuchsleiter gibt die gemessenen Laktatwerte und Zeitpunkt der Messung ein
4. Der Versuchsleiter speichert die Eingabe
5. Das System bestätigt die Speicherung der Laktatmesswerte

### Alternative Ablaufschritte
- Falsche Eingabe von Messwerten
  1. Versuchsleiter gibt falschen Wert (z.B. String anstatt von Float)
  2. System gibt eine Fehlermeldung zurück
  3. System fordert den Versuchsleiter auf einen korrekten Wert einzugeben
  4. Der Versuchsleiter gibt erneut einen richtigen Wert ein
  5. Er speichert die Eingabe
  6. Das System bestätigt die Speicherung der Laktatmesswerte

### Hinweise
- KEINE

### Änderungsgeschichte
- Version 1
- Name des Autors: Marius Valenta
- Datum: 14.03.2025

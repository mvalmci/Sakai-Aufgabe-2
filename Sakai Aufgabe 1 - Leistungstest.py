#python code für Sakai Aufgabe 1

def versuchsleiter_erkennen(name_versuchsleiter):
    if name_versuchsleiter == 'Marius Valenta':
        print('\n')
        print('Genehmigt! Sie können den Versuch nun anlegen.')
    else:
        print('Bitte geben Sie den richtigen Namen des Versuchsleiters ein')

name_versuchsleiter = input('Wer sind Sie? ')
versuchsleiter_erkennen(name_versuchsleiter)

leistungstests = []

def leistungstest_anlegen(first_experiment_id):
    
    try:
        first_experiment_id = int(first_experiment_id)
        for i in range(10):
            leistungstest = {
                'Id_Nummer': first_experiment_id + i,
                'Versuchsleiter': 'Marius Valenta',
                'Datum': '12.03.2025'
            }
            leistungstests.append(leistungstest)
    except ValueError:
        print("Error: The first_experiment_id should be an integer.")
    return leistungstests

print('\n')
first_experiment_id = input('Bitte geben sie die ID ein, mit welcher die Testreihe starten soll: ')
print('\n')

print('Die Testreihe wurde erfolgreich angelegt!')
print('\n')
leistungstest_anlegen(first_experiment_id)

print('Hier ist eine Liste mit Leistungstests, welche eine mit einer geraden ID erstellt wurden')
print('\n')
for leistungstest in leistungstests:
  if leistungstest['Id_Nummer'] % 2 == 0:
    print(leistungstest)
    
print('\n')
print('Hier ist eine Liste der ersten fünf Leistungstests')
print('\n')
print(leistungstests[0:5])

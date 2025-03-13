#python code für Sakai Aufgabe 1

def versuchsleiter_erkennen(name_versuchsleiter):
    if name_versuchsleiter == 'Marius Valenta':
        print('\n')
        print('Genehmigt! Sie können den Versuch nun anlegen.')
    else:
        print('Bitte geben Sie den richtigen Namen des Versuchsleiters ein')

name_versuchsleiter = input('Wer sind Sie? ')
versuchsleiter_erkennen(name_versuchsleiter)

def create_experiments(first_experiment_id):
    experiments = []
    try:
        first_experiment_id = int(first_experiment_id)
        for i in range(10):
            experiment = {
                'Id_Nummer': first_experiment_id + i,
                'Versuchsleiter': 'Marius Valenta',
                'Datum': '12.03.2025'
            }
            experiments.append(experiment)
    except ValueError:
        print("Error: The first_experiment_id should be an integer.")
    return experiments

print('\n')
first_experiment_id = input('Bitte geben sie die ID ein, mit welcher die Testreihe starten soll: ')
print('\n')

print('Die Testreihe wurde erfolgreich angelegt! \nHier iste eine Liste der Testreihe:')
print('\n')
create_experiments(first_experiment_id)

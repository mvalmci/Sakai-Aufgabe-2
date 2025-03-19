from my_functions import build_experiment
from my_functions import build_person
from my_functions import estimate_max_hr
from datetime import datetime

if __name__ == "__main__":
    experiment = build_experiment(
        experiment_name=input("Bitte geben Sie dem Experiment einen Namen: "),
        date=datetime.today().strftime("%Y-%m-%d"),
        supervisor=input("Bitte geben Sie den Namen des Versuchsleiters ein: "),
        subject="Leistungstest"
    )
    age1 = int(input("Bitte geben Sie das Alter des Patienten ein: "))
    patient = build_person(
        first_name=input("Wie lautet der Vorname des Patienten?: "),
        last_name=input("Wie lautet der Nachname des Patienten?: "),
        sex=input("Geschlecht? (male/female): "),
        age=age1
    )
    
    herzfrequenz = estimate_max_hr(
        sex = input("Bitte geben Sie das Geschlecht des Patienten ein um eine geschätzte maximale HR berechnen zu können: "),
        age_years= age1
    )
   
#nun wird eine neue Funktion erstellt, welche die beiden dictionarys zu einem zusammenfügt

    def dict_komplett(patient, experiment) -> dict:

       dict_ganz = { "Patient:innen_Daten" : patient,
                "Experiment_Daten" : experiment,
                }
       return dict_ganz
    
    print(dict_komplett(patient,experiment))
from my_functions import build_experiment
from my_functions import build_person
from my_functions import estimate_max_hr
from datetime import datetime

if __name__ == "__main__":
    experiment = build_experiment(
        experiment_name=input("Bitte geben Sie dem Experiment einen Namen: "),
        date=datetime.today().strftime("%Y-%m-%d"),
        supervisor=input("Bitte geben Sie den Namen des Versuchsleiters ein: "),
        subject="max_hr_test"
    )
    age_general = int(input("Bitte geben Sie das Alter des Patienten ein: "))
    sex_general = input("Bitte geben Sie das Geschlecht des Patienten ein! (male/female): ")
    patient = build_person(
        first_name=input("Wie lautet der Vorname des Patienten?: "),
        last_name=input("Wie lautet der Nachname des Patienten?: "),
        sex=sex_general,
        age=age_general
    )
    
    herzfrequenz = estimate_max_hr(
        sex = sex_general,
        age_years= age_general
    )
   
#nun wird eine neue Funktion erstellt, welche die beiden dictionarys zu einem zusammenfügt

    def dict_komplett(patient, experiment) -> dict:

       dict_ganz = { "Patient:innen_Daten" : patient,
                "Experiment_Daten" : experiment,
                }
       return dict_ganz
    
    print(dict_komplett(patient,experiment))
#python code für Sakai Aufgabe 1

from typing import List, Dict, Any

def create_experiments(first_experiment_id: int) -> List[Dict[str, Any]]:
    experiments = []
    creation_date = "2025-03-13"
    experiment_leader = "mvalmci"

    for i in range(10):
        experiment_id = first_experiment_id + i
        experiment = {
            "Id_Nummer": experiment_id,
            "Erstellungsdatum": creation_date,
            "Versuchsleiter": experiment_leader,
        }
        experiments.append(experiment)
    
    return experiments

def display_first_five_experiments(experiments: List[Dict[str, Any]]) -> None:
    for experiment in experiments[:5]:
        print(experiment)

def count_even_id_experiments(experiments: List[Dict[str, Any]]) -> int:
    return sum(1 for experiment in experiments if experiment["Id_Nummer"] % 2 == 0)

def main():
    try:
        first_experiment_id = int(input("Geben Sie die erste Experiment-ID ein: "))
        experiments = create_experiments(first_experiment_id)
        
        print("\nErste fünf Experimente:")
        display_first_five_experiments(experiments)
        
        even_id_count = count_even_id_experiments(experiments)
        print(f"\nAnzahl der Experimente mit gerader ID: {even_id_count}")
    
    except ValueError:
        print("Bitte geben Sie eine gültige ganze Zahl für die erste Experiment-ID ein.")

if __name__ == "__main__":
    main()

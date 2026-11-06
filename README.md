# My To-Do List

Une application de bureau simple de gestion des tâches, développée en **Python** avec **Tkinter**.

## Fonctionnalités

- Ajouter une tâche.
- Afficher toutes les tâches.
- Marquer une tâche comme terminée ou la remettre en cours.
- Supprimer une tâche après confirmation.
- Afficher les tâches en cours en rouge et les tâches terminées en vert.
- Sauvegarder automatiquement les tâches dans un fichier JSON.
- Retrouver les tâches après la fermeture et le redémarrage de l'application.

## Technologies utilisées

- Python 3
- Tkinter (interface graphique)
- JSON (sauvegarde des données)

## Prérequis

- Python 3 installé.
- Tkinter disponible avec l'installation de Python.

Aucune bibliothèque externe n'est nécessaire.

## Lancer le projet

1. Téléchargez ou clonez ce dépôt.
2. Ouvrez le dossier du projet.
3. Lancez le fichier `main.py` :

```bash
python main.py
```

Sur certaines installations Windows, cette commande peut être :

```bash
py main.py
```

## Organisation des fichiers

```text
my-todo-list-python/
├── main.py       # Code principal de l'application
├── taches.json   # Sauvegarde des tâches
├── README.md     # Présentation et instructions
└── .gitignore    # Fichiers à ne pas envoyer sur GitHub
```

## Format des données

Les tâches sont enregistrées dans `taches.json` au format JSON. Chaque tâche contient :
- `description` : le texte de la tâche.
- `terminee` : `true` si la tâche est terminée, sinon `false`.

Exemple :

```json
[
    {
        "description": "Apprendre Python",
        "terminee": false
    },
    {
        "description": "Faire les exercices",
        "terminee": true
    }
]
```

## Améliorations possibles

- Ajouter une fonction de recherche.
- Ajouter des catégories de tâches.
- Ajouter des filtres (toutes, en cours, terminées).
- Améliorer l'interface graphique.

## Auteur

Projet personnel réalisé dans le cadre de l'apprentissage de Python et du développement d'applications.

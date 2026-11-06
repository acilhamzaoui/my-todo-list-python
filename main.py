import tkinter as tk
from tkinter import messagebox
import json
from pathlib import Path

# Fichier de sauvegarde placé dans le même dossier que main.py
DOSSIER_PROJET = Path(__file__).resolve().parent
FICHIER_TACHES = DOSSIER_PROJET / "taches.json"

# Couleurs de l'application
BG = "#F4F5FB"
WHITE = "#FFFFFF"
PURPLE = "#7657E8"
DARK = "#25243A"
GREY = "#85859A"
GREEN = "#229B62"
RED = "#E05260"

taches = []


def charger_taches():
    """Charge les tâches depuis le fichier JSON."""
    global taches

    if not FICHIER_TACHES.exists():
        taches = []
        return

    try:
        with FICHIER_TACHES.open("r", encoding="utf-8") as fichier:
            donnees = json.load(fichier)

        # Vérifie que le fichier contient bien une liste de tâches.
        if isinstance(donnees, list):
            taches = [
                {
                    "description": str(item.get("description", "")),
                    "terminee": bool(item.get("terminee", False))
                }
                for item in donnees
                if isinstance(item, dict) and item.get("description")
            ]
        else:
            taches = []

    except (json.JSONDecodeError, OSError):
        taches = []
        messagebox.showwarning(
            "Sauvegarde",
            "Le fichier taches.json est illisible. Une liste vide sera utilisée."
        )


def sauvegarder_taches():
    """Enregistre les tâches dans le fichier JSON."""
    try:
        with FICHIER_TACHES.open("w", encoding="utf-8") as fichier:
            json.dump(taches, fichier, ensure_ascii=False, indent=4)
    except OSError as erreur:
        messagebox.showerror(
            "Erreur de sauvegarde",
            f"Impossible d'enregistrer les tâches :\n{erreur}"
        )


def afficher_taches():
    """Actualise la liste et les couleurs des tâches."""
    liste.delete(0, tk.END)

    for index, tache in enumerate(taches):
        if tache["terminee"]:
            texte = f"✓  {tache['description']}  — Terminée"
            couleur = GREEN
        else:
            texte = f"○  {tache['description']}  — En cours"
            couleur = RED

        liste.insert(tk.END, texte)
        liste.itemconfig(index, fg=couleur)

    total = len(taches)
    terminees = sum(1 for tache in taches if tache["terminee"])
    restantes = total - terminees

    compteur.config(
        text=f"{total} tâches  |  {restantes} en cours  |  {terminees} terminées"
    )


def ajouter_tache(event=None):
    """Ajoute une nouvelle tâche non terminée."""
    description = entree.get().strip()

    if not description:
        messagebox.showwarning("Attention", "Veuillez écrire une tâche.")
        entree.focus_set()
        return

    taches.append({
        "description": description,
        "terminee": False
    })

    entree.delete(0, tk.END)
    sauvegarder_taches()
    afficher_taches()
    entree.focus_set()


def changer_statut():
    """Marque une tâche comme terminée ou la remet en cours."""
    selection = liste.curselection()

    if not selection:
        messagebox.showwarning(
            "Attention",
            "Veuillez sélectionner une tâche."
        )
        return

    index = selection[0]
    taches[index]["terminee"] = not taches[index]["terminee"]

    sauvegarder_taches()
    afficher_taches()
    liste.selection_set(index)


def supprimer_tache():
    """Supprime la tâche sélectionnée après confirmation."""
    selection = liste.curselection()

    if not selection:
        messagebox.showwarning(
            "Attention",
            "Veuillez sélectionner une tâche."
        )
        return

    index = selection[0]
    confirmation = messagebox.askyesno(
        "Confirmation",
        "Voulez-vous vraiment supprimer cette tâche ?"
    )

    if confirmation:
        taches.pop(index)
        sauvegarder_taches()
        afficher_taches()


def creer_bouton(parent, texte, commande, couleur, couleur_active):
    """Crée un bouton avec le style commun de l'application."""
    return tk.Button(
        parent,
        text=texte,
        command=commande,
        bg=couleur,
        fg=WHITE,
        activebackground=couleur_active,
        activeforeground=WHITE,
        font=("Arial", 10, "bold"),
        relief="flat",
        cursor="hand2",
        padx=12,
        pady=11
    )


# ------------------------------
# Fenêtre principale
# ------------------------------
fenetre = tk.Tk()
fenetre.title("My To-Do List")
fenetre.geometry("700x620")
fenetre.minsize(560, 500)
fenetre.configure(bg=BG)

header = tk.Frame(fenetre, bg=BG)
header.pack(fill="x", padx=35, pady=(30, 15))

tk.Label(
    header,
    text="My To-Do List",
    font=("Arial", 27, "bold"),
    bg=BG,
    fg=DARK
).pack(anchor="w")

tk.Label(
    header,
    text="Organisez vos tâches et atteignez vos objectifs.",
    font=("Arial", 11),
    bg=BG,
    fg=GREY
).pack(anchor="w", pady=5)

carte = tk.Frame(fenetre, bg=WHITE, padx=25, pady=25)
carte.pack(fill="both", expand=True, padx=35, pady=15)

tk.Label(
    carte,
    text="Ajouter une nouvelle tâche",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=DARK
).pack(anchor="w", pady=(0, 10))

zone_saisie = tk.Frame(carte, bg=WHITE)
zone_saisie.pack(fill="x", pady=(0, 20))

entree = tk.Entry(
    zone_saisie,
    font=("Arial", 12),
    bg=BG,
    fg=DARK,
    relief="flat",
    bd=0
)
entree.pack(side="left", fill="x", expand=True, ipady=12, padx=(0, 10))
entree.bind("<Return>", ajouter_tache)

creer_bouton(
    zone_saisie, "+ Ajouter", ajouter_tache, PURPLE, "#6042CE"
).pack(side="right")

compteur = tk.Label(
    carte,
    text="0 tâches | 0 en cours | 0 terminées",
    font=("Arial", 10),
    bg=WHITE,
    fg=GREY
)
compteur.pack(anchor="w", pady=(0, 12))

zone_liste = tk.Frame(carte, bg=WHITE)
zone_liste.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(zone_liste)
scrollbar.pack(side="right", fill="y")

liste = tk.Listbox(
    zone_liste,
    font=("Arial", 12),
    bg="#FAFAFE",
    fg=DARK,
    selectbackground="#DCD4FF",
    selectforeground=DARK,
    relief="flat",
    bd=0,
    activestyle="none",
    height=12,
    yscrollcommand=scrollbar.set
)
liste.pack(side="left", fill="both", expand=True)
scrollbar.config(command=liste.yview)

zone_boutons = tk.Frame(carte, bg=WHITE)
zone_boutons.pack(fill="x", pady=(20, 0))

creer_bouton(
    zone_boutons,
    "✓ Terminer / Reprendre",
    changer_statut,
    GREEN,
    "#167A4A"
).pack(side="left", fill="x", expand=True, padx=(0, 8))

creer_bouton(
    zone_boutons,
    "✕ Supprimer",
    supprimer_tache,
    RED,
    "#C83D4D"
).pack(side="left", fill="x", expand=True)

# Chargement initial et lancement de l'application
charger_taches()
afficher_taches()
entree.focus_set()
fenetre.mainloop()

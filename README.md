# Pong Power-Up – Projet NSI Terminale

Ce projet est un jeu de Pong avec des *power-ups*, développé en Python à l'aide de la bibliothèque **Pyxel**, dans le cadre d'un projet personnel de NSI en Terminale. Le jeu oppose deux joueurs qui contrôlent des raquettes, avec une balle qui rebondit, marque des points et interagit avec des objets bonus qui modifient sa vitesse.
Consulter directement le jeu via ce lien : https://www.pyxelstudio.net/studio/kvhpl4

## Fonctionnalités

- Deux joueurs (clavier : `Z/S` pour le joueur 1, `↑/↓` pour le joueur 2)
- Balle avec gestion de rebonds, scores, et collisions
- Power-ups :
  - Un qui accélère la balle
  - Un qui ralentit la balle
- Affichage graphique simple avec **Pyxel**
- Ligne médiane, scores visibles à l'écran
- Dessins personnalisés avec `pyxel.load()` et `pyxel.blt()`

## Captures d'écran

![image](https://github.com/user-attachments/assets/230fed82-e1c8-4cbb-88b7-6818ed2a23fd)

## Installation

1. Installe Python (si ce n'est pas déjà fait).
2. Installe la bibliothèque Pyxel :

```bash
pip install pyxel
```

3. Tu peux aussi consulter [le site officiel de Pyxel](https://github.com/kitao/pyxel) pour plus d'infos et d'exemples.

## Lancer le jeu

Sauvegarde le code dans un fichier, par exemple `pong.py`, puis exécute :

```bash
python pong.py
```

Assure-toi d'avoir un fichier de ressources `res.pyxres` dans le même dossier si tu veux utiliser les dessins personnalisés du power-up.
Ou tu peux aller sur le site officiel de pyxel et faire un dessin personalisé comme celui ci dessous 

![image](https://github.com/user-attachments/assets/4b640696-699c-4f7c-9a97-4eb4006db2f4)

## Notes

- Le jeu commence automatiquement.
- Si la balle sort à gauche ou à droite, le score est mis à jour, et la balle repart du centre.
- Les power-ups apparaissent aléatoirement et affectent la vitesse de la balle en cas de collision.

## Auteur

Projet développé par Emmanuel TIAMZON ancien élève de Terminale générale spécialité NSI, réalisé en autonomie dans le cadre d'un projet de milieu d'année.

## Remarque

Ce projet n’est pas destiné à un usage commercial. Il a été créé dans un but d’apprentissage uniquement.

# Secure PDF

Secure PDF est un outil simple pour protéger vos fichiers PDF avec un mot de passe. Ce script utilise la bibliothèque `pypdf` pour lire et écrire des fichiers PDF et ajouter une protection par mot de passe.

## Fonctionnalités

- Protection des fichiers PDF avec un mot de passe
- Traitement de tous les fichiers PDF dans un répertoire source

## Prérequis

- Python 3.x
- La bibliothèque `pypdf`

## Installation

1. Clonez le dépôt ou téléchargez les fichiers du projet.
2. Assurez-vous d'avoir `pip` installé pour gérer les paquets Python.
3. Installez les dépendances nécessaires en utilisant le fichier `requirements.txt` :

```bash
    pip install -r requirements.txt
```

## Utilisation

1. Placez les fichiers PDF que vous souhaitez protéger dans le répertoire `src`.
2. Modifiez le mot de passe dans le script `main.py` si nécessaire :

    ```python
        password = "my_password"  # Définissez votre mot de passe ici
    ```

3. Exécutez le script :

    ```bash
        python main.py
    ```

4. Les fichiers PDF protégés seront générés dans le `répertoire output`.

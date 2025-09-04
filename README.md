# StarterKit Flask – Structure et Installation

## Architecture du projet

```
flask/
│
├── app.py                  # Point d'entrée principal de l'application
├── config/                 # Fichiers de configuration (Flask, base de données)
│   ├── database.py
│   └── flask_config.py
├── controllers/            # Logique métier (fonctions)
│   ├── main.py
│   ├── auth.py
│   └── account.py
├── routes/                 # Définition des routes et blueprints
│   ├── main_routes.py
│   ├── auth_routes.py
│   └── account_routes.py
├── models/                 # Modèles SQLAlchemy
│   ├── user.py
│   └── account.py
├── templates/              # Fichiers HTML (Jinja2)
│   └── ...
├── instance/               # Dossier pour la base SQLite
│   └── data.db
├── .env                    # Variables d'environnement
├── README.md               # Documentation du projet
```

- **app.py** : Initialise Flask, charge la config, enregistre les blueprints.
- **config/** : Centralise les paramètres (clé secrète, URI base, debug...)
- **controllers/** : Contient la logique métier, séparée des routes.
- **routes/** : Définit les routes et blueprints, appelle les fonctions des controllers.
- **models/** : Décrit les tables et relations de la base de données.
- **templates/** : Les vues HTML.
- **instance/** : Contient la base SQLite.
- **.env** : Permet de personnaliser la config sans modifier le code.

## Installation et lancement

1. **Cloner le projet**
   ```bash
   git clone <url-du-repo>
   cd flask
   ```
2. **Créer et activer un environnement virtuel**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # ou
   source venv/bin/activate  # Linux/Mac
   ```
3. **Installer les dépendances**
   ```bash
   pip install flask flask_sqlalchemy python-dotenv
   ```
4. **Vérifier/éditer le fichier `.env`**
   - Adapter la clé secrète et l’URI de la base si besoin.
5. **Lancer l’application**
   ```bash
   py app.py
   ```
6. **Accéder à l’application**
   - Ouvrir le navigateur sur [http://localhost:5002](http://localhost:5002)

## Conseils
- Pour changer la config, modifiez `.env` ou les fichiers du dossier `config`.
- Pour ajouter des routes, créez un nouveau fichier dans `routes/` et un controller associé.
- Pour ajouter des modèles, créez un fichier dans `models/`.

---
Ce projet est conçu pour être modulaire, évolutif et facile à maintenir.

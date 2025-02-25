# kube
Projet kube cesi
## Dépendances:
Installer "docker" et "docker compose"
## Structure:
- flask_app:
    - app.py: server fastapi
    - Dockerfile: lance le projet avec "uvicorn"
    - requirements.txt: dépendances python
    - utils.py: contient la focntion qui initialise la base de données et autres
    - wsgi.py: appelle app.py via gunicorn
- nginx: reverse proxy
-mongodb
## Pour lancer
- `cd kube_cesi`
- build: `docker compose build --no-cache`
- run avec logs: `docker compose up`
- run sans les logs (detached mode): `docker compose up -d`
- pour voir les services qui se lancent: `docker ps`
- documentation et test de l'api: http://localhost:docs
## Pour arrêter:
- `cd kube_cesi`
- `docker compose down --remove-orphans`

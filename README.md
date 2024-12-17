# kube
Projet kube cesi
## Dépendances:
Installer "docker" et "docker compose"
## Structure:
- flask_app:
    - static: images et css (à améliorer)
    - templates: html (à améliorer)
    - app.py: server flask (à améliorer)
    - Dockerfile: lance le projet avec "gunicorn"
    - requirements.txt: dépendances python
    - utils.py: contient la focntion qui initialise la base de données et autres
    - wsgi.py: appelle app.py via gunicorn
- nginx: reverse proxy
## Pour lancer
- `cd kube_cesi`
- build: `docker compose build --no-cache`
- run avec logs: `docker compose up`
- run sans les logs (detached mode): `docker compose up -d`
- pour voir les services qui se lancent: `docker ps`
- `http://localhost`
## Pour arrêter:
- `cd kube_cesi`
- `docker compose down --remove-orphans`

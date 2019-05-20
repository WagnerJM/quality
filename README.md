# Quality Watcher

## todo



## Notizen

https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/

https://stackoverflow.com/questions/54499070/leaflet-and-vuejs-how-to-add-a-new-marker-onclick-in-the-map



## Installation

1. Linux Server (vorzugsweise Ubuntu)
    1. Docker installieren
    2. Docker-Compose installieren
2. Backend-Repository klonen
`git clone https://github.com/WagnerJM/quality.git`
3. In das Verzeichnis wechseln
`cd quality`
4. Client-Repo klonen
`git clone https://github.com/WagnerJM/quality_client.git client`
5. .env Datei erstellen
    `python start.py`
    Dabei werden verschiedene Daten abgefragt die für die App notwendig sind und eine .env Datei erstellt
6. Container bauen und starten
`docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d`

7. Öffne ein Terminal
`docker ps`
- Kopiere die _server id
8. Öffne eine Bash Konsole zum Container
`docker exec -it [CONTAINER_ID] bash`
Dabei loggt man sich in den Container rein
9. Erstelle die Datenbank schemas
<code>

flask db init

flask db migrate

flask db upgrade

</code>

Nachdem das fertig ist, kann mit der App gearbeitet werden.



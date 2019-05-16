# Quality Watcher

## todo



## Notizen

https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/


## Installation

.env Datei erstellen

```
APP_SETTINGS=
FLASK_APP=
FLASK_ENV=
POSTGRES_USER=
POSTGRES_PW=
REDIS_PW=
DATABASE=
SECRET_KEY=
JWT_SECRET=

```

<code> mkdir data </code>

- Secret Key herstellen zb. über die python shell

<code>
import secrets

secrets.token_hex(32)
</code>

Anschließend Key rauskopieren und in .env Datei einfügen


## Production Deployment

- Anforderungen:
    - Linux Server (vorzugsweise ubuntu)
    - docker 
    - docker-compose

- Ausführen des start.sh

- clone client repo
<code>
git clone https://github.com/WagnerJM/quality_client.git

</code>
- Damit docker-compose alle Container erstellen kann, muss das Client-Verzeichnis "client" heißen

`mv quality_client client`

- Damit docker die App erreichbar macht im Netzwerk
    - check if docker runs 

    <code>
    sudo sytemctl status docker
    </code>

    - run docker compose as daemon

    <code>
    docker-compose up -d  
    </code>

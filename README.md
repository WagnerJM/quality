# Quality Watcher

## todo



## Notizen

https://www.revsys.com/tidbits/celery-and-django-and-docker-oh-my/

https://stackoverflow.com/questions/54499070/leaflet-and-vuejs-how-to-add-a-new-marker-onclick-in-the-map



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

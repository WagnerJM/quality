from flask.cli import FlaskGroup

from app import create_app
from app.database import db



app = create_app()
cli = FlaskGroup(create_app=create_app)
prompt = "> "

@cli.command('create_admin')
def create_admin_user():
    pass

if __name__ == '__main__':
    cli()

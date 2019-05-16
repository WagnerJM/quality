"""empty message

Revision ID: 032d14946f8c
Revises: 
Create Date: 2019-05-16 11:50:29.618489

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '032d14946f8c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('qrkarten',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('qrkID', sa.Integer(), nullable=False),
    sa.Column('titel', sa.String(), nullable=False),
    sa.Column('x_achse_titel', sa.String(), nullable=False),
    sa.Column('y_achse_titel', sa.String(), nullable=False),
    sa.Column('obere_warngrenze', sa.Float(), nullable=True),
    sa.Column('untere_warngrenze', sa.Float(), nullable=True),
    sa.Column('obere_eingriffsgrenze', sa.Float(), nullable=True),
    sa.Column('untere_eingriffsgrenze', sa.Float(), nullable=True),
    sa.Column('stdabw', sa.Float(), nullable=True),
    sa.Column('mittelwert', sa.Float(), nullable=True),
    sa.Column('dateiname', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('qrkID'),
    sa.UniqueConstraint('id')
    )
    op.create_table('messwerte',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('messwertID', sa.Integer(), nullable=False),
    sa.Column('datum', sa.DateTime(), nullable=False),
    sa.Column('wert', sa.Float(), nullable=False),
    sa.Column('valid', sa.Boolean(), nullable=True),
    sa.Column('qrk_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['qrk_id'], ['qrkarten.qrkID'], ),
    sa.PrimaryKeyConstraint('messwertID'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messwerte')
    op.drop_table('qrkarten')
    # ### end Alembic commands ###

"""empty message

Revision ID: 476f33a6f51b
Revises: 819563ebfc17
Create Date: 2021-07-14 16:28:44.989518

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '476f33a6f51b'
down_revision = '819563ebfc17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date_updated', sa.DateTime(), nullable=True))
    op.drop_column('post', 'date_update')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date_update', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('post', 'date_updated')
    # ### end Alembic commands ###

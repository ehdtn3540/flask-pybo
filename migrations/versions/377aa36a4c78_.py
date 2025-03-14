"""empty message

Revision ID: 377aa36a4c78
Revises: b65ee761c3ba
Create Date: 2025-03-14 11:05:39.581364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '377aa36a4c78'
down_revision = 'b65ee761c3ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###

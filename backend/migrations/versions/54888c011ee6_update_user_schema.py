"""Update user schema

Revision ID: 54888c011ee6
Revises: 0a24f0ceedb3
Create Date: 2025-03-11 10:23:16.336675

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '54888c011ee6'
down_revision = '0a24f0ceedb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('users_ibfk_1', type_='foreignkey')
        batch_op.drop_column('departmentcode')
        batch_op.drop_column('batch')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('batch', mysql.VARCHAR(length=9), nullable=True))
        batch_op.add_column(sa.Column('departmentcode', mysql.VARCHAR(length=10), nullable=False))
        batch_op.create_foreign_key('users_ibfk_1', 'departments', ['departmentcode'], ['departmentcode'])

    # ### end Alembic commands ###

"""empty message

Revision ID: 1a5f453e6e23
Revises: e9c18760196b
Create Date: 2021-06-14 18:27:15.965411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a5f453e6e23'
down_revision = 'e9c18760196b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('goal', 'goal_id')
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.add_column('task', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['id'])
    op.drop_column('task', 'task_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('task_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'id')
    op.drop_column('task', 'goal_id')
    op.add_column('goal', sa.Column('goal_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('goal', 'id')
    # ### end Alembic commands ###

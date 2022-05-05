"""add fee_id to student

Revision ID: e1ca8747a54d
Revises: 
Create Date: 2022-05-05 09:51:51.083894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1ca8747a54d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('student', sa.Column('fee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'student', 'fee', ['fee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'student', type_='foreignkey')
    op.drop_column('student', 'fee_id')
    # ### end Alembic commands ###

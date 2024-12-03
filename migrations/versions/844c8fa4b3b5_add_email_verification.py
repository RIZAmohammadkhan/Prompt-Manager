"""Add email verification

Revision ID: 844c8fa4b3b5
Revises: 
Create Date: 2024-12-03 15:27:57.419068

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '844c8fa4b3b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email_verified', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email_verified')

    # ### end Alembic commands ###
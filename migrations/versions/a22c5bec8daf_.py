"""empty message

Revision ID: a22c5bec8daf
Revises: 6f7b3083221e
Create Date: 2024-02-20 10:34:14.722076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a22c5bec8daf'
down_revision = '6f7b3083221e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('image_file')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.VARCHAR(length=20), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
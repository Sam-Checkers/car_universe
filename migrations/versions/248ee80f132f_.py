"""empty message

Revision ID: 248ee80f132f
Revises: 67b699f8accd
Create Date: 2024-02-25 17:38:26.746810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '248ee80f132f'
down_revision = '67b699f8accd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_file', sa.String(length=20), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('image_file')

    # ### end Alembic commands ###

"""rmse a float

Revision ID: d5dcfa15191a
Revises: 9b2916d72ffe
Create Date: 2023-08-31 16:54:56.290582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5dcfa15191a'
down_revision = '9b2916d72ffe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('regressionmodel', sa.Column('rmse', sa.Float(), nullable=True))
    op.drop_column('regressionmodel', 'accuracy')
    op.alter_column('segmentationmodel', 'iou',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('segmentationmodel', 'iou',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               existing_nullable=True)
    op.add_column('regressionmodel', sa.Column('accuracy', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('regressionmodel', 'rmse')
    # ### end Alembic commands ###

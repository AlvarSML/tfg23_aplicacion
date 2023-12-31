"""Eliminacion en cascada

Revision ID: 0264a2946005
Revises: f9342dd338df
Create Date: 2023-09-15 16:16:24.930466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0264a2946005'
down_revision = 'f9342dd338df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('item', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('modelselection_reg_id_fkey', 'modelselection', type_='foreignkey')
    op.drop_constraint('modelselection_seg_id_fkey', 'modelselection', type_='foreignkey')
    op.create_foreign_key(None, 'modelselection', 'regressionmodel', ['reg_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'modelselection', 'segmentationmodel', ['seg_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'modelselection', type_='foreignkey')
    op.drop_constraint(None, 'modelselection', type_='foreignkey')
    op.create_foreign_key('modelselection_seg_id_fkey', 'modelselection', 'segmentationmodel', ['seg_id'], ['id'])
    op.create_foreign_key('modelselection_reg_id_fkey', 'modelselection', 'regressionmodel', ['reg_id'], ['id'])
    op.alter_column('item', 'owner_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###

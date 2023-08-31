"""Simplificacion

Revision ID: 9b2916d72ffe
Revises: 8ade0c9f75cc
Create Date: 2023-08-31 12:52:06.380155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b2916d72ffe'
down_revision = '8ade0c9f75cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association_seg_reg')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('association_seg_reg',
    sa.Column('modelo_seg', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('modelo_reg', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['modelo_reg'], ['segmentationmodel.id'], name='association_seg_reg_modelo_reg_fkey'),
    sa.ForeignKeyConstraint(['modelo_seg'], ['regressionmodel.id'], name='association_seg_reg_modelo_seg_fkey'),
    sa.PrimaryKeyConstraint('modelo_seg', 'modelo_reg', name='association_seg_reg_pkey')
    )
    # ### end Alembic commands ###
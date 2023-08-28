"""Modelos para regresion

Revision ID: 3d2b7c34107d
Revises: d4867f3a4c0a
Create Date: 2023-08-28 17:33:13.088595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d2b7c34107d'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('short_desc', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('root_dir', sa.String(), nullable=True),
    sa.Column('file_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_model_file_path'), 'model', ['file_path'], unique=False)
    op.create_index(op.f('ix_model_id'), 'model', ['id'], unique=False)
    op.create_index(op.f('ix_model_name'), 'model', ['name'], unique=False)
    op.create_table('regressionmodel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('accuracy', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('segmentationmodel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('accuracy', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association_seg_reg',
    sa.Column('modelo_seg', sa.Integer(), nullable=False),
    sa.Column('modelo_reg', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['modelo_reg'], ['segmentationmodel.id'], ),
    sa.ForeignKeyConstraint(['modelo_seg'], ['regressionmodel.id'], ),
    sa.PrimaryKeyConstraint('modelo_seg', 'modelo_reg')
    )
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_table('association_seg_reg')
    op.drop_table('segmentationmodel')
    op.drop_table('regressionmodel')
    op.drop_index(op.f('ix_model_name'), table_name='model')
    op.drop_index(op.f('ix_model_id'), table_name='model')
    op.drop_index(op.f('ix_model_file_path'), table_name='model')
    op.drop_table('model')
    # ### end Alembic commands ###

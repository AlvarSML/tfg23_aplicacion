"""estados

Revision ID: 8ade0c9f75cc
Revises: ff90c8aaa00a
Create Date: 2023-08-30 16:31:39.634020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ade0c9f75cc'
down_revision = 'ff90c8aaa00a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('modelselection',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('reg_model', sa.Integer(), nullable=False),
    sa.Column('seg_model', sa.Integer(), nullable=False),
    sa.Column('changed_by', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['changed_by'], ['user.id'], ),
    sa.ForeignKeyConstraint(['reg_model'], ['regressionmodel.id'], ),
    sa.ForeignKeyConstraint(['seg_model'], ['segmentationmodel.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('model', sa.Column('created_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('model', sa.Column('model_description', sa.String(), nullable=True))
    op.drop_column('model', 'description')
    op.add_column('segmentationmodel', sa.Column('iou', sa.Integer(), nullable=True))
    op.drop_column('segmentationmodel', 'accuracy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('segmentationmodel', sa.Column('accuracy', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('segmentationmodel', 'iou')
    op.add_column('model', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('model', 'model_description')
    op.drop_column('model', 'created_date')
    op.drop_table('modelselection')
    # ### end Alembic commands ###

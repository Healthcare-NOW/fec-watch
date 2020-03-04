"""Adding individual contributions.

Revision ID: 4e6299081e3f
Revises: c579f108ac7c
Create Date: 2020-03-03 19:12:46.606169

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4e6299081e3f'
down_revision = 'c579f108ac7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('individual_contributor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('city', sa.String(length=30), nullable=True),
    sa.Column('state', sa.String(length=2), nullable=True),
    sa.Column('zip', sa.String(length=9), nullable=True),
    sa.Column('employer', sa.String(length=38), nullable=True),
    sa.Column('occupation', sa.String(length=38), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('individual_contribution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('committee_id', sa.Integer(), nullable=False),
    sa.Column('contributor_id', sa.Integer(), nullable=False),
    sa.Column('amendment_indicator', postgresql.ENUM('N', 'A', 'T', name='amendment_indicator'), nullable=True),
    sa.Column('report_type', sa.String(length=3), nullable=True),
    sa.Column('primary_general_indicator', sa.String(length=5), nullable=True),
    sa.Column('fec_image_ref', sa.String(length=18), nullable=True),
    sa.Column('transaction_type', sa.String(length=3), nullable=True),
    sa.Column('entity_type', sa.String(length=3), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('amount', postgresql.MONEY(), nullable=True),
    sa.Column('committee_fec_id', sa.String(length=9), nullable=True),
    sa.Column('other_fec_id', sa.String(length=9), nullable=True),
    sa.ForeignKeyConstraint(['committee_id'], ['committee.id'], ),
    sa.ForeignKeyConstraint(['contributor_id'], ['individual_contributor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('individual_contribution')
    op.drop_table('individual_contributor')
    # ### end Alembic commands ###
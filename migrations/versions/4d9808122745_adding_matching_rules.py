"""Adding matching rules.

Revision ID: 4d9808122745
Revises: fc6af3722d01
Create Date: 2020-03-08 15:22:03.698298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d9808122745'
down_revision = 'fc6af3722d01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flagged_employer_matching_rule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employer', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('flagged_employer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['flagged_employer_id'], ['flagged_employer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('flagged_individual_contributor', 'flagged_employer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('flagged_individual_contributor', 'employer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('flagged_individual_contributor', sa.Column('employer', sa.VARCHAR(length=38), autoincrement=False, nullable=True))
    op.alter_column('flagged_individual_contributor', 'flagged_employer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_table('flagged_employer_matching_rule')
    # ### end Alembic commands ###
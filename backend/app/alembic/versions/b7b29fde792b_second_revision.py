"""second revision

Revision ID: b7b29fde792b
Revises: 
Create Date: 2022-11-30 09:09:32.675022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7b29fde792b'
down_revision = 'b7b29fde792a'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('contract', sa.Column('suspend', sa.Integer(), nullable=True))
    op.add_column('user_broker', sa.Column('api_name', sa.String(), nullable=True))
    op.add_column('user_broker', sa.Column('contract_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user_broker', 'contract', ['contract_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')

    # op.alter_column('user_broker', 'old_column', type=sa.String())
    # op.add_column('my_table', 'fk_to_other_table', sa.Integer())
    # op.create_foreign_key('fk_to_other_table', 'my_table', 'other_table', 'id')

def downgrade():
    op.drop_column('contract', 'suspend')
    op.drop_column('user_broker', 'api_name')
    op.drop_column('user_broker', 'contract_id')

    # op.drop_column('my_table', 'new_column')
    # op.alter_column('my_table', 'old_column', type=sa.Integer())
    # op.drop_column('my_table', 'fk_to_other_table')


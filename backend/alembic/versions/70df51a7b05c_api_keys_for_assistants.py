"""api keys for assistants
Revision ID: 70df51a7b05c
Revises: e0fe14982bcf
Create Date: 2024-01-11 15:13:48.020085
"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic
revision = '70df51a7b05c'
down_revision = 'e0fe14982bcf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('api_keys', sa.Column('assistant_id', sa.Integer(), nullable=True))
    op.alter_column('api_keys', 'user_id', existing_type=sa.INTEGER(), nullable=True)
    op.create_unique_constraint(
        "api_keys_assistant_id_unique", 'api_keys', ['assistant_id']
    )
    op.create_foreign_key(
        "api_keys_assistant_fkey",
        'api_keys',
        'assistants',
        ['assistant_id'],
        ['id'],
        ondelete='CASCADE',
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("api_keys_assistant_fkey", 'api_keys', type_='foreignkey')
    op.drop_constraint("api_keys_assistant_id_unique", 'api_keys', type_='unique')
    op.alter_column('api_keys', 'user_id', existing_type=sa.INTEGER(), nullable=False)
    op.drop_column('api_keys', 'assistant_id')
    # ### end Alembic commands ###
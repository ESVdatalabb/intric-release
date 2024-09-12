"""add crawl runs table
Revision ID: 7480251bb46b
Revises: d48c7ec8a356
Create Date: 2024-05-17 10:19:58.333457
"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic
revision = '7480251bb46b'
down_revision = 'd48c7ec8a356'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'crawl_runs',
        sa.Column('pages_crawled', sa.Integer(), nullable=True),
        sa.Column('files_downloaded', sa.Integer(), nullable=True),
        sa.Column('pages_failed', sa.Integer(), nullable=True),
        sa.Column('files_failed', sa.Integer(), nullable=True),
        sa.Column('completed_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('crawl_id', sa.UUID(), nullable=False),
        sa.Column('job_id', sa.UUID(), nullable=True),
        sa.Column(
            'id', sa.UUID(), server_default=sa.text('gen_random_uuid()'), nullable=False
        ),
        sa.Column(
            'created_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.Column(
            'updated_at',
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ['crawl_id'],
            ['crawls.id'],
        ),
        sa.ForeignKeyConstraint(['job_id'], ['jobs.uuid'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
    )

    op.add_column('crawls', sa.Column('group_id', sa.UUID(), nullable=True))
    op.drop_constraint('crawls_tenant_id_fkey', 'crawls', type_='foreignkey')
    op.create_foreign_key(
        'crawls_groups_fkey',
        'crawls',
        'groups',
        ['group_id'],
        ['uuid'],
        ondelete='CASCADE',
    )
    op.drop_column('crawls', 'allowed_path')
    op.drop_column('crawls', 'tenant_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'crawls', sa.Column('tenant_id', sa.UUID(), autoincrement=False, nullable=True)
    )
    op.add_column(
        'crawls',
        sa.Column('allowed_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.drop_constraint('crawls_groups_fkey', 'crawls', type_='foreignkey')
    op.create_foreign_key(
        'crawls_tenant_id_fkey',
        'crawls',
        'tenants',
        ['tenant_id'],
        ['uuid'],
        ondelete='CASCADE',
    )
    op.drop_column('crawls', 'group_id')
    op.drop_table('crawl_runs')
    # ### end Alembic commands ###
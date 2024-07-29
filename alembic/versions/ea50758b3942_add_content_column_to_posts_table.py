"""add content column to posts table

Revision ID: ea50758b3942
Revises: 207b3b820b41
Create Date: 2024-07-27 21:57:45.821823

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea50758b3942'
down_revision: Union[str, None] = '207b3b820b41'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass

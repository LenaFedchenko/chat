"""chat messages

Revision ID: 7b12d9c4a8f1
Revises: 39f57dc9e37b
Create Date: 2026-06-29 12:30:00.000000

"""
from alembic import op
import sqlalchemy as sa


revision = '7b12d9c4a8f1'
down_revision = '39f57dc9e37b'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('chat') as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.create_unique_constraint('uq_chat_word', ['word'])
        batch_op.create_unique_constraint('uq_chat_owner_id', ['owner_id'])

    op.create_table(
        'message',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('text', sa.String(length=500), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('chat_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['chat_id'], ['chat.id']),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('message')

    with op.batch_alter_table('chat') as batch_op:
        batch_op.drop_constraint('uq_chat_owner_id', type_='unique')
        batch_op.drop_constraint('uq_chat_word', type_='unique')
        batch_op.drop_column('created_at')

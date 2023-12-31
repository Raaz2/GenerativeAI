"""done

Revision ID: 874de3d0500c
Revises: 
Create Date: 2023-07-07 23:54:51.085278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '874de3d0500c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dish',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_name', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_dish',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('dish_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['dish_id'], ['dish.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('order_id', 'dish_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_dish')
    op.drop_table('orders')
    op.drop_table('dish')
    # ### end Alembic commands ###

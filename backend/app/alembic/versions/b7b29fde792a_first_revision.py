"""first revision

Revision ID: b7b29fde792a
Revises: 
Create Date: 2022-11-30 09:09:32.675022

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'b7b29fde792a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('beta_risk_index',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('index_name', sa.String(), nullable=True),
                    sa.Column('index_symbols', sa.String(), nullable=True),
                    sa.Column('timeframe', sa.String(), nullable=True),
                    sa.Column('cache_uid', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('broker',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('data_source',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('uni_symbol',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('base', sa.String(), nullable=True),
                    sa.Column('quote', sa.String(), nullable=True),
                    sa.Column('symbol', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('symbol')
                    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('firstname', sa.String(length=120), nullable=True),
                    sa.Column('lastname', sa.String(length=120), nullable=True),
                    sa.Column('username', sa.String(length=120), nullable=True),
                    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(), nullable=False),
                    sa.Column('email', sqlalchemy_utils.types.email.EmailType(), nullable=False),
                    sa.Column('phone_number', sqlalchemy_utils.types.phone_number.PhoneNumberType(), nullable=False),
                    sa.Column('time_registered', sa.Float(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('phone_number'),
                    sa.UniqueConstraint('username')
                    )
    op.create_table('beta_risk',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('uni_symbol_id', sa.Integer(), nullable=True),
                    sa.Column('timestamp', sa.Float(), nullable=True),
                    sa.Column('beta', sa.Float(), nullable=True),
                    sa.Column('cache_uid', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['uni_symbol_id'], ['uni_symbol.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('contract',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('broker_id', sa.Integer(), nullable=True),
                    sa.Column('time_registered', sa.Float(), nullable=True),
                    sa.Column('expire_timestamp', sa.Float(), nullable=True),
                    sa.Column('update_timestamp', sa.Float(), nullable=True),
                    sa.Column('total_margin', sa.Float(), nullable=True),
                    sa.Column('risk_tolerance_pct', sa.Float(), nullable=True),
                    sa.Column('free_margin', sa.Float(), nullable=True),
                    sa.Column('total_risk', sa.Float(), nullable=True),
                    sa.Column('free_risk', sa.Float(), nullable=True),
                    sa.Column('total_open_position', sa.Integer(), nullable=True),
                    sa.Column('pnl', sa.Float(), nullable=True),
                    sa.ForeignKeyConstraint(['broker_id'], ['data_source.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('srls',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('uni_symbol_id', sa.Integer(), nullable=True),
                    sa.Column('signal_engine_signature', sa.String(), nullable=False),
                    sa.Column('timeframes', sa.String(), nullable=True),
                    sa.Column('calculators', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['uni_symbol_id'], ['uni_symbol.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('stream_processors',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('processor', sa.String(), nullable=True),
                    sa.Column('template_name', sa.String(), nullable=True),
                    sa.Column('logic', sa.String(), nullable=True),
                    sa.Column('input', sa.String(), nullable=True),
                    sa.Column('output', sa.String(), nullable=True),
                    sa.Column('uni_symbol_id', sa.Integer(), nullable=True),
                    sa.Column('engine', sa.String(), nullable=True),
                    sa.Column('signature', sa.String(), nullable=True),
                    sa.Column('logic_model', sa.LargeBinary(), nullable=True),
                    sa.Column('input_model', sa.LargeBinary(), nullable=True),
                    sa.Column('output_model', sa.LargeBinary(), nullable=True),
                    sa.ForeignKeyConstraint(['uni_symbol_id'], ['uni_symbol.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('symbol',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('data_source_id', sa.Integer(), nullable=True),
                    sa.Column('uni_symbol_id', sa.Integer(), nullable=True),
                    sa.Column('symbol', sa.String(), nullable=True),
                    sa.Column('market', sa.String(), nullable=True),
                    sa.Column('list_timestamp', sa.Float(), nullable=True),
                    sa.ForeignKeyConstraint(['data_source_id'], ['data_source.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['uni_symbol_id'], ['uni_symbol.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('user_broker',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('broker_id', sa.Integer(), nullable=True),
                    sa.Column('api_type', sa.String(), nullable=True),
                    sa.Column('api_key', sa.String(), nullable=False),
                    sa.Column('api_secret', sa.String(), nullable=True),
                    sa.Column('api_password', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['broker_id'], ['data_source.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('analysis_quality',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('signal_generator_id', sa.Integer(), nullable=True),
                    sa.Column('timestamp', sa.Float(), nullable=True),
                    sa.Column('score', sa.Float(), nullable=True),
                    sa.Column('rise_std_price_pct', sa.Float(), nullable=True),
                    sa.Column('rise_mean_price_pct', sa.Float(), nullable=True),
                    sa.Column('rise_max_price_pct', sa.Float(), nullable=True),
                    sa.Column('fall_std_price_pct', sa.Float(), nullable=True),
                    sa.Column('fall_mean_price_pct', sa.Float(), nullable=True),
                    sa.Column('fall_max_price_pct', sa.Float(), nullable=True),
                    sa.Column('risk', sa.Float(), nullable=True),
                    sa.ForeignKeyConstraint(['signal_generator_id'], ['stream_processors.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('analysis_signal',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('signal_generator_id', sa.Integer(), nullable=True),
                    sa.Column('uni_symbol_id', sa.Integer(), nullable=True),
                    sa.Column('engine', sa.String(), nullable=True),
                    sa.Column('timestamp', sa.Float(), nullable=True),
                    sa.Column('instant_price', sa.Float(), nullable=True),
                    sa.Column('signal_type', sa.String(), nullable=True),
                    sa.Column('analysis_style', sa.Integer(), nullable=True),
                    sa.Column('optimizer_tag', sa.Integer(), nullable=True),
                    sa.Column('quality', sa.String(), nullable=True),
                    sa.Column('consumption_pattern', sa.Integer(), nullable=True),
                    sa.Column('mode', sa.Integer(), nullable=True),
                    sa.Column('expire_configs', sa.String(), nullable=True),
                    sa.Column('cache_uid', sa.String(), nullable=True),
                    sa.Column('cache_path_info', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['signal_generator_id'], ['stream_processors.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['uni_symbol_id'], ['uni_symbol.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('base_signal',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('uid', sa.String(), nullable=True),
                    sa.Column('signal_generator_id', sa.Integer(), nullable=True),
                    sa.Column('timestamp', sa.Float(), nullable=True),
                    sa.Column('timeframe', sa.String(), nullable=True),
                    sa.Column('signal_type', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['signal_generator_id'], ['stream_processors.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('uid')
                    )
    op.create_table('closed_positions',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('contract_id', sa.Integer(), nullable=True),
                    sa.Column('generic_routing_key', sa.Integer()),
                    sa.Column('open_timestamp', sa.Float(), nullable=True),
                    sa.Column('close_timestamp', sa.Float(), nullable=True),
                    sa.Column('position', sa.LargeBinary(), nullable=True),
                    sa.Column('pnl', sa.Float(), nullable=True),
                    sa.Column('position_type', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('contract_session_performances',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('contract_id', sa.Integer(), nullable=False),
                    sa.Column('cluster_type', sa.Enum('Position', 'Swing', 'Scalp', name='enginemode'), nullable=True),
                    sa.Column('start_margin', sa.Float(), nullable=True),
                    sa.Column('pnl', sa.Float(), nullable=True),
                    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('generic_positions',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('signal_publisher_id', sa.Integer(), nullable=True),
                    sa.Column('generic_position', sa.LargeBinary(), nullable=False),
                    sa.Column('signal_generator_id', sa.Integer(), nullable=True),
                    sa.Column('direct_signal_timestamp', sa.Float(), nullable=False),
                    sa.Column('task_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['signal_publisher_id'], ['stream_processors.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('generic_positions_archive',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('signal_publisher_id', sa.Integer(), nullable=True),
                    sa.Column('generic_position', sa.LargeBinary(), nullable=False),
                    sa.Column('signal_generator_id', sa.Integer(), nullable=True),
                    sa.Column('direct_signal_timestamp', sa.Float(), nullable=False),
                    sa.ForeignKeyConstraint(['signal_publisher_id'], ['stream_processors.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('open_positions',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('contract_id', sa.Integer(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('generic_position_rk', sa.Integer(), nullable=True),
                    sa.Column('position', sa.LargeBinary(), nullable=True),
                    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('srl',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('signal_engine_signature', sa.String(), nullable=False),
                    sa.Column('uni_symbol_id', sa.Integer(), nullable=True),
                    sa.Column('timeframe', sa.String(), nullable=True),
                    sa.Column('calculator', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['uni_symbol_id'], ['uni_symbol.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('srlevel',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('srls_id', sa.Integer(), nullable=True),
                    sa.Column('average_price', sa.Float(), nullable=True),
                    sa.Column('std_price', sa.Float(), nullable=True),
                    sa.Column('quality', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['srls_id'], ['srls.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('open_orders',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('position_id', sa.Integer(), nullable=True),
                    sa.Column('contract_id', sa.Integer(), nullable=True),
                    sa.Column('status', sa.Integer(), nullable=True),
                    sa.Column('uid', sa.String(), nullable=True),
                    sa.Column('order', sa.LargeBinary(), nullable=True),
                    sa.ForeignKeyConstraint(['contract_id'], ['contract.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['position_id'], ['open_positions.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('optimized_signal',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('signal_optimizer_id', sa.Integer(), nullable=True),
                    sa.Column('uni_symbol_id', sa.Integer(), nullable=True),
                    sa.Column('analysis_signal_id', sa.Integer(), nullable=True),
                    sa.Column('timestamp', sa.Float(), nullable=True),
                    sa.Column('direct_signal_timestamp', sa.Float(), nullable=True),
                    sa.Column('analysis_score', sa.Float(), nullable=True),
                    sa.Column('analysis_risk', sa.Float(), nullable=True),
                    sa.Column('cache_uid', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['analysis_signal_id'], ['analysis_signal.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['signal_optimizer_id'], ['stream_processors.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['uni_symbol_id'], ['uni_symbol.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('optimizer_signal_pool',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('analysis_signal_id', sa.Integer(), nullable=True),
                    sa.Column('signal_optimizer_id', sa.Integer(), nullable=True),
                    sa.Column('uni_symbol_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['analysis_signal_id'], ['analysis_signal.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['signal_optimizer_id'], ['stream_processors.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['uni_symbol_id'], ['uni_symbol.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('signal_archive',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('uid', sa.String(), nullable=True),
                    sa.Column('base_signal_id', sa.Integer(), nullable=True),
                    sa.Column('init_price', sa.Float(), nullable=True),
                    sa.Column('signal_type', sa.String(), nullable=True),
                    sa.Column('status', sa.Integer(), nullable=True),
                    sa.Column('stamp_period', sa.Integer(), nullable=True),
                    sa.Column('stamp_step', sa.String(), nullable=True),
                    sa.Column('stamps', sa.String(), nullable=True),
                    sa.Column('task_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['base_signal_id'], ['base_signal.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('srline_raw',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('srl_id', sa.Integer(), nullable=True),
                    sa.Column('timestamp', sa.Float(), nullable=True),
                    sa.Column('index_price', sa.Float(), nullable=True),
                    sa.Column('open', sa.Float(), nullable=True),
                    sa.Column('high', sa.Float(), nullable=True),
                    sa.Column('low', sa.Float(), nullable=True),
                    sa.Column('close', sa.Float(), nullable=True),
                    sa.Column('volume', sa.Float(), nullable=True),
                    sa.ForeignKeyConstraint(['srl_id'], ['srl.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('srline',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('srls_id', sa.Integer(), nullable=True),
                    sa.Column('srline_raw_id', sa.Integer(), nullable=True),
                    sa.Column('srlevel_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['srls_id'], ['srls.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['srline_raw_id'], ['srline_raw.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['srlevel_id'], ['srlevel.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    op.create_table('signal_quality',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('signal_archive_id', sa.Integer(), nullable=True),
                    sa.Column('signal_generator_id', sa.Integer(), nullable=True),
                    sa.Column('score', sa.Float(), nullable=True),
                    sa.Column('rise_mean_price_pct', sa.Float(), nullable=True),
                    sa.Column('rise_max_price_pct', sa.Float(), nullable=True),
                    sa.Column('fall_mean_price_pct', sa.Float(), nullable=True),
                    sa.Column('fall_max_price_pct', sa.Float(), nullable=True),
                    sa.ForeignKeyConstraint(['signal_archive_id'], ['signal_archive.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['signal_generator_id'], ['stream_processors.id'], onupdate='CASCADE', ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    # ### end Alembic commands ###

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('signal_quality')
    op.drop_table('srline')
    op.drop_table('srline_raw')
    op.drop_table('signal_archive')
    op.drop_table('optimizer_signal_pool')
    op.drop_table('optimized_signal')
    op.drop_table('open_orders')
    op.drop_table('srlevel')
    op.drop_table('srl')
    op.drop_table('open_positions')
    op.drop_table('generic_positions_archive')
    op.drop_table('generic_positions')
    op.drop_table('contract_session_performances')
    op.drop_table('closed_positions')
    op.drop_table('base_signal')
    op.drop_table('analysis_signal')
    op.drop_table('analysis_quality')
    op.drop_table('user_broker')
    op.drop_table('symbol')
    op.drop_table('stream_processors')
    op.drop_table('srls')
    op.drop_table('contract')
    op.drop_table('beta_risk')
    op.drop_table('user')
    op.drop_table('uni_symbol')
    op.drop_table('data_source')
    op.drop_table('broker')
    op.drop_table('beta_risk_index')
    # ### end Alembic commands ###

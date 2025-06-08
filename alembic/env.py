from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from models import brands, categories, inventory, media, product_specs, products, specifications

from dotenv import load_dotenv
from config import settings

load_dotenv()

from database import Base



config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata
# show changes in database structure
# print(target_metadata.tables)


def run_migrations_offline() -> None:
    context.configure(
        url=settings.get_synk_database_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        {
            "sqlalchemy.url": settings.get_synk_database_url(),
        },
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
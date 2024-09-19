from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession
from pydantic_settings import SettingsConfigDict, BaseSettings


class db_config(BaseSettings):
    DB_URL: str
    # строка из .env файла
    # DB_URL=postgresql+psycopg://name:password@host/db_name

    model_config = SettingsConfigDict(env_file=".env")


class DataBaseHelper:

    def __init__(self,
                 url: str,
                 echo: bool = False,
                 echo_pool: bool = False,
                 pool_size: int = 5,
                 max_overflow: int = 10) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
            connect_args={"options": "-c timezone=utc"}
        )

        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session


db_conf = db_config()

db_helper = DataBaseHelper(
    url=db_conf.DB_URL,
    echo=False,
    echo_pool=False,
    pool_size=5,
    max_overflow=10
)

from dependency_injector import containers, providers

from pdp.database import Database
from pdp.repositories import UserRepository

from . import services


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".endpoints"])
    config = providers.Configuration(yaml_files=["config.yaml"])
    db = providers.Singleton(Database, db_url=config.db.url)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        services.UserService, user_repository=user_repository
    )

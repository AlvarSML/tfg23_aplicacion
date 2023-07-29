import logging

from app.db.init_db import init_db
from app.db.session import SessionLocal

from app.db.base_class import Base

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init() -> None:
    db = SessionLocal()
    init_db(db)
    logger.info("BDD iniciada")
    logger.info(Base.metadata.tables.keys())



def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    # Probando sqalchemy
    
    main()

from pedesis.logger import get_logger

from pedesis.db.maker import init_all_tables
from pedesis.shortcuts import get_db

logger = get_logger()

def main() -> None:
    logger.info("Creating initial data")
    init_all_tables()
    logger.info("Initial data created")


if __name__ == '__main__':
    main()

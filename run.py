from app.database.db import create_tables
from app.main import start_app

if __name__ == "__main__":
    create_tables()
    start_app()
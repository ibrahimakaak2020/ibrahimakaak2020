import os
from dotenv import load_dotenv, dotenv_values

from pathlib import Path
#env_path = Path('.') / '.env'
#dotenv_path=env_path
load_dotenv()

config = dotenv_values(".env") 

class Settings:
    PROJECT_NAME:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_USER : str = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_SERVER : str = os.getenv("DATABASE_SERVER")
    DATABASE_PORT : str = os.getenv("DATABASE_PORT") # default postgres port is 5432
    DATABASE_DB : str = os.getenv("DATABASE_DB")
    DATABASE_URL = f"mysql+mysqldb://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}/{DATABASE_DB}"
                    #"mysql+mysqldb://root:sqhadmin@localhost/sqhit"

settings = Settings()




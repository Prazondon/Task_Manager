from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_url = "postgresql://mypostgre_ykxq_user:IMZcJIfxLfOqn0PoAyvicBw93T4q21ju@dpg-d952s75ckfvc73aqfdtg-a/mypostgre_ykxq"

engine = create_engine(database_url, echo = True)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)


Base = declarative_base()


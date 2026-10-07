from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_url = "postgresql://taskmanager_37dy_user:Rp5tlHOR4xz2Sa8KUMAFbThf3fOCaLSc@dpg-db368mijnfac738raseg-a/taskmanager_37dy"

engine = create_engine(database_url, echo = True)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)


Base = declarative_base()


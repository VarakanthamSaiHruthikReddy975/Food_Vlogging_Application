from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# creating SQLAlchemy engine
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True, # This is to test connection before using it, to avoid using stale connections
    echo=settings.debug, # log SQL in debug mode
    pool_size=5, # Connection pool size
    max_overflow=10 # this is for extra connections if needed
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
    )

# Base class for models
Base = declarative_base()

# main function to get db session
def get_db():
    @app.get("/users")
    def get_users(db: Session = Depends(get_db)):
        users = db.query(User).all()
        return users
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
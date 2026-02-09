from pydantic_settings import BaseSettings
from pydantic import computed_field

class Settings(BaseSettings):
    db_usr: str
    db_password: str
    db_name: str
    db_port: int = 5432

    @computed_field
    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    # Security
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Application
    app_name: str = "Food Vlog API"
    debug: bool = True
    environment: str = "development"

    class Config:
        env_file = ".env"
        case_sensitive = False

# Global settings instance
settings = Settings()
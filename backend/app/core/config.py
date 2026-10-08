from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Color Designer"
    API_V1_STR: str = "/api/v1"
    
    SECRET_KEY: str = "supersecretkey-change-this-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    
    DATABASE_URL: str = "mysql+pymysql://root:root@MySQL-8.2:3306/ai_color_designer"
    
    UPLOAD_DIR: str = "../storage/uploads"
    PROCESSED_DIR: str = "../storage/processed"
    MODELS_DIR: str = "../storage/models"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()

class Config:
    INTERNAL_HOST = "localhost"
    STAGING_HOST = "localhost"
    PRODUCTION_HOST = "localhost"

    REDIS_BROKER_URL = "redis://localhost:6379/0"
    REDIS_RESULT_BACKEND = "redis://localhost:6379/1"

    DATABASE_URI = None

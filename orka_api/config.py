import os


class Config:
    DEBUG = True

    COGNITO_REGION = os.environ.get("COGNITO_REGION", "us-east-1")
    COGNITO_USERPOOL_ID = os.environ.get(
        "COGNITO_USERPOOL_ID", "us-east-1_pdrrhWtb9"
    )
    COGNITO_CHECK_TOKEN_EXPIRATION = False

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///db.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CORS_ORIGINS_GLOBAL = ["http://localhost:3000"]
    CORS_ALLOW_CREDENTIALS_GLOBAL = True
    CORS_MAX_AGE = 600

    FLASK_ADMIN_SWATCH = "paper"

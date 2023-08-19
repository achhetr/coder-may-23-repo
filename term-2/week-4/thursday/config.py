import os

class BaseConfig(object):
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        # if error in connection use
        # 
        db = os.environ.get("DATABASE_URL")

        if db is None:
            raise ValueError("Missing environment value for `DATABASE_URL`")

        return db

class DevelopementConfig(BaseConfig):
    DEBUG = True


class TestingConfig(DevelopementConfig):
    pass

class ProductionConfig(BaseConfig):
    pass


current_env = os.environ.get("FLASK_ENV")

if current_env == "testing":
    app_config = TestingConfig()
elif current_env == "production":
    app_config = ProductionConfig()
else:
    app_config = DevelopementConfig()





import os

config_variables = {
    'ENV': os.getenv('WORKING_ENV') or 'develop',
    'POSTGRES_DB_HOST': os.getenv('POSTGRES_DB_HOST') or 'no db host',
    'POSTGRES_DB_PORT': os.getenv('POSTGRES_DB_PORT') or 'no db host',
    'POSTGRES_DB_PASSWORD': os.getenv('POSTGRES_DB_PASSWORD') or 'no db password',
    'POSTGRES_DB_USER': os.getenv('POSTGRES_DB_USER') or 'no db user',
    'POSTGRES_DB_DATABASE': os.getenv('POSTGRES_DB_DATABASE') or 'no db database',
    'POSTGRES_DB_SCHEMA': os.getenv('POSTGRES_DB_SCHEMA') or 'no db schema',
    'POSTGRES_DB_TABLE': os.getenv('POSTGRES_DB_TABLE') or 'no db table',
}


class Config(object):
    def __init__(self):
        self._config = config_variables

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]


class BasicConfig(Config):

    @property
    def env(self):
        return self.get_property('ENV')

    @property
    def db_host(self):
        return self.get_property('POSTGRES_DB_HOST')

    @property
    def db_port(self):
        return self.get_property('POSTGRES_DB_PORT')

    @property
    def db_password(self):
        return self.get_property('POSTGRES_DB_PASSWORD')

    @property
    def db_user(self):
        return self.get_property('POSTGRES_DB_USER')

    @property
    def db_database(self):
        return self.get_property('POSTGRES_DB_DATABASE')

    @property
    def db_schema(self):
        return self.get_property('POSTGRES_DB_SCHEMA')

    @property
    def db_table(self):
        return self.get_property('POSTGRES_DB_TABLE')


config_by_name = dict(
    BasicConfig=BasicConfig()
)

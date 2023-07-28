from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

cfg = ConfigParser()
cfg.read('./app/config/dbConfig.ini')

POOL_SIZE = 20
POOL_RECYCLE = 3600
POOL_TIMEOUT = 15
MAX_OVERFLOW = 2
CONNECT_TIMEOUT = 60


def getMysqlUrl():
    '''获取mysql链接
    '''
    dbHost = cfg.get(section='mysql', option='BASE_HOST')
    dbUser = cfg.get(section='mysql', option='BASE_USER')
    dbPwd = cfg.get(section='mysql', option='BASE_PASSWORD')
    dbPort = cfg.get(section='mysql', option='BASE_PORT')
    dbName = cfg.get(section='mysql', option='BASE_DB')
    return f'mysql+pymysql://{dbUser}:{dbPwd}@{dbHost}:{dbPort}/{dbName}?charset=utf8'


class Database():
    def __init__(self) -> None:
        self.connection_is_active = False
        self.engine = None

    def get_db_connection(self):
        if self.connection_is_active == False:
            connect_args = {'connect_timeout': CONNECT_TIMEOUT}
            try:
                self.engine = create_engine(
                    getMysqlUrl(),
                    pool_size=POOL_SIZE,
                    pool_recycle=POOL_RECYCLE,
                    pool_timeout=POOL_TIMEOUT,
                    max_overflow=MAX_OVERFLOW,
                    connect_args=connect_args)
                return self.engine
            except Exception as e:
                print('Error connecting to MySQL DB:', e)
        return self.engine

    def get_db_session(self):
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()
            return session
        except Exception as e:
            print('Error getting DB session:', e)
        return None

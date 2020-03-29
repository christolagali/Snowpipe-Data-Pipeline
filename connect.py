import config_files.snowflakeconfig as sfc
import snowflake.connector
from sqlalchemy import create_engine
from snowflake.sqlalchemy import URL


def getConnection():
    try:

        connection = snowflake.connector.connect(
            user=sfc.creds['user'],
            password=sfc.creds['pass'],
            account=sfc.creds['account'],
            warehouse=sfc.creds['warehouse'],
            database=sfc.creds['database']

        )

        return connection

    except Exception as e:
        print(e)










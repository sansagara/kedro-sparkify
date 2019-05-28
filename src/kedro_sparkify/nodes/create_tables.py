from .sql_queries import create_table_queries, drop_table_queries
from kedro.config import ConfigLoader
import psycopg2


# CONFIG
conf_paths = ['conf/base']
conf_loader = ConfigLoader(conf_paths)
config = conf_loader.get('credentials*', 'credentials*/**')


def get_cur():
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['dev_redshift'].values()))
    return conn.cursor(), conn


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

import os
from psycopg2 import connect
from psycopg2.extras import execute_values

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": f"{os.getenv("POSTGRES_DATABASE")}",
    "user": f"{os.getenv("POSTGRES_USERNAME")}",
    "password": f"{os.getenv("POSTGRES_PASSWORD")}",
}

def get_connection(db_config):
    return connect(**db_config)

def filter_new_items(conn, items):
    links = [i["link"] for i in items]

    if not links:
        return []
    
    with conn.cursor() as cur:
        cur.execute("SELECT link FROM news WHERE link = ANY(%s)", (links,))
        existing = {row[0] for row in cur.fetchall()}
    
    return [i for i in items if i["link"] not in existing]

def bulk_insert(conn, items):
    if not items:
        return
    rows = [
        (i["title"], i["link"], i["publication_date"], i["sentiment"], i["about_svo"])
        for i in items
    ]
    with conn.cursor() as cur:
        execute_values(
            cur,
            """
            INSERT INTO news (title, link, publication_datem, sentiment, about_svo)
            VALUES %s
            ON CONFLICT (link) DO NOTHING
            """,
            rows,
        )
    conn.commit()
import pandas as pd


def select_data(db_conn, input):
    query = 'SELECT * FROM idols '
    if input != 0:
        query += f'WHERE idol_id = {input}'
    df = pd.read_sql_query(query, db_conn)
    return df
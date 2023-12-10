import pandas as pd

id_columns = {'idols': 'idol_id', 'groups': 'group_id', 'companies': 'company_id'}

def select_data(db_conn, table, input):
    id_col = id_columns.get(table)
    query = f'SELECT * FROM {table}'
    if input != 0:
        query += f'WHERE {id_col} = {input}'
    df = pd.read_sql_query(query, db_conn)
    return df
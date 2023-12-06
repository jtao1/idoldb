import sqlalchemy

def delete_row(db_conn, table, id_col, id):
    query = sqlalchemy.text(f"""
        DELETE FROM {table}
        WHERE {id_col} = :id
    """
    )
    db_conn.execute(
        query,
        {"id": id}
    )
    db_conn.commit()
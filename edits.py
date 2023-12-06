import sqlalchemy

def edit_query(db_conn, table, col, id, row, new_val):
    query = sqlalchemy.text(f"""
        UPDATE {table}
        SET {col} = :new_val
        WHERE {row} = :id
    """
    )
    db_conn.execute(
        query, 
        {"new_val": new_val, "id": id}
    )
    db_conn.commit()


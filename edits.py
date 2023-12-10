import sqlalchemy

id_dict = {'idols':'idol_id', 'group_':'group_id', 'company':'company_id'}

def edit_query(db_conn, table, col, id, new_val):
    query = sqlalchemy.text(f"""
        UPDATE {table}
        SET {col} = :new_val
        WHERE {id_dict[table]} = :id
    """
    )
    db_conn.execute(
        query, 
        {"new_val": new_val, "id": id}
    )
    db_conn.commit()


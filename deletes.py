import sqlalchemy

id_columns = {'idols': 'idol_id', 'groups': 'group_id', 'companies': 'company_id'}


def delete_row(db_conn, table, id):
    query = sqlalchemy.text(f"""
        DELETE FROM {table}
        WHERE {id_columns.get(table)} = :id
    """
    )
    db_conn.execute(
        query,
        {"id": id}
    )
    db_conn.commit()
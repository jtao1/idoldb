from sqlalchemy import text
import connect

id_dict = {'idols':'idol_id', 'group_':'group_id', 'company':'company_id'}

delete_row = '''
    CREATE PROCEDURE DeleteRow(
        IN p_table VARCHAR(255),
        IN p_id_col VARCHAR(255),
        IN p_id INT
    )
    BEGIN
        SET @delete_query = CONCAT(
            'DELETE FROM ', p_table,
            ' WHERE ', p_id_col, ' = ', p_id
        );

        PREPARE stmt FROM @delete_query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END;
'''

def delete_row(db_conn, table, id):
    engine, session = db_conn
    id_col = id_dict.get(table)
    with engine.connect().execution_options(autocommit=True) as conn:
        conn.execute(text('CALL DeleteRow(:table_name, :id_col, :id)'), 
                     {'table_name': table, 'id_col': id_col, 'id': id})    
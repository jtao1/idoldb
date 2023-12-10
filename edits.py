from sqlalchemy import text
import connect

id_dict = {'idols':'idol_id', 'group_':'group_id', 'company':'company_id'}

edit_query = '''
CREATE PROCEDURE EditQuery(
    IN p_table VARCHAR(255),
    IN p_col VARCHAR(255),
    IN p_id INT,
    IN p_id_col VARCHAR(255),
    IN p_new_val VARCHAR(255)
)
BEGIN
    SET @update_query = CONCAT(
        'UPDATE ', p_table,
        ' SET ', p_col, ' = ?',
        ' WHERE ', p_id_col, ' = ?'
    );

    SET @p_new_val = p_new_val;
    SET @p_id = p_id;

    PREPARE stmt FROM @update_query;
    EXECUTE stmt USING @p_new_val, @p_id;
    DEALLOCATE PREPARE stmt;
END;
'''

def edit_query(db_conn, table, col, id, new_val):
    engine, session = db_conn
    id_col = id_dict.get(table)
    with engine.connect().execution_options(autocommit=True) as conn:
        conn.execute(text('CALL EditQuery(:table_name, :col, :id, :id_col, :new_val)'), 
                     {'table_name': table, 'col': col, 'id': id, 'id_col': id_col, 'new_val': new_val})    


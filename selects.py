import pandas as pd
from sqlalchemy import text
import connect

id_dict = {'idols':'idol_id', 'group_':'group_id', 'company':'company_id'}

select_data = text('''
    CREATE PROCEDURE SelectData(
        IN table_name VARCHAR(255),
        IN input_value INT,
        IN id_col VARCHAR(255)
    )
    BEGIN
        -- Construct the SQL query
        SET @query_text = CONCAT('SELECT * FROM ', table_name);

        -- Check if input_value is provided for filtering
        IF input_value != -1 THEN
            SET @query_text = CONCAT(@query_text, ' WHERE ', id_col, ' = ', input_value);
        END IF;

        -- Execute the SQL query using prepared statement
        PREPARE stmt FROM @query_text;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END
''')

# engine, session = connect.db_conn()

# drop_procedure_statement = f"DROP PROCEDURE IF EXISTS SelectData;"
# # Execute the statement
# # with engine.connect() as conn:
# #     conn.execute(drop_procedure_statement)
# with engine.connect() as conn:
#     conn.execute(select_data)

def select_data(db_conn, table, input_value):
    engine, session = db_conn
    id_col = id_dict.get(table)
    with engine.connect().execution_options(autocommit=True) as conn:
        result = conn.execute(text('CALL SelectData(:table_name, :input_value, :id_col)'), 
                               {'table_name': table, 'input_value': input_value, 'id_col': id_col})    
        df = pd.DataFrame(result.fetchall())    
    return df
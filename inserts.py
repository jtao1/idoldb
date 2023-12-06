import sqlalchemy

def idol_insert_row(db_conn, table, data):
    insert_idol = sqlalchemy.text(
        f"""INSERT INTO 
        {table} (idol_id, name, stage_name, group_, company, country, birthdate, height_cm) 
        VALUES (:id, :name, :stage_name, :group_, :company, :country, :birthdate, :height_cm)"""
    )
    id, name, stage_name, group, company, country, birthdate, height = data
    db_conn.execute(insert_idol, parameters=
                    {'id': id, 'name': name, 'stage_name': stage_name, 'group_': group, 
                    'company': company, 'country': country, 'birthdate': birthdate, 'height_cm': height})
    db_conn.commit()
import sqlalchemy

def idol_insert_row(db_conn, table, data):
    if table == 'idols':
        insert_idol = sqlalchemy.text(
            f"""INSERT INTO 
            {table} (idol_id, name, stage_name, group_, company, country, birthdate, height_cm) 
            VALUES (:id, :name, :stage_name, :group_, :company, :country, :birthdate, :height_cm)"""
        )
        id, name, stage_name, group, company, country, birthdate, height = data
        db_conn.execute(insert_idol, parameters=
                        {'id': id, 'name': name, 'stage_name': stage_name, 'group_': group, 
                        'company': company, 'country': country, 'birthdate': birthdate, 'height_cm': height})
    
    elif table == 'group_':
        insert_group = sqlalchemy.text(
            f"""INSERT INTO
            {table} (code, company, group_id, member_count, name)
            VALUES (:code, :company, :id, :members, :name)"""
        )
        id, name, code, company, members = data
        code = '' if None else code
        db_conn.execute(insert_group, parameters=
                        {'code': code, 'company': company, 'id': id, 'members': members, 'name': name})
    
    elif table == 'company':
        insert_company = sqlalchemy.text(
            f"""INSERT INTO
            {table} (company_id, company_name, group_count, idol_count)
            VALUES (:id, :name, :groups, :members)"""
        )
        id, name, groups, members = data
        db_conn.execute(insert_company, parameters=
                        {'id': id, 'name': name, 'groups': groups, 'members': members})
    db_conn.commit()
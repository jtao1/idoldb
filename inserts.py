from sqlalchemy import text

insert_idol = '''
    CREATE PROCEDURE InsertIdol(
        IN p_id INT,
        IN p_name VARCHAR(255),
        IN p_stage_name VARCHAR(255),
        IN p_group VARCHAR(255),
        IN p_company VARCHAR(255),
        IN p_country VARCHAR(255),
        IN p_birthdate DATE,
        IN p_gender VARCHAR(255),
        IN p_height_cm INT
    )
    BEGIN
        DECLARE table_name VARCHAR(255);
        
        SET table_name = 'idols';

        IF table_name = 'idols' THEN
            INSERT INTO idols (idol_id, name, stage_name, group_, company, country, birthdate, gender, height_cm) 
            VALUES (p_id, p_name, p_stage_name, p_group, p_company, p_country, p_birthdate, p_gender, p_height_cm);
        END IF;
    END;
'''

insert_group = '''
    CREATE PROCEDURE InsertGroup(
        IN p_id INT,
        IN p_name VARCHAR(255),
        IN p_code VARCHAR(255),
        IN p_company VARCHAR(255),
        IN p_members INT
    )
    BEGIN
        DECLARE table_name VARCHAR(255);

        SET table_name = 'group_';

        IF table_name = 'group_' THEN
            INSERT INTO group_ (code, company, group_id, member_count, name)
            VALUES (COALESCE(NULLIF(p_code, ''), NULL), p_company, p_id, p_members, p_name);
        END IF;
    END;
'''

insert_company = '''
    CREATE PROCEDURE InsertCompany(
        IN p_id INT,
        IN p_name VARCHAR(255),
        IN p_groups INT,
        IN p_members INT
    )
    BEGIN
        DECLARE table_name VARCHAR(255);

        SET table_name = 'company';

        IF table_name = 'company' THEN
            INSERT INTO company (company_id, company_name, group_count, idol_count)
            VALUES (p_id, p_name, p_groups, p_members);
        END IF;
    END;
'''

def idol_insert_row(db_conn, table, data):
    engine, session = db_conn
    with engine.connect().execution_options(autocommit=True) as conn:
        if table == 'idols':
            id, name, stage_name, group, company, country, birthdate, gender, height = data
            conn.execute(text('CALL InsertIdol(:id, :name, :stage_name, :group, :company, :country, :birthdate, :gender, :height)'), 
                         {'id': id, 'name': name, 'stage_name': stage_name, 'group': group, 'company': company, 
                          'country': country, 'birthdate': birthdate, 'gender': gender, 'height': height})
             
        elif table == 'group_':
            id, name, code, company, members = data
            code = '' if None else code
            conn.execute(text('CALL InsertGroup(:id, :name, :code, :company, :members)'),
                         {'code': code, 'company': company, 'id': id, 'members': members, 'name': name})
        
        elif table == 'company':
            id, name, groups, members = data
            conn.execute(text('CALL InsertCompany(:id, :name, :groups, :members)'),
                         {'id': id, 'name': name, 'groups': groups, 'members': members})

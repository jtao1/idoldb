import panel as pn
import pandas as pd

import connect
import widgets

import inserts
import selects
import edits
import deletes
import datetime

#widgets
sql_select = widgets.select()
sql_idol_insert = widgets.idol_insert()
sql_group_insert = widgets.group_insert()
sql_company_insert = widgets.company_insert()
sql_edit = widgets.edit()
sql_delete = widgets.delete()
report_widgets = widgets.report()
insert_table_dict = {'idols':sql_idol_insert, 'group_':sql_group_insert, 'company':sql_company_insert}
for widgets in [sql_select, sql_idol_insert, sql_group_insert, sql_company_insert, sql_edit, sql_delete]:
    for widget in widgets:
        widget.width = 150

def execute_action(event):
    if table_menu.clicked == None:
       table_menu.clicked = table_menu.clicked or 'idols'
    main.objects = [main_row]
    
    if action_menu.clicked == 'select':
        df = selects.select_data(conn, table_menu.clicked, sql_select[0].value)
        if sql_select[2].value != 'none':
            df = df[df[sql_select[2].value] == sql_select[3].value]
        df_pane = pn.pane.DataFrame(df)
        reports(df)
        main.append(df_pane)
    elif action_menu.clicked == 'insert':
        data = [data.value for data in insert_table_dict[table_menu.clicked]]
        inserts.idol_insert_row(conn, table_menu.clicked, data)
    elif action_menu.clicked == 'edit':
        edits.edit_query(conn, table_menu.clicked, sql_edit[0].value, sql_edit[1].value, sql_edit[2].value)
    elif action_menu.clicked == 'delete':
        deletes.delete_row(conn, table_menu.clicked, sql_delete[0].value)
        sql_delete[0].name = 'work'

def sql_actions(event):
    main.objects = [main_row]
    main_sub_row.objects = []
    action_menu.name = 'SQL Action' if action_menu.clicked is None else next(display for display, value in action_menu_items if value == action_menu.clicked)
    table_menu.name = 'idols' if table_menu.clicked is None else next(display for display, value in table_menu_items if value == table_menu.clicked)
    if action_menu.clicked == 'select':
        main_sub_row.objects = sql_select
    elif action_menu.clicked == 'insert':
        if table_menu.clicked == 'idols' or table_menu.clicked == None:
            main_sub_row.objects = sql_idol_insert
        elif table_menu.clicked == 'group_':
            main_sub_row.objects = sql_group_insert
        elif table_menu.clicked == 'company':
            main_sub_row.objects = sql_company_insert
    elif action_menu.clicked == 'edit':
        main_sub_row.objects = sql_edit
    elif action_menu.clicked == 'delete':
        main_sub_row.objects = sql_delete

def reports(df):
    report.objects = []
    report.objects = report_widgets
    report.objects[0].value = str(len(df))
    report.objects[1].value = str(df['height_cm'].mean())

    df['birthdate'] = pd.to_datetime(df['birthdate'])
    df['age'] = (pd.to_datetime('today') - df['birthdate']).dt.days // 365.25
    report.objects[2].value = str(df['age'].mean())

conn = connect.db_conn()
pn.extension(sizing_mode='stretch_width')

main_button = pn.widgets.Button(name='Enter', button_type='primary', width=100)
main_button.on_click(execute_action)

action_menu_items = [('Select', 'select'), ('Insert', 'insert'), ('Edit', 'edit'), ('Delete', 'delete')]
action_menu = pn.widgets.MenuButton(name='SQL Action', items=action_menu_items, button_type='primary', width=100)
action_menu.on_click(sql_actions)

table_menu_items = [('Idols', 'idols'), ('Groups', 'group_'), ('Companies', 'company')]
table_menu = pn.widgets.MenuButton(name='Tables', items=table_menu_items, button_type='primary', width=100)
table_menu.on_click(sql_actions)

main_sub_row = pn.Row()
main_row = pn.Row(action_menu, table_menu, main_sub_row, main_button)
main = pn.Column(main_row)


report = pn.Column()

app = pn.Tabs(('Main', main), ('Report', report))

app.servable()


#TODO search bar, input name of idol, company, or group then show result
import panel as pn
import pandas as pd

import connect
import widgets

import inserts
import selects
import edits
import deletes

#widgets
idol_select = widgets.select()
idol_insert = widgets.idol_insert()
group_insert = widgets.group_insert()
company_insert = widgets.company_insert()
idol_edit = widgets.edit()
idol_delete = widgets.delete()
for widgets in [idol_select, idol_insert, group_insert, company_insert, idol_edit, idol_delete]:
    for widget in widgets:
        widget.width = 150

def execute_action(event):
    if table_menu.clicked == None:
        table_menu.clicked = 'idols'
    main.objects = [main_row]
    if action_menu.clicked == 'select':
        df = selects.select_data(conn, idol_select[0].value)
        df_pane = pn.pane.DataFrame(df)
        if df_pane in main.objects:
            main.remove(df_pane)
        main.append(df_pane)
    elif action_menu.clicked == 'insert':
        idol_data = [data.value for data in idol_insert]
        inserts.idol_insert_row(conn, table_menu.clicked, idol_data)
    elif action_menu.clicked == 'edit':
        edits.edit_query(conn, table_menu.clicked, idol_edit[0].value, idol_edit[1].value, idol_edit[2].value, idol_edit[3].value)
    elif action_menu.clicked == 'delete':
        deletes.delete_row(conn, table_menu.clicked, 'idol_id', idol_delete[0].value)

def sql_actions(event):
    main.objects = [main_row]
    main_sub_row.objects = []
    action_menu.name = action_menu.clicked or 'SQL Action'
    table_menu.name = table_menu.clicked or 'Tables'
    if action_menu.clicked == 'select':
        main_sub_row.objects = idol_select
    elif action_menu.clicked == 'insert':
        if table_menu.clicked == 'idols' or table_menu.clicked == None:
            main_sub_row.objects = idol_insert
        elif table_menu.clicked == 'groups':
            main_sub_row.objects = group_insert
        elif table_menu.clicked == 'companies':
            main_sub_row.objects = company_insert
    elif action_menu.clicked == 'edit':
        main_sub_row.objects = idol_edit
    elif action_menu.clicked == 'delete':
        main_sub_row.objects = idol_delete

conn = connect.db_conn()
pn.extension(sizing_mode='stretch_width')

main_button = pn.widgets.Button(name='Enter', button_type='primary', width=100)
main_button.on_click(execute_action)

action_menu_items = [('Select', 'select'), ('Insert', 'insert'), ('Edit', 'edit'), ('Delete', 'delete')]
action_menu = pn.widgets.MenuButton(name='SQL Action', items=action_menu_items, button_type='primary', width=100)
action_menu.on_click(sql_actions)

table_menu_items = [('Idols', 'idols'), ('Groups', 'groups'), ('Companies', 'companies')]
table_menu = pn.widgets.MenuButton(name='Tables', items=table_menu_items, button_type='primary', width=100)
table_menu.on_click(sql_actions)

main_sub_row = pn.Row()
main_row = pn.Row(action_menu, table_menu, main_sub_row, main_button)
main = pn.Column(main_row)

app = pn.Tabs(('Main', main), ('Report'))

app.servable()


#TODO search bar, input name of idol, company, or group then show result
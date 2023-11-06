import panel as pn
import pandas as pd

import inserts
import selects
import connect

def execute_action(event):
    if action_menu.clicked == 'select':
        df = selects.select_data(conn, select_input.value)
        df_pane = pn.pane.DataFrame(df)
        if df_pane in main.objects:
            main.remove(df_pane)
        main.append(df_pane)
        return df
    elif action_menu.clicked == 'insert':
        return
    elif action_menu.clicked == 'edit':
        return
    elif action_menu.clicked == 'delete':
        return
    
def input_row(event):
    idol_data = [main_row_idol_id.value, main_row_name.value, main_row_stage_name.value, main_row_group.value,
                  main_row_company.value, main_row_country.value, main_row_birthdate.value, main_row_height.value]
    inserts.idol_insert_row(conn, idol_data)

def action_row(event):
    main_sub_row.objects = []
    if action_menu.clicked == 'select':
        main_sub_row.append(select_input)
    elif action_menu.clicked == 'insert':
        main_sub_row.objects = [main_row_idol_id, main_row_name, main_row_stage_name, main_row_group, main_row_company, main_row_country, main_row_birthdate, main_row_height]
    elif action_menu.clicked == 'edit':
        return
    elif action_menu.clicked == 'delete':
        return

conn = connect.db_conn()
pn.extension(sizing_mode='stretch_width')

main_button = pn.widgets.Button(name='Enter', button_type='primary', width=100)
main_button.on_click(execute_action)

action_menu_items = [('Select', 'select'), ('Insert', 'insert'), ('Edit', 'edit'), ('Delete', 'delete')]
action_menu = pn.widgets.MenuButton(name='SQL Action', items=action_menu_items, button_type='primary', width=100)
action_menu.on_click(action_row)

table_menu_items = [('Idols', 'idols'), ('Groups', 'groups'), ('Companies', 'companies')]
table_menu = pn.widgets.MenuButton(name='Tables', items=table_menu_items, button_type='primary', width = 100)

main_sub_row = pn.Row()
main_row = pn.Row(action_menu, table_menu, main_sub_row, main_button)
main = pn.Column(main_row)

#action menu select
select_input = pn.widgets.IntInput(name='Input an idol_id or 0 to SELECT ALL')

#action menu insert
main_row_idol_id = pn.widgets.IntInput(name='id')
main_row_name = pn.widgets.TextInput(name='name')
main_row_stage_name = pn.widgets.TextInput(name='stage_name')
main_row_group = pn.widgets.TextInput(name='group')
main_row_company = pn.widgets.TextInput(name='company')
main_row_country = pn.widgets.TextInput(name='country')
main_row_birthdate = pn.widgets.TextInput(name='birthdate')
main_row_height = pn.widgets.IntInput(name='height (cm)')

app = pn.Tabs(('Main', main), ('Report'))

app.servable()



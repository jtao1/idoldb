import panel as pn
import pandas as pd

import inserts
import selects
import edits
import connect
import deletes

def execute_action(event):
    main.objects = [main_row]
    if action_menu.clicked == 'select':
        df = selects.select_data(conn, select_input.value)
        df_pane = pn.pane.DataFrame(df)
        if df_pane in main.objects:
            main.remove(df_pane)
        main.append(df_pane)
        #return df
    elif action_menu.clicked == 'insert':
        idol_data = [main_row_idol_id.value, main_row_name.value, main_row_stage_name.value, main_row_group.value,
                    main_row_company.value, main_row_country.value, main_row_birthdate.value, main_row_height.value]
        inserts.idol_insert_row(conn, table_menu.clicked, idol_data)
    elif action_menu.clicked == 'edit':
        edits.edit_query(conn, table_menu.clicked, edit_col, edit_idol_id, edit_row, edit_new_val)
    elif action_menu.clicked == 'delete':
        deletes.delete_row(conn, table_menu.clicked, 'idol_id', delete_input.value)

def action_row(event):
    main.objects = [main_row]
    main_sub_row.objects = []
    if action_menu.clicked == 'select':
        main_sub_row.objects = [select_tool_tip, select_input]
    elif action_menu.clicked == 'insert':
        main_sub_row.objects = [main_row_idol_id, main_row_name, main_row_stage_name, main_row_group, main_row_company, main_row_country, main_row_birthdate, main_row_height]
    elif action_menu.clicked == 'edit':
        main_sub_row.objects = [edit_idol_id, edit_col, edit_row, edit_new_val]
    elif action_menu.clicked == 'delete':
        main_sub_row.objects = [delete_input]

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
select_input = pn.widgets.IntInput(name='Input an idol_id') #TODO search bar, input name of idol, company, or group then show result
select_tool_tip = pn.widgets.TooltipIcon(value='Input 0 to SELECT ALL')

#action menu insert
main_row_idol_id = pn.widgets.IntInput(name='id')
main_row_name = pn.widgets.TextInput(name='name')
main_row_stage_name = pn.widgets.TextInput(name='stage_name')
main_row_group = pn.widgets.TextInput(name='group')
main_row_company = pn.widgets.TextInput(name='company')
main_row_country = pn.widgets.TextInput(name='country')
main_row_birthdate = pn.widgets.TextInput(name='birthdate')
main_row_height = pn.widgets.IntInput(name='height (cm)')

#action menu edit
edit_idol_id = pn.widgets.IntInput(name='id')
edit_col = pn.widgets.TextInput(name='column to change')
edit_row = pn.widgets.TextInput(name='row of id')
edit_new_val = pn.widgets.TextInput(name='new value')

#action menu delete 
delete_input = pn.widgets.TextInput(name='input id')

app = pn.Tabs(('Main', main), ('Report'))

app.servable()



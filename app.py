import panel as pn
import pandas as pd

import inserts
import selects
import connect

def get_data(event):
    df = selects.select_data(conn, select_input.value)
    df_pane = pn.pane.DataFrame(df)
    if df_pane in t1.objects:
        t1.remove(df_pane)
    t1.append(df_pane)
    return df

def input_row(event):
    idol_data = [t2_idol_id.value, t2_name.value, t2_stage_name.value, t2_group.value, t2_company.value, t2_country.value, t2_birthdate.value, t2_height.value]
    inserts.idol_insert_row(conn, idol_data)

conn = connect.db_conn()
pn.extension(sizing_mode='stretch_width')

select_input = pn.widgets.IntInput(name='Input an idol_id or 0 to SELECT ALL')
t1_button = pn.widgets.Button(name='Enter', button_type='primary')
t1_button.on_click(get_data)

t1 = pn.Column(select_input, t1_button)

t2_idol_id = pn.widgets.IntInput(name='id')
t2_name = pn.widgets.TextInput(name='name')
t2_stage_name = pn.widgets.TextInput(name='stage_name')
t2_group = pn.widgets.TextInput(name='group')
t2_company = pn.widgets.TextInput(name='company')
t2_country = pn.widgets.TextInput(name='country')
t2_birthdate = pn.widgets.TextInput(name='birthdate')
t2_height = pn.widgets.IntInput(name='height (cm)')

t2_insert_data = pn.Row(t2_idol_id, t2_name, t2_stage_name, t2_group, t2_company, t2_country, t2_birthdate, t2_height)
t2_button = pn.widgets.Button(name='Enter', button_type='primary')
t2_button.on_click(input_row)
t2 = pn.Column(t2_insert_data, t2_button)

app = pn.Tabs(('Select', t1), ('Insert', t2))

app.servable()



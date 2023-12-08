import panel as pn

#insert actions
def select():
    select_input = pn.widgets.IntInput(name='Input an idol_id') #TODO search bar, input name of idol, company, or group then show result
    select_tool_tip = pn.widgets.TooltipIcon(value='Input 0 to SELECT ALL')
    return [select_input, select_tool_tip]

def insert():
    insert_idol_id = pn.widgets.IntInput(name='id')
    insert_name = pn.widgets.TextInput(name='name')
    insert_stage_name = pn.widgets.TextInput(name='stage_name')
    insert_group = pn.widgets.TextInput(name='group')
    insert_company = pn.widgets.TextInput(name='company')
    insert_country = pn.widgets.TextInput(name='country')
    insert_birthdate = pn.widgets.TextInput(name='birthdate')
    insert_height = pn.widgets.IntInput(name='height (cm)')
    return [insert_idol_id, insert_name, insert_stage_name, insert_group, insert_company, insert_country, insert_birthdate, insert_height]
#edit actions
def edit():
    edit_col = pn.widgets.TextInput(name='column to change')
    edit_idol_id = pn.widgets.IntInput(name='id')
    edit_row = pn.widgets.TextInput(name='row of id')
    edit_new_val = pn.widgets.TextInput(name='new value')
    return [edit_col, edit_idol_id, edit_row, edit_new_val]

#delete actions
def delete():
    delete_input = pn.widgets.TextInput(name='input id')
    return [delete_input]
import panel as pn

def select():
    select_input = pn.widgets.IntInput(name='Input an id')
    select_tool_tip = pn.widgets.TooltipIcon(value='Input -1 to SELECT ALL')
    select_report = pn.widgets.Select(name='Only select', options={'none':'none','group':'group_', 'company':'company', 'gender':'gender'})
    select_report_input = pn.widgets.TextInput(name='input')
    return [select_input, select_tool_tip, select_report, select_report_input]

def idol_insert():
    insert_idol_id = pn.widgets.IntInput(name='id')
    insert_name = pn.widgets.TextInput(name='name')
    insert_stage_name = pn.widgets.TextInput(name='stage_name')
    insert_group = pn.widgets.TextInput(name='group')
    insert_company = pn.widgets.TextInput(name='company')
    insert_country = pn.widgets.TextInput(name='country')
    insert_birthdate = pn.widgets.TextInput(name='birthdate')
    insert_gender = pn.widgets.Select(name='gender', options=['Male', 'Female', 'Other'])
    insert_height = pn.widgets.IntInput(name='height (cm)')
    return [insert_idol_id, insert_name, insert_stage_name, insert_group, insert_company, insert_country, insert_birthdate, insert_gender, insert_height]

def group_insert():
    insert_id = pn.widgets.IntInput(name='id')
    insert_name = pn.widgets.TextInput(name='group name')
    insert_code = pn.widgets.TextInput(name='code')
    insert_company = pn.widgets.TextInput(name='company')
    insert_members = pn.widgets.IntInput(name='number of members')
    return [insert_id, insert_name, insert_code, insert_company, insert_members]

def company_insert():
    insert_id = pn.widgets.IntInput(name='id')
    insert_name = pn.widgets.TextInput(name='company name')
    insert_groups = pn.widgets.IntInput(name='number of groups')
    insert_members = pn.widgets.IntInput(name='number of members')
    return [insert_id, insert_name, insert_groups, insert_members]

def edit():
    edit_col = pn.widgets.TextInput(name='column to change') #TODO drop down
    edit_idol_id = pn.widgets.IntInput(name='id')
    edit_new_val = pn.widgets.TextInput(name='new value')
    return [edit_col, edit_idol_id, edit_new_val]

def delete():
    delete_input = pn.widgets.TextInput(name='id')
    return [delete_input]

def report():
    num_idols = pn.widgets.TextInput(name='number of idols', disabled=True)
    average_height = pn.widgets.TextInput(name='average height', disabled=True)
    average_age = pn.widgets.TextInput(name='average age', disabled=True)
    return [num_idols, average_height, average_age]
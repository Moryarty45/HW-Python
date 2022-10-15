import db_type.db_csv as dbc
import gui as gui

def type_csv():
    while True:
        match gui.get_func():
            case '+':
                dbc.add_new_data(gui.get_lname(), 
                                    gui.get_fname(),
                                    gui.get_phone_num())
            case '-':
                dbc.del_data(gui.get_id())
            case '=':
                dbc.find_data(gui.get_lname())
            case '?':
                dbc.read_csv()
            case '0':
                return
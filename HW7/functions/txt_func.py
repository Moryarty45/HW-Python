import db_type.db_txt as dbt
import gui as gui

def type_txt():
    while True:
        match gui.get_operation():
            case '+':
                dbt.add_new_data(gui.get_lname(), 
                                    gui.get_fname(),
                                    gui.get_phone_num())
            case '-':
                dbt.del_data(gui.get_id())
            case '=':
                dbt.find_data(gui.get_lname())
            case '?':
                dbt.read_txt()
            case '0':
                return
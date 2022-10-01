import pb_find as f
import pb_add as a
import phonebook as pb
import gui as g

def start():
    pb_temp = pb.read_pb_base()
    while True:
        match g.get_operation():
            case '+':
                pb.add_tel_number(a.new_number(a.new_id(pb_temp), 
                                            g.get_lname(), 
                                            g.get_fname(), 
                                            g.get_phone_num()))
                print('Запись успешно добавлена!')
            case '-':
                pb.delete_tel_number(g.get_id(), pb_temp)
                print('Запись успешно удалена!')
            case '=':
                f.find(g.get_lname(), pb_temp)
            case '0':
                print('До свидания!')
                break
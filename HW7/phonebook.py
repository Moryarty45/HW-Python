from datetime import datetime as dt
import pb_find as f
import pb_add as a

def add_tel_number(data):
    with open('/Users/alexey-dubovko/Desktop/Geek/Python/HW-Python/HW7/phonebook.txt', 'a', encoding="utf-8") as file:
        file.write(f'*{data}* \n')

def delete_tel_number(id, data):    
    data = ['*'.join(data[i]) for i in range(len(data)) if int(data[i][0]) != int(id)]
    with open('/Users/alexey-dubovko/Desktop/Geek/Python/HW-Python/HW7/phonebook.txt', 'w', encoding="utf-8") as file:
        for i in range(len(data)):
            file.write(f'*{data[i]}*\n')

def read_pb_base():
    with open('/Users/alexey-dubovko/Desktop/Geek/Python/HW-Python/HW7/phonebook.txt', 'r', encoding="utf-8") as file:     
        data = file.readlines()
        data = [data[i][:-1].split('*') for i in range(len(data))]
        data = [data[i][1:-1] for i in range(len(data))]
    return data
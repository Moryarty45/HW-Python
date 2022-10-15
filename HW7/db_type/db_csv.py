import logger as log

path = (r'/Users/alexey-dubovko/Desktop/Geek/Python/HW-Python/HW7/db_type/phonebook.csv')

def add_new_data(lname, fname, number):
    temp = lname + ';' + fname + ';' + number

    with open(path, 'r', encoding='utf-8', newline='\n') as file:     
        data_for_id = file.readlines()
    data_for_id = [data_for_id[i].split(';') for i in range(len(data_for_id))]
    data_for_id = [data_for_id[i][0] for i in range(len(data_for_id))]

    new_id = max(tuple(map(int, data_for_id))) + 1
    
    temp = str(new_id)  + ';' + temp

    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'{temp}\n')    
    print('Запись успешно добавлена!')
    log.logger(f'Добавлена новая запись - {temp}')

def del_data(id):
    with open(path, 'r', encoding='utf-8') as file:     
        data = file.readlines()
    data = [data[i].split(';') for i in range(len(data))]
    data = [';'.join(data[i]) for i in range(len(data)) if data[i][0] != id]

    with open(path, 'w', encoding='utf-8') as file:
        for row in data:
            file.write(f'{row}')
    print('Запись успешно удалена!')
    log.logger(f'Удалена запись - {id}')

def find_data(lname):
    with open(path, 'r', encoding='utf-8') as file:     
        data = file.readlines()
    data = [data[i][0:-1].split(';') for i in range(len(data))]
    data = [data[i] for i in range(len(data)) if data[i][1] == lname]
    data = [';'.join(data[i]) for i in range(len(data))]    
    print('Найдены совпадения: ')
    print(''.join(data))
    log.logger(f'Выполнен поиск по запросу - {lname}')

def read_csv():
    with open(path, 'r', encoding='utf-8') as file:     
        data = file.readlines()
        for row in data:
            print(row, end='')

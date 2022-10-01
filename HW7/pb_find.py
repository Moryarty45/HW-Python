def find(lname, phonebook):
    lname_list = [phonebook[i] for i in range(len(phonebook)) if phonebook[i][1] == lname]
    return print('Найдено записей:\n', 'ID: ',lname_list[0][0], 'Фамилия: ',lname_list[0][1], 'Имя: ',lname_list[0][2], 'Номер: ',lname_list[0][3])
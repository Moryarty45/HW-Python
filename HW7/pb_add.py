def new_number(id, lname, fname, phone_number):
    return '*'.join([id, lname, fname, phone_number])

def new_id(phonebook):
    id_temp = [phonebook[i][0] for i in range(len(phonebook))]
    id_list = tuple(map(int, id_temp))
    return str(max(id_list) + 1)


import functions.main_func as generalf
import functions.txt_func as txtf
import functions.csv_func as csvf

def start():
    while True:
        match generalf.choose_type_db():
            case '1':
                txtf.type_txt()
            case '2':
                csvf.type_csv()
            case '0':
                print('До свидания!')
                break
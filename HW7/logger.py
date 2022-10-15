from datetime import datetime as dt

def logger(data): 
    time = dt.now().strftime("%H:%M:%S") 
    log_string = f"{time}; {data}\n" 
    with open("/Users/alexey-dubovko/Desktop/Geek/Python/HW-Python/HW7/phonebook.log", "a") as file: 
        file.write(log_string)
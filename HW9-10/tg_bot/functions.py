from pyowm import OWM
from pyowm.utils.config import get_default_config

def weather(city):
    owm = OWM('aar7f9e7fnbc7fsgrar64hffgl7r6t9')
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    mgr = owm.weather_manager()
    obs = mgr.weather_at_place(city)
    w = obs.weather

    temp = w.temperature('celsius')['temp']
    wind = w.wind()['speed'] 
    pressure_dict = w.barometric_pressure(unit='inHg')
    press = pressure_dict['press']

    return (f'''Сейчас в городе {city}:
    Температура воздуха {round(temp)} C, 
    Давление {round(press*25.4)} мм рт.ст.,
    Сила ветра {wind} м/с''')
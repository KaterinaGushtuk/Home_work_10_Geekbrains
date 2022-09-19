from datetime import datetime as dt

def get_log(R, V):
    dtime = dt.now()
    with open('log.txt', 'a') as file:
        file.write(f'{dtime}; выражение: {V}; результат: {R}\n')
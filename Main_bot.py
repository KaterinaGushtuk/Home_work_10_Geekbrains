import Cheak_vyr_bot as Cb
import Operation_bot as Ob
import Log_bot as Lb

def main (Com):
    Vyr = Com[Com.find("#") + 1:]
    CH = Cb. chek_vyr(Vyr)
    if CH == False:
        Lb.get_log('Ошибка: не соблюдены требования к формату выражения', Vyr)
        return ('Не соблюдены требования к формату выражения')
    Res = Ob.oper(CH)
    Lb.get_log(Res, Vyr)
    return (Res)
    
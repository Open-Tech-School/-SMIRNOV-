###################################################

# происходящие в боте.
# Модуль предоставляет четыре типа уведомлений:
#
# Info - Информация.
# Warn - Предупреждение.
# Error - Ошибка.
# Success - Успех.
#
# Для того, чтобы уведомления хоть как-то выделялись,
# добавляется дата, время и указывается тип
# уведомления.

###################################################

from module import config
import datetime

def get_time():
    now = datetime.datetime.now()
    time = now.strftime(f"[%d.%m.%Y, %H:%M]")
    return time

def info(log):
    writeToFile(log)
    print(f"{get_time()} ИНФО {log}")

def warn(log):
    writeToFile(log)
    print(f"{get_time()} ВНИМАНИЕ {log}")

def error(log):
    writeToFile(log)
    print(f"{get_time()} ОШИБКА {log}")

def success(log):
    writeToFile(log)
    print(f"{get_time()} УСПЕХ {log}")

def writeToFile(log):
    perm = config.logToFile
    date = get_time()
    if perm != True:
        return
    elif perm == True:
        file = 'log.txt'
        f = open(file, 'a+')
        f.write(f'{date} | {log}\n')
        f.close()


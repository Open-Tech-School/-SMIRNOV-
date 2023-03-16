import pymysql
from module import logger

class BASEDATA:
    def __init__(self):
        self.connection = pymysql.connect(
    host="localhost", 
    port=3306, 
    user="root", 
    passwd="", 
    database="BotMareseevich")
        self.cursor = self.connection.cursor()
        return logger.success(self.connection)
    def found_itemattraction(self):
        with self.connection:
            return self.cursor.execute('')

    
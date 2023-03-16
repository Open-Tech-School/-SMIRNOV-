import pymysql
from module import logger

def connect():
    try:
        connection = pymysql.connect(
        host="localhost", 
        port=3306, 
        user="root", 
        passwd="", 
        database="BotMareseevich")
        connection.autocommit(True)
        logger.success(connection)
    except connection.Error as e:
        logger.error(e)
    
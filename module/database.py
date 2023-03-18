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
        self.connection.autocommit(True)
        return logger.success(self.connection)
        
    def found_itemattraction(self):
        with self.connection:
            return self.cursor.execute('')
            
            
    def create_usertable(self):
        with self.connection:
            return self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    id INT,
    money BIGINT,
    status TEXT,
    adm INT DEFAULT 0,
    ball BIGINT,
    timestamp TEXT)
    ''')
    
    def create_user(self, name, id, status, times):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO users VALUES ('{name}', {id}, 0, '{status}', 0, 0, '{times}')")
    
    def find_user(self, id):
        with self.connection:
            return self.cursor.execute(f'SELECT id FROM users WHERE id = {id}')
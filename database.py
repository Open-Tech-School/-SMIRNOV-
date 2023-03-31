import sqlite3
from module import logger

class BASEDATA:
    def __init__(self):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
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
    adm INT,
    ball BIGINT,
    timestamp TEXT)
    ''').connection.commit()

    def create_itemattraction(self):
        with self.connection:
            return self.cursor.execute('''CREATE TABLE IF NOT EXISTS attractions (
    name TEXT,
    URL_Google_maps,
    descriptions EXT,
    picture TEXT)
    ''').connection.commit()

    def create_user(self, name, id, status, times):
        with self.connection:
            return self.cursor.execute(f"INSERT INTO users (name, id, money, status, adm, ball, timestamp) VALUES ('{name}', {id}, 0, '{status}', 0, 0, '{times}')")
    
    def find_user(self, id):
        with self.connection:
            return self.cursor.execute(f'SELECT id FROM users WHERE id = {id}')

    def check_profile(self, id):
        with self.connection:
            return self.cursor.execute(f'SELECT name, money, status, ball, timestamp FROM users WHERE id = {id}').fetchone()
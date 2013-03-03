
import sqlite3
from db_manager import DatabaseManager

class SQLiteDBManager(DatabaseManager):
    
    def __init__(self, path):
        self.path = path
        self.conn = sqlite3.connect(path)
        return


import sqlite3
import cPickle
from db_manager import DatabaseManager

class SQLiteDBManager(DatabaseManager):
    
    def __init__(self, path):
        self.path = path
        self.conn = sqlite3.connect(path)
        return

    def make_new_session(self, 
                         values): # should be a dictionary of values
                                  # to store in the database.

        return

    # a raw call, until formalizing an extension API of some sorts
    def raw(self, call):
        return self.conn.executemany(call)

        
                          
                         

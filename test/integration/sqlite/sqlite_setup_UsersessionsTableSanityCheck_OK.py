
from dbsetup import sqlite_setup
import sqlite3
import unittest

class TestUsersessionsTable(unittest.TestCase):

    # This is done instead of a setUp() since we want to test one
    # completed installation without any serious modification.
    conn = sqlite_setup(":memory:")
    schema = None
    
    def test_usersessions_exists(self):
        
        c = self.conn.cursor()
        c.execute("SELECT type,name FROM sqlite_master WHERE type='table' and name='usersessions';")
        self.assertEquals(len(c.fetchall()), 1)


    # We have to guarantee at the current moment the following 4
    # fields exist:
    def get_schema(self):
        if self.schema is None:
            # helper method to get the schema into a dictionary
            c = self.conn.cursor()
            c.execute("PRAGMA table_info('usersessions');")
            a = c.fetchall()
        
            # Column 1 is the name of the column in the schema, and
            # column 2 is the datatype, so build a dict. An example
            # column is represented by this row:
        
            #(0, u'session_id', u'BIGINT', 0, None, 1).
            b = dict()
            for i in a:
                b[i[1]] = i[2]
            self.schema = b
            
        return self.schema

    def test_columnSessionId_exists(self):
        a = self.get_schema()
        self.assertTrue( a["session_id"] == "BIGINT" )
    
    def test_columnUserId_exists(self):
        a = self.get_schema()
        self.assertTrue( a["user_id"] == "BIGINT" )
        
    def test_columnCreated_exists(self):
        a = self.get_schema()
        self.assertTrue( a["created"] == "DATETIME" )

    def test_columnLastseen_exists(self):
        a = self.get_schema()
        self.assertTrue( a["lastseen"] == "DATETIME" )
        
    def test_columnSessionData_exists(self):
        a = self.get_schema()
        self.assertTrue( a["session_data"] == "TEXT" )
        
if __name__ == "__main__":
    unittest.main()

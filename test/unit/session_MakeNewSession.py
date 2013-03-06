
import unittest
from web.session import Session
from web.db.db_manager import DatabaseManager

class DatabaseManagerMock(DatabaseManager):
    
    def __init__(self):
        self.v = None

    def make_new_session(self, values):
        self.v = values;

    def get_dict(self):
        return self.v

class TestMakeNewSession(unittest.TestCase):
    
    def test_saveEmptySession(self):
        d = DatabaseManagerMock()
        s = Session(d)
        s.save()
        self.assertTrue(isinstance(d.get_dict(), dict), 
                        "When make_new_values of the database manager was called, we did not get an empty dict.")
        self.assertEquals(len(d.get_dict()), 0)

if __name__ == "__main__":
    unittest.main()

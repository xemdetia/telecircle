import unittest
from web.session import Session
from web.db.db_manager import DatabaseManager

class DatabaseManagerMock(DatabaseManager):
    
    def __init__(self):
        self.v = dict({'hello':'goodbye'})

    def get_session_dict(self, session_id):
        return self.v

    def replace_session(self, session_id, values):
        self.v = values

    def get_dict(self):
        return self.v

class TestMakeNewSession(unittest.TestCase):
    
    def test_saveEmptySession(self):
        d = DatabaseManagerMock()
        s = Session(d,1)

        a = d.get_dict()
        a["ok"] = "ok"
        
        s.save()
        self.assertTrue(isinstance(d.get_dict(),dict))
        self.assertEquals(len(d.get_dict()), 2)

if __name__ == "__main__":
    unittest.main()

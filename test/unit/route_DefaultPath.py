
import unittest
from web.route import Router

def route_test(env):
    return "ok"

class TestDefaultPath(unittest.TestCase):
    
    def test_DefaultPath(self):
        r = Router()
        r.set_default(route_test)
        self.assertEquals(r.go("/", {}), "ok")

if __name__ == "__main__":
    unittest.main()

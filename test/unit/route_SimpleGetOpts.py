
import unittest
from web.route import Router

def index_fn(env):
    return "index"

def about_fn(env):
    return "about"

class TestSimpleGet(unittest.TestCase):
    
    r = None
    
    def get_router(self):
        if self.r is None:
            r = Router()
            r.add_route("^/index", index_fn)
            r.add_route("^/about", about_fn, Router.GET)
        return r
            
    def test_GetIndex(self):
        r = self.get_router()
        self.assertEquals(r.go("/index", {}), "index")

    def test_GetAbout(self):
        r = self.get_router()
        self.assertEquals(r.go("/about", {}), "about")

if __name__ == "__main__":
    unittest.main()

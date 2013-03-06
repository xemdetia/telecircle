import unittest
from web.route import Router

def index_fn(env):
    return env["url_vars"]["id"]

class TestGetOpts(unittest.TestCase):
    
    r = None
    
    def get_router(self):
        if self.r is None:
            r = Router()
            r.add_route("^/page/(?P<id>\w+)", index_fn)
        return r
            
    def test_PageWithParameter(self):
        r = self.get_router()

        self.assertEquals(r.go("/page/123456", {}), "123456")

if __name__ == "__main__":
    unittest.main()

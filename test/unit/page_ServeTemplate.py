import unittest
from web.page import Page

a = "<html><head><title>$sample</title></head><body>$sample</body></html>"
b = "<html><head><title>test sample</title></head><body>test sample</body></html>"
mapping = {'sample':'test sample'}

class TestPageServeTemplate(unittest.TestCase):
    
    def test_pageServeTemplate(self):
        
        p = Page(a, mapping)
        c = p.render()
        self.assertEquals(b,c)

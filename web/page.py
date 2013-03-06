from string import Template
class Page:
    
    # This page function is designed to take a string in as
    # page_template and a mapping (a dictionary) of keywords to
    # values. To simply everything we are using the default Python
    # templating operation found here.
    # http://docs.python.org/2/library/string.html#template-strings
    def __init__(self, page_template, mapping={}):
        self.page_template = page_template
        self.mapping = mapping
        return

    # This function applys the templating and the mapping and returns
    # a string.
    def render(self):
        t = Template(self.page_template)
        return t.safe_substitute(self.mapping)

        

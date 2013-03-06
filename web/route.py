import re

class Router:

    # As part of the routing there needs to be a distinction between
    # whether a particular URL is supposed to respond to GET requests
    # only, POST requests only or both.
    ALL = 0
    GET = 1
    POST = 2
    
    def __init__(self):
        
        # These two lists are considered completely separate and they
        # will be formed of a regex object in the fst and then the
        # actual method to be called to do anything in the snd. The
        # result of the function in the snd should be a string that
        # should be sent to the user.
        self.get_method = []
        self.post_method = []

        # By default we shouldn't have a route to anywhere. This
        # should fail overtly, as some sites might not want a
        # catchall. Again this is split between the two so to make
        # POST and GET more distinct actions
        self.default_get_route = None
        self.default_post_route = None

    # This function gives the opportunity to choose a default
    # method. This could be either an index page, some 404 page or
    # some other reason. 
    def set_default(self, route_function, method=0):

        if method == 0 or method == 1:
            self.default_get_route = route_function
        
        if method == 0 or method == 2:
            self.default_post_route = route_function
        return

    # Generally we're going to be receiving a GET to display a page,
    # so that assumption is made here in the go() syntax. Otherwise
    # method should be specified. Env is a dictionary of session
    # variables and is required while post_data is a dictionary that
    # may or may not be needed dependent on what is going on.
    def go(self, url, env, post_data={},method=1):

        result = None # initialize with failure
        lst = self.from_method_get_routes(method) # get the routes for our method

        for i in lst:
            r = i[0].match(url)
            if r is not None:
                env["url_vars"] = r.groupdict()
                result = i[1](env)
        
        default_route = self.from_method_get_default_route(method)
        if result is None and default_route is not None:
            result = default_route(env)

        return result
    
    # Helper method to switch between particular lists of tuples.
    def from_method_get_routes(self, method):
        if method == self.GET:
            return self.get_method
        elif method == self.POST:
            return self.post_method
        else:
            None

    # helper method to get one of the default routes
    def from_method_get_default_route(self, method):
        if method == self.GET:
            return self.default_get_route
        elif method == self.POST:
            return self.default_post_route
        else:
            None
        

    # Again we default to GET-routes, as it is safer to do the act
    # intended not to mutate the database at all.
    def add_route(self, pattern, route_function, method=1):

        # recurse once to apply to method 1 and method 2 separately
        if method == 0:
            self.add_route(pattern, route_function, method=1)
            method = 2

        if method == 1:
            lst = self.get_method
        elif method == 2:
            lst = self.post_method

        p = re.compile(pattern)
        lst.append((p, route_function))

        


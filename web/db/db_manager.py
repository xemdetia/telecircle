
class DatabaseManager:

    def __init__(self):
        return

    #
    # Sessions
    #
    # All three of these functions should update the 'last touched'
    # field of the database as an atomic step.
    def make_new_session(self, 
                         values): # should be a dictionary of values
                                  # to store in the database.
        return False

    def replace_session(self,
                        session_id, # UUID Long that matches the
                                    # session.
                        values):    # New dict to replace the old
                                    # dict
        return

    def get_session_dict(self,
                         session_id): # This should be a long integer
                                      # UUID that matches the session.
        return

        

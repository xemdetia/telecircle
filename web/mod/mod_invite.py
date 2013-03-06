from datetime import datetime
from uuid import uuid4

class InviteModule:
    
    def __init__(self, db_manager):

        self.db_manager = db_manager

    def issue_query(self, issuer_id):
        uuid = uuid4() # Make our uuid to insert
        timestamp = datetime.now()

        query =  "BEGIN TRANSACTION;\n"
        query += "INSERT INTO invites (invite_value, issuer_id, issued_at) VALUES "
        query += "('"+str(uuid)+"',"+str(issuer_id)+",'"+str(timestamp)+"');\n"
        query += "COMMIT;\n"

        return query

    def issue(self, issuer_id):

        self.db_manager.raw(issue_query(issuer_id))
        return

    def get_invite_query(self, invite_uuid):
        
        query = "SELECT invite_id FROM invites WHERE invite_value='"+invite_uuid+"';"
        return query

    def claim_invite_query(self, invite_id, claimer_id):
        
        date = datetime.now()
        query =  "BEGIN TRANSACTION;\n"
        query += "UPDATE invites SET claimer_id="+str(claimer_id)
        query += ",claimed_at='"+str(date)+"' WHERE invite_id="+str(invite_id)+";\n"
        query += "COMMIT;"

        return query
    def claim(self, claimer_id, claim_uuid):

        return
    
    

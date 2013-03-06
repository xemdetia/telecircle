
-- This is a table for the optional module mod_invite. See the README
-- for more information.
CREATE TABLE invites (
       
       -- Simple row id
       invite_id INTEGER PRIMARY KEY AUTOINCREMENT,
       
       -- Invite id keystring, a UUID in standard form
       invite_value CHAR(36) NOT NULL,
       
       -- The person who issued the invite
       issuer_id BIGINT NOT NULL,
       issued_at DATETIME NOT NULL,

       -- The person who eventually claimed it
       claimer_id BIGINT,
       claimed_at DATETIME      
);

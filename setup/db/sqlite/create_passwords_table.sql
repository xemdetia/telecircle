
-- This is to create the passwords database. This is a simple mapping
-- of user id to password.
CREATE TABLE passwords (

       -- This lines up with the userid on the other table. I'm not
       -- sure what version of sqlite I am using so I am not going to
       -- rely on foreign keys being available. SQLite added foreign
       -- keys in version 3.6.19 as listed
       -- http://www.sqlite.org/foreignkeys.html#fk_basics. At the
       -- time of writing they were still on 3.7.15.2 for the current
       -- release.
       userid BIGINT PRIMARY KEY,

       -- Hexadecimal SHA-1 implementation (defined to be exactly 40
       -- characters). Nonces for keys are handled by the applications
       -- in question.
       pwhash CHAR(40),
       
       -- A marker for the last time the password was changed. If
       -- anything this is for sanity checking in case there is an
       -- incursion or something else going on.
       last_changed DATETIME
);
       

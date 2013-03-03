
CREATE TABLE usersessions (

       -- session_id's are UUID's as integers
       session_id BIGINT PRIMARY KEY,
       
       -- user_id's line up with the users table
       user_id BIGINT,
              
       -- These two values encode easily the created time of the
       -- session and the time they were last seen. At creation these
       -- should be the same. When lastseen and created differ by a
       -- predetermined amount, the row should be purged from the
       -- database or at least considered invalid.
       created DATETIME,
       lastseen DATETIME
);

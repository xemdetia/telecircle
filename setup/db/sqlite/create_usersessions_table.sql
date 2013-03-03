

CREATE TABLE usersessions (

       -- 
       
       -- These two values encode easily the created time of the
       -- session and the time they were last seen. At creation these
       -- should be the same. When lastseen and created differ by a
       -- predetermined amount, the row should be purged from the
       -- database or at least considered invalid.
       created DATETIME,
       lastseen DATETIME
);
       

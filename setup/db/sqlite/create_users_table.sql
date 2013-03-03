
CREATE TABLE users (

       -- User id
       id BIGINT PRIMARY KEY,

       -- User name
       sName VARCHAR(255),

       -- User email. By default this would never be exposed.
       email VARCHAR(254)
);

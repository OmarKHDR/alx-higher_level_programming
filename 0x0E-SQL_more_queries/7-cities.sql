-- - --

CREATE DATABASE if NOT EXISTS hbtn_0d_usa; 
CREATE TABLE if NOT EXISTS hbtn_0d_usa.cities
(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY state_id REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);

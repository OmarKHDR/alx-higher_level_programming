-- = --

CREATE DATABASE if NOT EXISTS hbtn_0d_2;
CREATE USER if NOT EXISTS user_0d_2@localhost;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
FLUSH PRIVILEGES;
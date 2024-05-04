#!/usr/bin/bash

/*
this script prepares a MYSQL server for the project
 will be creating a new database hbnb_dev_db
 will be creating a new user hbnb_dev (in localhost)
 password will be set to hbnb_dev_pwd
 hbnb_dev will have all privileged on the database hbnb_dev_db
 hbnb_dev will have SELECT privilege on performance_schema
 if the database hbnb_dev_db and hbnb_dev already exits, the script will fail
 checking if the database exists
*/

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

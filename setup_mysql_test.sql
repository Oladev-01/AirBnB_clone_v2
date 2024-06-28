#!/usr/bin/bash

-- this script creates a new database hbnb_test_db
-- new user hbnb_test in localhost
-- password of the new user set to hbnb_test_pwd
-- user will have all privileges on the created database
-- user will have SELECT privileges on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test' @'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_test' @'localhost';
FLUSH PRIVILEGES;

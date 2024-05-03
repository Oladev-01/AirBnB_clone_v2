#!/usr/bin/bash
# this script prepares a MYSQL server for the project
# will be creating a new database hbnb_dev_db
# will be creating a new user hbnb_dev (in localhost)
# password will be set to hbnb_dev_pwd
# hbnb_dev will have all privileged on the database hbnb_dev_db
# hbnb_dev will have SELECT privilege on performance_schema
# if the database hbnb_dev_db and hbnb_dev already exits, the script will fail
HBNB_MYSQL_DB="hbnb_dev_db"
HBNB_MYSQL_PWD="hbnb_dev_pwd"
HBNB_MYSQL_HOST="localhost"
HBNB_MYSQL_USER="hbnb_dev"

# checking if the database exists
echo "CREATE DATABASE IF NOT EXISTS ${HBNB_MYSQL_DB};" | mysql -u root -p

if ! mysql -u root -p -e "SELECT 1 FROM mysql.user WHERE user='${HBNB_MYSQL_USER}'" | grep -q 1; then
    echo "CREATE USER '${HBNB_MYSQL_USER}'@'localhost' IDENTIFIED BY '${HBNB_MYSQL_PWD}';" | mysql -u root -p
    echo "GRANT ALL PRIVILEGES ON ${HBNB_MYSQL_DB}.* TO '${HBNB_MYSQL_USER}'@'localhost';" | mysql -u root -p
    echo "GRANT SELECT ON performance_schema.* TO '${HBNB_MYSQL_USER}'@'localhost';" | mysql -u root -p
    echo "FLUSH PRIVILEGES;" | mysql -u root -p
fi
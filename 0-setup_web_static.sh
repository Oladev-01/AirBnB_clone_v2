#!/usr/bin/env bash
# This script is used to automate some instructions, setting up the web servers for deployment
# of web static

# Checking if nginx is installed or not before installing on the server
if [ ! -x "$(command -v nginx)" ]; then
    sudo apt update
    sudo apt install -y nginx
fi
sudo ufw allow 'Nginx HTTP'


# Checks if the folder "/data/" exists before creating a new one
if [ ! -d "/data/" ]; then
    sudo mkdir -p /data
fi

# Checks if the folder "/data/web_static/" exists before creating a new one
if [ ! -d "/data/web_static/" ]; then
    sudo mkdir -p /data/web_static/
fi

# Checks if the folder "/data/web_static/releases/" exists before creating a new one
if [ ! -d "/data/web_static/releases/" ]; then
    sudo mkdir -p /data/web_static/releases/
fi

# Checks if the folder "/data/web_static/shared/" exists before creating a new one
if [ ! -d "/data/web_static/shared/" ]; then
    sudo mkdir -p /data/web_static/shared/
fi

# Creating a simple html file for test
sudo mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Creating a sym link even if it exists
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Setting ownership of user and group of the folder '/data/' recursively to ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Updating the nginx config to serve the page from /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
# Restarting nginx to load the configuration
sudo service nginx restart
exit 0;


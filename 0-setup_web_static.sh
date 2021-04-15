#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

# Install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
ufw allow 'Nginx HTTP'

# Create directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create index
echo "<html>
  <head>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart

exit 0

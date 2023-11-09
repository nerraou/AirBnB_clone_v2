#!/usr/bin/env bash
# set up your web servers for the deployment of web_static
# install nginx if not exists
nginx -v > /dev/null 2>&1 || ( apt update -y && apt install -y nginx )
# create /data folders
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
# create index.html with simple content
html_content=\
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo -n "$html_content" | tee /data/web_static/releases/test/index.html > /dev/null
# remove and create symblic link if already exists
rm -f /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# change /data ownership to ubuntu user
chown -R ubuntu:ubuntu /data

# nginx config
nginx_config=\
"server {
	listen 80 default_server;
	listen [::]:80 default_server;
	server_name _;

	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	location /hbnb_static {
        alias /data/web_static/current/;
		try_files \$uri \$uri/ =404;
	}

	error_page 404 /404.html;
	location = /404.html {
		internal;
	}
}
"

echo -n "$nginx_config" | tee /etc/nginx/sites-enabled/default > /dev/null
service nginx restart

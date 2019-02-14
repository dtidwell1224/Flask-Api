# Flask-Api
This was written on Fedora 29.
Place "webapi.service" in your systemd services file location.
Download nginx and replace your "nginx.conf" file in /etc/nginx with the provided file(the provided will require a certificate).
The "api.py" can be run from any location, but the virtualenv will need setup.
In this case, I ran the following:
mkdir /etc/webapi/pyrest/; cd /etc/webapi/; virtualenv pyrest.

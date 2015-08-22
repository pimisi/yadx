import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir(
    '/opt/rh/httpd24/root/var/www/django_projects/.virtualenvs/yadx-env/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/opt/rh/httpd24/root/var/www/django_projects/YAdX')
sys.path.append('/opt/rh/httpd24/root/var/www/django_projects/YAdX/yadx_digital')

os.environ['DJANGO_SETTINGS_MODULE'] = 'yadx_digital.settings'

# Activate your virtual env
activate_env=os.path.expanduser(
    "/opt/rh/httpd24/root/var/www/django_projects/.virtualenvs/yadx-env/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
# application = django.core.handlers.wsgi.WSGIHandler()
application = get_wsgi_application()
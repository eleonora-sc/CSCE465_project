import sys

sys.path.insert(0, '/var/www/basic-flask-app')

activate_this = '/home/caden/.local/share/virtualenvs/caden-t2GVPQiy/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import app as application
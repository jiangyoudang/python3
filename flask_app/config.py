WTF_CSRF_ENABLED = True

SECRET_KEY = 'secret'



OPENID_PROVIDER = [
    {'name': 'google', 'url': 'https://www.google.com/accounts/o8/id'}

]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = os.path.join(basedir, 'app.db')
DATABASE_REPO = os.path.join(basedir, 'db_repo')
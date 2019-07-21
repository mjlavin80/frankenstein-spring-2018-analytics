import os
#SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/datastore.db' % (os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://mjlavin80:Rh2^sza1LvFF94@138.68.16.68:3306/nyt_web_app'

SQLALCHEMY_POOL_RECYCLE = 3600
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True

SECRET_KEY = 'gskkrkemensbagakdoeksmss'

# Set these values
GITHUB_CLIENT_ID = '4fc5c85362694365927b'
GITHUB_CLIENT_SECRET = 'c77c3f8bfe598cb1878a1512e5b55c86e930caf1'


#for user access
GITHUB_ADMIN = "mjlavin80"

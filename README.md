# modify settings.py to use sqlite3 as db
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': 'db.sqlite3',
     }
 }
